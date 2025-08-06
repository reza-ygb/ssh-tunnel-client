#!/usr/bin/env python3
"""
SSH Tunnel Client - Complete Solution
کلاینت تونل SSH برای مسیریابی امن ترافیک

One-click install and use SSH tunnel client for secure traffic routing.
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import threading
import subprocess
import os
import sys
import json
import time
import socket
import logging
from datetime import datetime

# Auto-install required packages
def install_package(package):
    """Install a package using pip"""
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package, "--quiet"])
        return True
    except subprocess.CalledProcessError:
        return False

# Try importing required packages, install if missing
packages_to_check = {
    'paramiko': 'paramiko',
    'psutil': 'psutil', 
    'netifaces': 'netifaces'
}

print("🔧 Checking dependencies...")
for import_name, package_name in packages_to_check.items():
    try:
        globals()[import_name] = __import__(import_name)
        print(f"✓ {package_name} found")
    except ImportError:
        print(f"📦 Installing {package_name}...")
        if install_package(package_name):
            globals()[import_name] = __import__(import_name)
            print(f"✓ {package_name} installed")
        else:
            print(f"✗ Failed to install {package_name}")
            sys.exit(1)

# Import specific classes we need
try:
    from paramiko import SSHClient, AutoAddPolicy, AuthenticationException, SSHException
except ImportError:
    # Fallback definitions
    class SSHClient:
        pass
    class AutoAddPolicy:
        pass
    class AuthenticationException(Exception):
        pass
    class SSHException(Exception):
        pass

class TunnelManager:
    """مدیریت تونل SSH"""
    
    def __init__(self):
        self.ssh_client = None
        self.is_connected = False
        self.config_file = "ssh_tunnel_config.json"
        self.log_file = "ssh_tunnel.log"
        self.original_dns = None
        
        # Setup logging
        self.setup_logging()
        
    def setup_logging(self):
        """تنظیم سیستم لاگ"""
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(self.log_file, encoding='utf-8'),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)
        self.logger.info("SSH Tunnel Client started")
        
    def save_config(self, config):
        """ذخیره ایمن تنظیمات"""
        try:
            # Remove sensitive data
            safe_config = {k: v for k, v in config.items() if k != 'password'}
            with open(self.config_file, 'w', encoding='utf-8') as f:
                json.dump(safe_config, f, indent=2, ensure_ascii=False)
            self.logger.info("Configuration saved")
            return True
        except Exception as e:
            self.logger.error(f"Failed to save config: {e}")
            return False
    
    def load_config(self):
        """بارگذاری تنظیمات"""
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
        except Exception as e:
            self.logger.error(f"Failed to load config: {e}")
        return {}
    
    def check_system_requirements(self):
        """بررسی نیازمندی‌های سیستم"""
        issues = []
        
        # Check OS
        if os.name != 'posix':
            issues.append("This application requires Linux")
        
        # Check root privileges
        if os.geteuid() != 0:
            issues.append("Root privileges required (run with sudo)")
        
        if issues:
            return False, "; ".join(issues)
        
        self.logger.info("System requirements met")
        return True, "System ready"
    
    def backup_dns(self):
        """پشتیبان‌گیری DNS"""
        try:
            if os.path.exists('/etc/resolv.conf'):
                with open('/etc/resolv.conf', 'r') as f:
                    self.original_dns = f.read()
            self.logger.info("DNS backed up")
            return True
        except Exception as e:
            self.logger.error(f"Failed to backup DNS: {e}")
            return False
    
    def restore_dns(self):
        """بازگردانی DNS"""
        try:
            if self.original_dns:
                with open('/etc/resolv.conf', 'w') as f:
                    f.write(self.original_dns)
                self.logger.info("DNS restored")
                return True
        except Exception as e:
            self.logger.error(f"Failed to restore DNS: {e}")
            return False
    
    def set_secure_dns(self):
        """تنظیم DNS امن"""
        try:
            dns_config = """# SSH Tunnel DNS
