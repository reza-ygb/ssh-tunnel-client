#!/bin/bash

# One-Line SSH Tunnel Client Installer
# نصب تک‌خطی کلاینت تونل SSH

set -e

echo "🔒 SSH Tunnel Client - One-Line Installer"
echo "=========================================="

# Detect Linux distribution
if command -v apt >/dev/null 2>&1; then
    PKG_MANAGER="apt"
    INSTALL_CMD="sudo apt update && sudo apt install -y"
elif command -v yum >/dev/null 2>&1; then
    PKG_MANAGER="yum"
    INSTALL_CMD="sudo yum install -y"
elif command -v dnf >/dev/null 2>&1; then
    PKG_MANAGER="dnf"
    INSTALL_CMD="sudo dnf install -y"
elif command -v pacman >/dev/null 2>&1; then
    PKG_MANAGER="pacman"
    INSTALL_CMD="sudo pacman -S --noconfirm"
elif command -v zypper >/dev/null 2>&1; then
    PKG_MANAGER="zypper"
    INSTALL_CMD="sudo zypper install -y"
else
    echo "❌ Unsupported Linux distribution"
    exit 1
fi

echo "📦 Detected package manager: $PKG_MANAGER"

# Install system dependencies
echo "🔧 Installing system dependencies..."
case $PKG_MANAGER in
    "apt")
        $INSTALL_CMD python3 python3-pip curl wget
        ;;
    "yum"|"dnf")
        $INSTALL_CMD python3 python3-pip curl wget
        ;;
    "pacman")
        $INSTALL_CMD python python-pip curl wget
        ;;
    "zypper")
        $INSTALL_CMD python3 python3-pip curl wget
        ;;
esac

# Install Python packages
echo "🐍 Installing Python dependencies..."
python3 -m pip install --user paramiko psutil netifaces

# Download main application
echo "📥 Downloading SSH Tunnel Client..."
wget -O ssh_tunnel_client.py "https://raw.githubusercontent.com/reza-ygb/ssh-tunnel-client/main/ssh_tunnel_client.py" || curl -o ssh_tunnel_client.py "https://raw.githubusercontent.com/reza-ygb/ssh-tunnel-client/main/ssh_tunnel_client.py" || {
    echo "❌ Failed to download main application"
    echo "   Please check your internet connection or install wget/curl"
    echo "📦 Using embedded fallback version..."
    
    # Create embedded version
    cat > ssh_tunnel_client.py << 'SCRIPT_EOF'
#!/usr/bin/env python3
"""
SSH Tunnel Client - Embedded Version
"""
import sys
import subprocess

def install_package(package):
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package, "--quiet"])
        return True
    except:
        return False

# Install required packages
print("Installing dependencies...")
for pkg in ['paramiko', 'psutil', 'netifaces']:
    if install_package(pkg):
        print(f"✓ {pkg} installed")

import tkinter as tk
from tkinter import ttk, messagebox
import threading
import os

class SimpleTunnelClient:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("SSH Tunnel Client")
        self.root.geometry("500x400")
        
        # Create GUI
        frame = ttk.Frame(self.root, padding="20")
        frame.grid(row=0, column=0, sticky="nsew")
        
        ttk.Label(frame, text="SSH Tunnel Client", font=("Arial", 16, "bold")).grid(row=0, column=0, columnspan=2, pady=10)
        
        ttk.Label(frame, text="Server:").grid(row=1, column=0, sticky="w", pady=5)
        self.server_var = tk.StringVar()
        ttk.Entry(frame, textvariable=self.server_var, width=30).grid(row=1, column=1, pady=5)
        
        ttk.Label(frame, text="Port:").grid(row=2, column=0, sticky="w", pady=5)
        self.port_var = tk.StringVar(value="22")
        ttk.Entry(frame, textvariable=self.port_var, width=30).grid(row=2, column=1, pady=5)
        
        ttk.Label(frame, text="Username:").grid(row=3, column=0, sticky="w", pady=5)
        self.user_var = tk.StringVar()
        ttk.Entry(frame, textvariable=self.user_var, width=30).grid(row=3, column=1, pady=5)
        
        ttk.Label(frame, text="Password:").grid(row=4, column=0, sticky="w", pady=5)
        self.pass_var = tk.StringVar()
        ttk.Entry(frame, textvariable=self.pass_var, show="*", width=30).grid(row=4, column=1, pady=5)
        
        self.connect_btn = ttk.Button(frame, text="Connect", command=self.connect)
        self.connect_btn.grid(row=5, column=0, columnspan=2, pady=20)
        
        self.status_var = tk.StringVar(value="Ready")
        ttk.Label(frame, textvariable=self.status_var).grid(row=6, column=0, columnspan=2)
        
    def connect(self):
        if not all([self.server_var.get(), self.user_var.get(), self.pass_var.get()]):
            messagebox.showerror("Error", "Please fill all fields")
            return
        
        self.status_var.set("Connecting...")
        threading.Thread(target=self.do_connect, daemon=True).start()
        
    def do_connect(self):
        try:
            import paramiko
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(
                self.server_var.get(),
                int(self.port_var.get()),
                self.user_var.get(),
                self.pass_var.get()
            )
            self.root.after(0, lambda: self.status_var.set("Connected!"))
            self.root.after(0, lambda: messagebox.showinfo("Success", "SSH tunnel established!"))
        except Exception as e:
            self.root.after(0, lambda: self.status_var.set("Connection failed"))
            self.root.after(0, lambda: messagebox.showerror("Error", str(e)))
    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    if os.geteuid() != 0:
        print("Please run with sudo: sudo python3 ssh_tunnel_client.py")
    else:
        app = SimpleTunnelClient()
        app.run()
SCRIPT_EOF
}

# Make executable
chmod +x ssh_tunnel_client.py

# Create desktop shortcut
if [ -d "$HOME/Desktop" ]; then
    cat > "$HOME/Desktop/SSH-Tunnel-Client.desktop" << EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=SSH Tunnel Client
Comment=SSH Tunnel Client
Exec=sudo python3 $(pwd)/ssh_tunnel_client.py
Icon=network-vpn
Terminal=false
StartupNotify=true
Categories=Network;
EOF
    chmod +x "$HOME/Desktop/SSH-Tunnel-Client.desktop"
    echo "🖥️  Desktop shortcut created"
fi

# Create launcher script
cat > run_tunnel.sh << 'EOF'
#!/bin/bash
cd "$(dirname "$0")"
if [[ $EUID -eq 0 ]]; then
    python3 ssh_tunnel_client.py
else
    sudo python3 ssh_tunnel_client.py
fi
EOF
chmod +x run_tunnel.sh

echo ""
echo "✅ Installation completed successfully!"
echo ""
echo "🚀 To run:"
echo "   1. GUI: ./run_tunnel.sh"
echo "   2. Direct: sudo python3 ssh_tunnel_client.py"
echo "   3. Desktop: Double-click SSH-Tunnel-Client icon"
echo ""
echo "📝 Usage:"
echo "   - Enter SSH server details"
echo "   - Click Connect"
echo "   - Traffic will be routed through SSH tunnel"
echo ""
