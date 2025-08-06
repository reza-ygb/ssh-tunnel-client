<<<<<<< HEAD
# 🔒 SSH Tunnel Client

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.6+](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![Linux](https://img.shields.io/badge/platform-linux-green.svg)](https://www.linux.org/)
[![GUI](https://img.shields.io/badge/interface-GUI-orange.svg)](https://docs.python.org/3/library/tkinter.html)
[![GitHub release](https://img.shields.io/g| 🐛 **Issues** | [GitHub Issues](https://github.com/reza-ygb/ssh-tunnel-client/issues) | Bug reports, feature requests |
| 💬 **Discussions** | [GitHub Discussions](https://github.com/reza-ygb/ssh-tunnel-client/discussions) | General questions, ideas |hub/release/reza-ygb/ssh-tunnel-client.svg)](https://github.com/reza-ygb/ssh-tunnel-client/releases)
[![GitHub stars](https://img.shields.io/github/stars/reza-ygb/ssh-tunnel-client.svg)](https://github.com/reza-ygb/ssh-tunnel-client/stargazers)
[![GitHub issues](https://img.shields.io/github/issues/reza-ygb/ssh-tunnel-client.svg)](https://github.com/reza-ygb/ssh-tunnel-client/issues)

<div align="center">

## 🚀 Professional SSH Tunneling Solution

**Route all your network traffic securely through SSH connection**

*Intuitive GUI • Auto-Installation • Cross-Platform • Persian/English Interface*

![SSH Tunnel Client Demo](https://via.placeholder.com/800x400/2D3748/FFFFFF?text=SSH+Tunnel+Client+GUI+Interface)

</div>

## ⚡ One-Line Installation

**For all Linux distributions:**

```bash
curl -sSL https://raw.githubusercontent.com/reza-ygb/ssh-tunnel-client/main/one_line_installer.sh | bash
```

**Alternative (if you prefer wget):**

```bash
wget -qO- https://raw.githubusercontent.com/reza-ygb/ssh-tunnel-client/main/one_line_installer.sh | bash
```

That's it! The installer will:
- ✅ Detect your Linux distribution automatically
- ✅ Install Python 3.6+ if needed
- ✅ Download and setup SSH Tunnel Client
- ✅ Create desktop shortcut
- ✅ Setup launcher script

---

## ✨ Features

### 🔐 Security & Privacy
- **🛡️ Military-grade SSH encryption** - All traffic encrypted end-to-end
- **🚫 Zero password storage** - Credentials never saved to disk
- **🔒 Secure connection testing** - Verify before establishing tunnel
- **🧹 Clean disconnect** - Automatically restores all network settings
- **📝 Activity logging** - Complete security audit trail

### 🖥️ User Experience  
- **🎨 Beautiful GUI interface** - Modern, intuitive design
- **🌍 Bilingual support** - Full Persian and English interface
- **⚡ One-click connection** - Connect with single button press
- **📊 Real-time monitoring** - Live connection status and statistics
- **💾 Profile management** - Save server configurations (no passwords)

### 🐧 System Compatibility
- **📦 Universal installer** - Works on ALL Linux distributions
- **🔧 Auto-dependency management** - Installs everything automatically
- **🏃 Lightweight** - Minimal system resources required
- **🔄 Background operation** - Runs silently in background
- **🚀 Fast startup** - Ready to use in seconds

### 🌐 Network Features
- **🔀 Complete traffic routing** - Routes ALL internet traffic through tunnel
- **🏎️ High-speed tunneling** - Optimized for maximum performance
- **🌐 DNS leak protection** - Prevents DNS leaks automatically
- **📡 SOCKS proxy support** - Local SOCKS5 proxy server
- **🔌 Port forwarding** - Advanced SSH port forwarding capabilities

## 🚀 Quick Start Guide

### 📥 Installation Methods

#### Method 1: One-Line Auto-Install (Recommended)
```bash
# Universal installer for all Linux distributions
curl -sSL https://raw.githubusercontent.com/reza-ygb/ssh-tunnel-client/main/one_line_installer.sh | bash

# Launch the application
./run.sh
```

#### Method 2: Manual Download
```bash
# Download the main application file
wget https://raw.githubusercontent.com/reza-ygb/ssh-tunnel-client/main/ssh_tunnel_client.py

# Make it executable and run
chmod +x ssh_tunnel_client.py
sudo python3 ssh_tunnel_client.py
```

#### Method 3: Git Clone (For Developers)
```bash
# Clone the repository
git clone https://github.com/reza-ygb/ssh-tunnel-client.git
cd ssh-tunnel-client

# Run directly
sudo python3 ssh_tunnel_client.py
```

### 🎯 Usage Steps

1. **📋 Enter SSH Server Details**
   - Server IP or hostname
   - SSH port (usually 22)
   - Username
   - Password

2. **🔍 Test Connection**
   - Click "Test Connection" to verify SSH access
   - Green checkmark indicates successful connection

3. **🔗 Establish Tunnel**
   - Click "Connect" to start SSH tunnel
   - All internet traffic will route through your SSH server

4. **📊 Monitor Status**
   - Real-time connection status in the GUI
   - Activity logs show all operations

5. **🔚 Disconnect**
   - Click "Disconnect" to stop tunnel
   - Network settings automatically restored

## 🔧 Requirements

- **OS**: Linux (any distribution)
- **Python**: 3.6+
- **Privileges**: sudo/root access
- **Connection**: Internet access for initial setup

## 🌍 Supported Linux Distributions

<table>
<tr>
<td>

### 📦 Debian-based
- ✅ **Ubuntu** (18.04, 20.04, 22.04, 24.04)
- ✅ **Debian** (9, 10, 11, 12)
- ✅ **Linux Mint** (19, 20, 21)
- ✅ **Elementary OS**
- ✅ **Pop!_OS**
- ✅ **Zorin OS**

</td>
<td>

### 🔴 Red Hat-based
- ✅ **CentOS** (7, 8, Stream)
- ✅ **RHEL** (7, 8, 9)
- ✅ **Fedora** (35, 36, 37, 38)
- ✅ **Rocky Linux**
- ✅ **AlmaLinux**
- ✅ **Oracle Linux**

</td>
</tr>
<tr>
<td>

### 🏔️ Arch-based
- ✅ **Arch Linux**
- ✅ **Manjaro**
- ✅ **EndeavourOS**
- ✅ **Garuda Linux**

</td>
<td>

### 🦎 openSUSE-based
- ✅ **openSUSE Leap**
- ✅ **openSUSE Tumbleweed**
- ✅ **SUSE Linux Enterprise**

</td>
</tr>
</table>

**Package Managers Supported:** `apt`, `yum`, `dnf`, `pacman`, `zypper`, `apk`

## 🔒 Security & Privacy Features

<div align="center">

| Feature | Description | Status |
|---------|-------------|--------|
| � **SSH Encryption** | Military-grade AES encryption | ✅ Active |
| 🚫 **No Data Storage** | Zero credential storage | ✅ Active |
| 🛡️ **DNS Protection** | Prevents DNS leaks | ✅ Active |
| 🧹 **Clean Disconnect** | Restores original settings | ✅ Active |
| 📝 **Activity Logging** | Security audit trails | ✅ Active |
| 🔍 **Connection Testing** | Pre-connection validation | ✅ Active |

</div>

### 🛡️ Privacy Guarantees
- **No tracking or analytics** - Your privacy is sacred
- **No data collection** - We don't collect any personal information
- **No credential storage** - Passwords never touch the disk
- **Open source** - Full transparency, audit the code yourself
- **Local operation** - Everything runs on your machine

### 🔐 Encryption Details
- **Protocol**: SSH-2 with latest security standards
- **Key Exchange**: ECDH, DH Group 14+ SHA-256
- **Encryption**: AES-128/192/256-CTR, ChaCha20-Poly1305
- **MAC**: HMAC-SHA2-256, HMAC-SHA2-512
- **Compression**: Optional zlib compression  

## 📱 User Interface

<div align="center">

### 🎨 Modern GUI Design

| Component | Description |
|-----------|-------------|
| 🌐 **Server Configuration** | Easy SSH server setup panel |
| 🔗 **Connection Controls** | One-click connect/disconnect buttons |
| 📊 **Status Monitoring** | Real-time connection status display |
| 📝 **Activity Logs** | Live activity feed with timestamps |
| 💾 **Profile Manager** | Save and load server configurations |
| 🌍 **Language Toggle** | Switch between Persian and English |

</div>

### 🎯 Key Features
- **Responsive design** - Works on all screen sizes
- **Intuitive layout** - No learning curve required
- **Visual feedback** - Clear status indicators and animations
- **Error handling** - User-friendly error messages
- **Accessibility** - Keyboard shortcuts and screen reader support
- **Theme support** - Light theme with professional appearance

## 🛠️ Troubleshooting & FAQ

### ❓ Common Questions

<details>
<summary><strong>🔧 Installation Issues</strong></summary>

**Q: Installation fails with "Permission denied"**
```bash
# Make sure you have sudo access
sudo whoami

# Try manual installation
wget https://raw.githubusercontent.com/reza-ygb/ssh-tunnel-client/main/ssh_tunnel_client.py
sudo python3 ssh_tunnel_client.py
```

**Q: Python not found**
```bash
# Install Python 3.6+
# Ubuntu/Debian:
sudo apt update && sudo apt install python3 python3-pip

# CentOS/RHEL:
sudo yum install python3 python3-pip

# Fedora:
sudo dnf install python3 python3-pip
```

**Q: Package manager not supported**
```bash
# Download and run manually
wget https://raw.githubusercontent.com/reza-ygb/ssh-tunnel-client/main/ssh_tunnel_client.py
sudo python3 ssh_tunnel_client.py
```

</details>

<details>
<summary><strong>🔗 Connection Issues</strong></summary>

**Q: SSH connection failed**
- ✅ Verify server IP and port (usually 22)
- ✅ Check username and password
- ✅ Ensure SSH service is running: `sudo systemctl status ssh`
- ✅ Test manual SSH: `ssh user@server`

**Q: Connection drops frequently**
```bash
# Add keep-alive to SSH config
echo "ServerAliveInterval 60" >> ~/.ssh/config
echo "ServerAliveCountMax 3" >> ~/.ssh/config
```

**Q: Slow connection speed**
- Use servers geographically closer to you
- Check your internet connection speed
- Try different SSH encryption algorithms

</details>

<details>
<summary><strong>🌐 Network Issues</strong></summary>

**Q: DNS not working**
```bash
# Check DNS settings
cat /etc/resolv.conf

# Test DNS resolution
nslookup google.com

# Reset network (if disconnected improperly)
sudo systemctl restart NetworkManager
```

**Q: Can't access local network**
```bash
# This is expected behavior for security
# To access local network, modify routing manually
sudo ip route add 192.168.1.0/24 dev eth0
```

</details>

### 🐛 Error Messages

| Error | Cause | Solution |
|-------|-------|----------|
| `ImportError: paramiko` | Missing dependency | Let app auto-install or run `pip3 install paramiko` |
| `Permission denied (publickey)` | SSH key authentication | Use password auth or setup SSH keys |
| `Network is unreachable` | Network configuration | Check internet connection |
| `Address already in use` | Port conflict | Change SOCKS port in settings |
| `Operation not permitted` | Insufficient privileges | Run with `sudo` |

### 📋 Diagnostic Commands

```bash
# Check SSH Tunnel Client status
ps aux | grep ssh_tunnel_client

# Check network routing
ip route show

# Check DNS settings
cat /etc/resolv.conf

# Check iptables rules
sudo iptables -L -n

# Check active connections
netstat -tulpn | grep :1080

# View application logs
tail -f ssh_tunnel.log
```

## 🤝 Contributing & Community

### 🚀 How to Contribute

We welcome contributions from everyone! Here's how you can help:

<table>
<tr>
<td>

#### 🐛 **Bug Reports**
- Use our [bug report template](.github/ISSUE_TEMPLATE/bug_report.md)
- Include system information
- Provide reproduction steps
- Add relevant logs

</td>
<td>

#### 💡 **Feature Requests**
- Use our [feature request template](.github/ISSUE_TEMPLATE/feature_request.md)
- Describe the use case
- Explain the benefit
- Consider implementation

</td>
</tr>
<tr>
<td>

#### 🔧 **Code Contributions**
- Fork the repository
- Create feature branch
- Follow coding standards
- Add tests if applicable

</td>
<td>

#### 📚 **Documentation**
- Improve README
- Add usage examples
- Translate to other languages
- Create tutorials

</td>
</tr>
</table>

### 📖 Development Setup

```bash
# 1. Fork and clone
git clone https://github.com/reza-ygb/ssh-tunnel-client.git
cd ssh-tunnel-client

# 2. Create development branch
git checkout -b feature/amazing-feature

# 3. Make your changes
# Edit files...

# 4. Test your changes
sudo python3 ssh_tunnel_client.py

# 5. Commit and push
git commit -m "Add amazing feature"
git push origin feature/amazing-feature

# 6. Create Pull Request
```

### 📋 Contribution Guidelines

- **Code Style**: Follow PEP 8 for Python code
- **Security**: Never commit credentials or sensitive data
- **Testing**: Test on multiple Linux distributions
- **Documentation**: Update docs for new features
- **Licensing**: All contributions under MIT License

For detailed guidelines, see [CONTRIBUTING.md](CONTRIBUTING.md)

### 🌟 Contributors

<a href="https://github.com/reza-ygb/ssh-tunnel-client/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=reza-ygb/ssh-tunnel-client" />
</a>

*Made with [contrib.rocks](https://contrib.rocks)*

## 📄 License & Legal

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

### 🔒 Security Policy

We take security seriously. For security vulnerabilities, please see our [Security Policy](SECURITY.md).

### ⚖️ Legal Disclaimer

- This software is for educational and legitimate use only
- Users are responsible for compliance with local laws
- No warranty provided - use at your own risk
- Not affiliated with any SSH server providers

---

## 🙏 Support & Community

<div align="center">

### 🌟 Show Your Support

If this project helped you, please consider:

[![GitHub stars](https://img.shields.io/github/stars/reza-ygb/ssh-tunnel-client.svg?style=social&label=Star)](https://github.com/reza-ygb/ssh-tunnel-client/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/reza-ygb/ssh-tunnel-client.svg?style=social&label=Fork)](https://github.com/reza-ygb/ssh-tunnel-client/network)
[![GitHub watchers](https://img.shields.io/github/watchers/reza-ygb/ssh-tunnel-client.svg?style=social&label=Watch)](https://github.com/reza-ygb/ssh-tunnel-client/watchers)

</div>

### � Get Help

| Platform | Link | Purpose |
|----------|------|---------|
| �🐛 **Issues** | [GitHub Issues](https://github.com/reza-ygb/ssh-tunnel-client/issues) | Bug reports, feature requests |
| 💬 **Discussions** | [GitHub Discussions](https://github.com/reza-ygb/ssh-tunnel-client/discussions) | General questions, ideas |
| 📧 **Email** | support@ssh-tunnel-client.com | Private support |
| 🔒 **Security** | security@ssh-tunnel-client.com | Security issues |

### 📊 Project Stats

![GitHub repo size](https://img.shields.io/github/repo-size/reza-ygb/ssh-tunnel-client)
![GitHub code size](https://img.shields.io/github/languages/code-size/reza-ygb/ssh-tunnel-client)
![GitHub last commit](https://img.shields.io/github/last-commit/reza-ygb/ssh-tunnel-client)
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/reza-ygb/ssh-tunnel-client)

---

<div align="center">

## 🚀 Ready to Get Started?

```bash
curl -sSL https://raw.githubusercontent.com/reza-ygb/ssh-tunnel-client/main/one_line_installer.sh | bash
```

**🔒 Secure • 🚀 Fast • 🎯 Simple • 🌍 Universal**

*Made with ❤️ for the Linux community*

</div>
=======
# ssh-tunnel-client
Redirect all network traffic through SSH – lightweight tunnel client
>>>>>>> 9e24387f80673a842a8a7c8398b8a94ec5e71774