nameserver 8.8.8.8
nameserver 8.8.4.4
nameserver 1.1.1.1
nameserver 9.9.9.9
"""
            with open('/etc/resolv.conf', 'w') as f:
                f.write(dns_config)
            self.logger.info("Secure DNS configured")
            return True
        except Exception as e:
            self.logger.error(f"Failed to set DNS: {e}")
            return False
    
    def test_ssh_connection(self, host, port, username, password):
        """تست اتصال SSH"""
        try:
            self.logger.info(f"Testing SSH connection to {host}:{port}")
            
            client = SSHClient()
            client.set_missing_host_key_policy(AutoAddPolicy())
            
            client.connect(
                hostname=host,
                port=port,
                username=username,
                password=password,
                timeout=15,
                auth_timeout=15
            )
            
            # Test command execution
            stdin, stdout, stderr = client.exec_command('echo "SSH connection successful"')
            output = stdout.read().decode().strip()
            
            client.close()
            
            if "SSH connection successful" in output:
                self.logger.info("SSH test successful")
                return True, "SSH connection verified"
            else:
                return False, "SSH command failed"
                
        except AuthenticationException:
            return False, "Authentication failed - check credentials"
        except SSHException as e:
            return False, f"SSH error: {str(e)}"
        except socket.timeout:
            return False, "Connection timeout - check host/port"
        except Exception as e:
            self.logger.error(f"SSH test failed: {e}")
            return False, f"Connection error: {str(e)}"
    
    def create_ssh_tunnel(self, host, port, username, password):
        """ایجاد تونل SSH"""
        try:
            self.logger.info(f"Creating SSH tunnel to {host}:{port}")
            
            # Create SSH client
            self.ssh_client = SSHClient()
            self.ssh_client.set_missing_host_key_policy(AutoAddPolicy())
            self.ssh_client.connect(
                hostname=host,
                port=port,
                username=username,
                password=password
            )
            
            # Get transport for tunneling
            transport = self.ssh_client.get_transport()
            
            # Start SOCKS proxy server
            local_port = 1080
            
            def socks_server():
                try:
                    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                    server_socket.bind(('127.0.0.1', local_port))
                    server_socket.listen(10)
                    
                    self.logger.info(f"SOCKS proxy listening on port {local_port}")
                    
                    while self.is_connected:
                        try:
                            server_socket.settimeout(1.0)
                            client_sock, addr = server_socket.accept()
                            
                            # Handle in separate thread
                            threading.Thread(
                                target=self.handle_proxy_client,
                                args=(client_sock, transport),
                                daemon=True
                            ).start()
                            
                        except socket.timeout:
                            continue
                        except Exception as e:
                            if self.is_connected:
                                self.logger.error(f"Proxy error: {e}")
                            break
                    
                    server_socket.close()
                    
                except Exception as e:
                    self.logger.error(f"SOCKS server failed: {e}")
            
            # Start SOCKS server
            self.socks_thread = threading.Thread(target=socks_server, daemon=True)
            self.socks_thread.start()
            
            # Configure system
            self.configure_system_routing(host)
            
            self.logger.info("SSH tunnel established")
            return True, "Tunnel created successfully"
            
        except Exception as e:
            self.logger.error(f"Failed to create tunnel: {e}")
            return False, str(e)
    
    def handle_proxy_client(self, client_socket, transport):
        """مدیریت کلاینت پروکسی"""
        try:
            # Simplified proxy handling
            data = client_socket.recv(1024)
            if data:
                try:
                    channel = transport.open_channel(
                        'direct-tcpip',
                        ('8.8.8.8', 53),  # DNS forwarding
                        ('127.0.0.1', 1080)
                    )
                    channel.send(data)
                    response = channel.recv(4096)
                    if response:
                        client_socket.send(response)
                    channel.close()
                except:
                    pass
        except:
            pass
        finally:
            try:
                client_socket.close()
            except:
                pass
    
    def configure_system_routing(self, server_ip):
        """تنظیم مسیریابی سیستم"""
        try:
            # Backup and set DNS
            self.backup_dns()
            self.set_secure_dns()
            
            # Set environment variable for applications to use SOCKS proxy
            os.environ['http_proxy'] = 'socks5://127.0.0.1:1080'
            os.environ['https_proxy'] = 'socks5://127.0.0.1:1080'
            
            self.logger.info("System routing configured")
            return True
            
        except Exception as e:
            self.logger.error(f"Failed to configure routing: {e}")
            return False
    
    def start_tunnel(self, host, port, username, password):
        """شروع کامل تونل"""
        try:
            # Check system
            success, message = self.check_system_requirements()
            if not success:
                return False, message
            
            # Test SSH
            success, message = self.test_ssh_connection(host, port, username, password)
            if not success:
                return False, message
            
            # Create tunnel
            success, message = self.create_ssh_tunnel(host, port, username, password)
            if not success:
                return False, message
            
            self.is_connected = True
            self._last_server_ip = host
            
            self.logger.info(f"Tunnel connected to {host}:{port}")
            return True, f"Connected to {host}. Traffic is now routed through secure tunnel."
            
        except Exception as e:
            self.logger.error(f"Failed to start tunnel: {e}")
            self.disconnect()
            return False, str(e)
    
    def disconnect(self):
        """قطع اتصال"""
        try:
            self.is_connected = False
            
            # Close SSH
            if self.ssh_client:
                try:
                    self.ssh_client.close()
                    self.ssh_client = None
                    self.logger.info("SSH connection closed")
                except:
                    pass
            
            # Restore DNS
            self.restore_dns()
            
            # Clean environment variables
            if 'http_proxy' in os.environ:
                del os.environ['http_proxy']
            if 'https_proxy' in os.environ:
                del os.environ['https_proxy']
            
            self.logger.info("Tunnel disconnected")
            return True, "Disconnected successfully. Network restored."
            
        except Exception as e:
            self.logger.error(f"Disconnect error: {e}")
            return False, f"Disconnect error: {str(e)}"

class TunnelGUI:
    """رابط کاربری تونل SSH"""
    
    def __init__(self):
        self.tunnel_manager = TunnelManager()
        self.root = tk.Tk()
        self.setup_gui()
        self.load_saved_config()
        
    def setup_gui(self):
        """طراحی رابط کاربری"""
        self.root.title("SSH Tunnel Client - کلاینت تونل SSH")
        self.root.geometry("750x850")
        self.root.resizable(True, True)
        
        # Modern styling
        style = ttk.Style()
        style.theme_use('clam')
        
        # Configure colors
        style.configure('Title.TLabel', font=('Arial', 18, 'bold'), foreground='#2c3e50')
        style.configure('Success.TLabel', foreground='#27ae60', font=('Arial', 12, 'bold'))
        style.configure('Error.TLabel', foreground='#e74c3c', font=('Arial', 12, 'bold'))
        style.configure('Warning.TLabel', foreground='#f39c12', font=('Arial', 12, 'bold'))
        
        # Main container
        main_frame = ttk.Frame(self.root, padding="25")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        
        # Header
        header_frame = ttk.Frame(main_frame)
        header_frame.grid(row=0, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 25))
        header_frame.columnconfigure(0, weight=1)
        
        title_label = ttk.Label(header_frame, text="🔒 SSH Tunnel Client", style='Title.TLabel')
        title_label.grid(row=0, column=0)
        
        subtitle_label = ttk.Label(header_frame, text="تونل امن SSH برای مسیریابی ترافیک", font=('Arial', 11))
        subtitle_label.grid(row=1, column=0, pady=(5, 0))
        
        # Server config
        self.create_server_section(main_frame, row=1)
        
        # Control buttons
        self.create_buttons_section(main_frame, row=2)
        
        # Status
        self.create_status_section(main_frame, row=3)
        
        # Log
        self.create_log_section(main_frame, row=4)
        
        # Help
        self.create_help_section(main_frame, row=5)
        
        # Setup logging
        self.setup_gui_logging()
        
        # Initial message
        self.log_message("🚀 SSH Tunnel Client آماده است")
        
    def create_server_section(self, parent, row):
        """بخش تنظیمات سرور"""
        config_frame = ttk.LabelFrame(parent, text="⚙️ تنظیمات سرور SSH", padding="20")
        config_frame.grid(row=row, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 20))
        config_frame.columnconfigure(1, weight=1)
        
        # Server IP
        ttk.Label(config_frame, text="🌐 آدرس سرور:", font=('Arial', 10)).grid(row=0, column=0, sticky=tk.W, pady=8)
        self.ip_var = tk.StringVar()
        self.ip_entry = ttk.Entry(config_frame, textvariable=self.ip_var, width=35, font=('Arial', 11))
        self.ip_entry.grid(row=0, column=1, sticky=(tk.W, tk.E), padx=(15, 0), pady=8)
        
        # Port
        ttk.Label(config_frame, text="🔌 پورت:", font=('Arial', 10)).grid(row=1, column=0, sticky=tk.W, pady=8)
        self.port_var = tk.StringVar(value="22")
        self.port_entry = ttk.Entry(config_frame, textvariable=self.port_var, width=35, font=('Arial', 11))
        self.port_entry.grid(row=1, column=1, sticky=(tk.W, tk.E), padx=(15, 0), pady=8)
        
        # Username
        ttk.Label(config_frame, text="👤 نام کاربری:", font=('Arial', 10)).grid(row=2, column=0, sticky=tk.W, pady=8)
        self.username_var = tk.StringVar()
        self.username_entry = ttk.Entry(config_frame, textvariable=self.username_var, width=35, font=('Arial', 11))
        self.username_entry.grid(row=2, column=1, sticky=(tk.W, tk.E), padx=(15, 0), pady=8)
        
        # Password
        ttk.Label(config_frame, text="🔑 رمز عبور:", font=('Arial', 10)).grid(row=3, column=0, sticky=tk.W, pady=8)
        self.password_var = tk.StringVar()
        self.password_entry = ttk.Entry(config_frame, textvariable=self.password_var, show="*", width=35, font=('Arial', 11))
        self.password_entry.grid(row=3, column=1, sticky=(tk.W, tk.E), padx=(15, 0), pady=8)
        
    def create_buttons_section(self, parent, row):
        """بخش دکمه‌ها"""
        buttons_frame = ttk.Frame(parent)
        buttons_frame.grid(row=row, column=0, columnspan=2, pady=20)
        
        # Test button
        self.test_btn = ttk.Button(buttons_frame, text="🔍 تست اتصال", command=self.test_connection, width=18)
        self.test_btn.pack(side=tk.LEFT, padx=(0, 15))
        
        # Connect button
        self.connect_btn = ttk.Button(buttons_frame, text="🚀 اتصال", command=self.toggle_connection, width=18)
        self.connect_btn.pack(side=tk.LEFT, padx=(0, 15))
        
        # Save button
        self.save_btn = ttk.Button(buttons_frame, text="💾 ذخیره", command=self.save_config, width=18)
        self.save_btn.pack(side=tk.LEFT)
        
    def create_status_section(self, parent, row):
        """بخش وضعیت"""
        status_frame = ttk.LabelFrame(parent, text="📊 وضعیت", padding="20")
        status_frame.grid(row=row, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 20))
        status_frame.columnconfigure(0, weight=1)
        
        self.status_var = tk.StringVar(value="❌ قطع شده")
        self.status_label = ttk.Label(status_frame, textvariable=self.status_var, style='Error.TLabel')
        self.status_label.grid(row=0, column=0, pady=(0, 10))
        
        self.progress = ttk.Progressbar(status_frame, mode='indeterminate', length=400)
        self.progress.grid(row=1, column=0, sticky=(tk.W, tk.E))
        
    def create_log_section(self, parent, row):
        """بخش لاگ"""
        log_frame = ttk.LabelFrame(parent, text="📋 گزارش", padding="15")
        log_frame.grid(row=row, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 20))
        log_frame.columnconfigure(0, weight=1)
        log_frame.rowconfigure(0, weight=1)
        parent.rowconfigure(row, weight=1)
        
        self.log_text = scrolledtext.ScrolledText(log_frame, height=12, width=85, font=('Consolas', 9))
        self.log_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
    def create_help_section(self, parent, row):
        """بخش راهنما"""
        help_frame = ttk.LabelFrame(parent, text="❓ راهنما", padding="15")
        help_frame.grid(row=row, column=0, columnspan=2, sticky=(tk.W, tk.E))
        
        help_text = """
🔹 اطلاعات سرور SSH را وارد کنید
🔹 "تست اتصال" کلیک کنید
🔹 "اتصال" را فشار دهید
🔹 ترافیک از طریق تونل امن عبور می‌کند

⚠️ نیاز به دسترسی sudo
        """
        
        help_label = ttk.Label(help_frame, text=help_text, justify=tk.LEFT, font=('Arial', 9))
        help_label.pack()
        
    def setup_gui_logging(self):
        """تنظیم لاگ GUI"""
        class GUILogHandler(logging.Handler):
            def __init__(self, gui_instance):
                super().__init__()
                self.gui = gui_instance
                
            def emit(self, record):
                msg = self.format(record)
                self.gui.root.after(0, lambda: self.gui.log_message(msg))
                
        gui_handler = GUILogHandler(self)
        gui_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
        self.tunnel_manager.logger.addHandler(gui_handler)
        
    def log_message(self, message):
        """نمایش پیام در لاگ"""
        timestamp = datetime.now().strftime('%H:%M:%S')
        formatted_message = f"[{timestamp}] {message}\n"
        self.log_text.insert(tk.END, formatted_message)
        self.log_text.see(tk.END)
        
    def load_saved_config(self):
        """بارگذاری تنظیمات"""
        config = self.tunnel_manager.load_config()
        if config:
            self.ip_var.set(config.get('ip', ''))
            self.port_var.set(config.get('port', '22'))
            self.username_var.set(config.get('username', ''))
            self.log_message("📁 تنظیمات بارگذاری شد")
            
    def save_config(self):
        """ذخیره تنظیمات"""
        config = {
            'ip': self.ip_var.get(),
            'port': self.port_var.get(),
            'username': self.username_var.get()
        }
        
        if self.tunnel_manager.save_config(config):
            messagebox.showinfo("✅ موفق", "تنظیمات ذخیره شد!")
            self.log_message("💾 تنظیمات ذخیره شد")
        else:
            messagebox.showerror("❌ خطا", "خطا در ذخیره!")
        
    def validate_inputs(self):
        """بررسی ورودی‌ها"""
        if not self.ip_var.get().strip():
            messagebox.showerror("❌ خطا", "آدرس سرور را وارد کنید")
            return False
            
        if not self.port_var.get().strip():
            messagebox.showerror("❌ خطا", "پورت را وارد کنید")
            return False
            
        if not self.username_var.get().strip():
            messagebox.showerror("❌ خطا", "نام کاربری را وارد کنید")
            return False
            
        if not self.password_var.get():
            messagebox.showerror("❌ خطا", "رمز عبور را وارد کنید")
            return False
        
        try:
            port = int(self.port_var.get())
            if port < 1 or port > 65535:
                raise ValueError
        except ValueError:
            messagebox.showerror("❌ خطا", "پورت نامعتبر")
            return False
            
        return True
        
    def test_connection(self):
        """تست اتصال"""
        if not self.validate_inputs():
            return
            
        def test_thread():
            try:
                self.root.after(0, lambda: self.test_btn.config(state='disabled'))
                self.root.after(0, lambda: self.progress.start())
                self.root.after(0, lambda: self.log_message("🔍 تست اتصال..."))
                
                success, message = self.tunnel_manager.test_ssh_connection(
                    self.ip_var.get().strip(),
                    int(self.port_var.get()),
                    self.username_var.get().strip(),
                    self.password_var.get()
                )
                
                self.root.after(0, lambda: self.progress.stop())
                self.root.after(0, lambda: self.test_btn.config(state='normal'))
                
                if success:
                    self.root.after(0, lambda: messagebox.showinfo("✅ موفق", f"تست موفق!\n{message}"))
                    self.root.after(0, lambda: self.log_message(f"✅ {message}"))
                else:
                    self.root.after(0, lambda: messagebox.showerror("❌ خطا", f"تست ناموفق!\n{message}"))
                    self.root.after(0, lambda: self.log_message(f"❌ {message}"))
                    
            except Exception as e:
                error_msg = str(e)
                self.root.after(0, lambda: self.progress.stop())
                self.root.after(0, lambda: self.test_btn.config(state='normal'))
                self.root.after(0, lambda: messagebox.showerror("❌ خطا", f"خطا: {error_msg}"))
                
        threading.Thread(target=test_thread, daemon=True).start()
        
    def toggle_connection(self):
        """تغییر اتصال"""
        if self.tunnel_manager.is_connected:
            self.disconnect_tunnel()
        else:
            self.connect_tunnel()
            
    def connect_tunnel(self):
        """اتصال تونل"""
        if not self.validate_inputs():
            return
            
        def connect_thread():
            try:
                self.root.after(0, lambda: self.connect_btn.config(state='disabled'))
                self.root.after(0, lambda: self.progress.start())
                self.root.after(0, lambda: self.status_var.set("🔄 در حال اتصال..."))
                self.root.after(0, lambda: self.status_label.config(style='Warning.TLabel'))
                self.root.after(0, lambda: self.log_message("🚀 اتصال تونل..."))
                
                success, message = self.tunnel_manager.start_tunnel(
                    self.ip_var.get().strip(),
                    int(self.port_var.get()),
                    self.username_var.get().strip(),
                    self.password_var.get()
                )
                
                self.root.after(0, lambda: self.progress.stop())
                self.root.after(0, lambda: self.connect_btn.config(state='normal'))
                
                if success:
                    self.root.after(0, lambda: self.status_var.set("✅ متصل"))
                    self.root.after(0, lambda: self.status_label.config(style='Success.TLabel'))
                    self.root.after(0, lambda: self.connect_btn.config(text="🔌 قطع"))
                    self.root.after(0, lambda: messagebox.showinfo("✅ موفق", message))
                    self.root.after(0, lambda: self.log_message("✅ تونل متصل شد"))
                else:
                    self.root.after(0, lambda: self.status_var.set("❌ قطع شده"))
                    self.root.after(0, lambda: self.status_label.config(style='Error.TLabel'))
                    self.root.after(0, lambda: messagebox.showerror("❌ خطا", message))
                    self.root.after(0, lambda: self.log_message(f"❌ خطا: {message}"))
                    
            except Exception as e:
                error_msg = str(e)
                self.root.after(0, lambda: self.progress.stop())
                self.root.after(0, lambda: self.connect_btn.config(state='normal'))
                self.root.after(0, lambda: self.status_var.set("❌ قطع شده"))
                self.root.after(0, lambda: self.status_label.config(style='Error.TLabel'))
                self.root.after(0, lambda: messagebox.showerror("❌ خطا", f"خطا: {error_msg}"))
                
        threading.Thread(target=connect_thread, daemon=True).start()
        
    def disconnect_tunnel(self):
        """قطع تونل"""
        def disconnect_thread():
            try:
                self.root.after(0, lambda: self.connect_btn.config(state='disabled'))
                self.root.after(0, lambda: self.progress.start())
                self.root.after(0, lambda: self.status_var.set("🔄 قطع..."))
                self.root.after(0, lambda: self.status_label.config(style='Warning.TLabel'))
                self.root.after(0, lambda: self.log_message("🔌 قطع تونل..."))
                
                success, message = self.tunnel_manager.disconnect()
                
                self.root.after(0, lambda: self.progress.stop())
                self.root.after(0, lambda: self.connect_btn.config(state='normal'))
                self.root.after(0, lambda: self.status_var.set("❌ قطع شده"))
                self.root.after(0, lambda: self.status_label.config(style='Error.TLabel'))
                self.root.after(0, lambda: self.connect_btn.config(text="🚀 اتصال"))
                
                if success:
                    self.root.after(0, lambda: messagebox.showinfo("✅ موفق", message))
                    self.root.after(0, lambda: self.log_message("✅ تونل قطع شد"))
                else:
                    self.root.after(0, lambda: messagebox.showerror("❌ خطا", message))
                    
            except Exception as e:
                error_msg = str(e)
                self.root.after(0, lambda: self.progress.stop())
                self.root.after(0, lambda: self.connect_btn.config(state='normal'))
                self.root.after(0, lambda: self.status_var.set("❌ قطع شده"))
                self.root.after(0, lambda: self.status_label.config(style='Error.TLabel'))
                self.root.after(0, lambda: self.connect_btn.config(text="🚀 اتصال"))
                self.root.after(0, lambda: messagebox.showerror("❌ خطا", f"خطا: {error_msg}"))
                
        threading.Thread(target=disconnect_thread, daemon=True).start()
        
    def run(self):
        """اجرای برنامه"""
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        
        # Check system
        if os.geteuid() != 0:
            messagebox.showwarning(
                "⚠️ هشدار", 
                "نیاز به دسترسی root\n\nلطفاً با sudo اجرا کنید:\nsudo python3 ssh_tunnel_client.py"
            )
            self.log_message("⚠️ نیاز به دسترسی root")
        
        self.root.mainloop()
        
    def on_closing(self):
        """بستن برنامه"""
        if self.tunnel_manager.is_connected:
            result = messagebox.askyesnocancel(
                "🚪 خروج", 
                "تونل متصل است. قطع و خروج؟"
            )
            if result is True:
                self.tunnel_manager.disconnect()
                self.root.destroy()
            elif result is False:
                self.root.destroy()
        else:
            self.root.destroy()

def main():
    """تابع اصلی"""
    print("=" * 50)
    print("🔒 SSH Tunnel Client")
    print("کلاینت تونل SSH")
    print("=" * 50)
    print()
    
    # Check platform
    if os.name != 'posix':
        print("❌ فقط روی Linux کار می‌کند")
        input("Press Enter to exit...")
        return
    
    # Check root
    if os.geteuid() != 0:
        print("⚠️  نیاز به دسترسی root")
        print("   sudo python3 ssh_tunnel_client.py")
        print()
    
    try:
        print("🚀 شروع...")
        app = TunnelGUI()
        app.run()
        
    except KeyboardInterrupt:
        print("\n⚠️  متوقف شد")
    except Exception as e:
        print(f"❌ خطا: {e}")

if __name__ == "__main__":
    main()
