# 📦 Installation Guide

Complete installation guide for SSH Tunnel Client on all Linux distributions.

## 🚀 Method 1: One-Line Install (Recommended)

### Universal Auto-Installer

This installer works on **ALL** Linux distributions automatically:

```bash
curl -sSL https://raw.githubusercontent.com/reza-ygb/ssh-tunnel-client/main/one_line_installer.sh | bash
```

**Alternative with wget:**
```bash
wget -qO- https://raw.githubusercontent.com/reza-ygb/ssh-tunnel-client/main/one_line_installer.sh | bash
```

### What the installer does:
1. ✅ **Detects your Linux distribution** automatically
2. ✅ **Installs Python 3.6+** if not present
3. ✅ **Downloads SSH Tunnel Client** from GitHub
4. ✅ **Creates desktop shortcut** for easy access
5. ✅ **Sets up launcher script** with proper permissions
6. ✅ **Tests installation** to ensure everything works

---

## 📋 Method 2: Manual Installation

### Step 1: Install Prerequisites

<details>
<summary><strong>🐧 Ubuntu / Debian / Linux Mint</strong></summary>

```bash
# Update package list
sudo apt update

# Install Python and dependencies
sudo apt install -y python3 python3-pip python3-tk curl wget

# Install GUI libraries (if not installed)
sudo apt install -y python3-tkinter
```

</details>

<details>
<summary><strong>🔴 CentOS / RHEL / Rocky Linux</strong></summary>

```bash
# Install EPEL repository (if needed)
sudo yum install -y epel-release

# Install Python and dependencies
sudo yum install -y python3 python3-pip curl wget

# Install GUI libraries
sudo yum install -y tkinter
```

</details>

<details>
<summary><strong>🔵 Fedora</strong></summary>

```bash
# Install Python and dependencies
sudo dnf install -y python3 python3-pip curl wget

# Install GUI libraries
sudo dnf install -y python3-tkinter
```

</details>

<details>
<summary><strong>🏔️ Arch Linux / Manjaro</strong></summary>

```bash
# Update system
sudo pacman -Syu

# Install Python and dependencies
sudo pacman -S --noconfirm python python-pip curl wget

# Install GUI libraries
sudo pacman -S --noconfirm tk
```

</details>

<details>
<summary><strong>🦎 openSUSE</strong></summary>

```bash
# Refresh repositories
sudo zypper refresh

# Install Python and dependencies
sudo zypper install -y python3 python3-pip curl wget

# Install GUI libraries
sudo zypper install -y python3-tk
```

</details>

### Step 2: Download SSH Tunnel Client

```bash
# Create installation directory
mkdir -p ~/ssh-tunnel-client
cd ~/ssh-tunnel-client

# Download main application
wget https://raw.githubusercontent.com/reza-ygb/ssh-tunnel-client/main/ssh_tunnel_client.py

# Download launcher script
wget https://raw.githubusercontent.com/reza-ygb/ssh-tunnel-client/main/run.sh

# Make scripts executable
chmod +x ssh_tunnel_client.py run.sh
```

### Step 3: Install Python Dependencies

```bash
# Install required Python packages
pip3 install paramiko psutil netifaces

# Or let the application auto-install them
sudo python3 ssh_tunnel_client.py
```

### Step 4: Create Desktop Shortcut (Optional)

```bash
# Create desktop entry
cat > ~/Desktop/SSH-Tunnel-Client.desktop << EOF
[Desktop Entry]
Name=SSH Tunnel Client
Name[fa]=کلاینت تونل SSH
Comment=Secure SSH tunneling with GUI
Comment[fa]=تونل امن SSH با رابط گرافیکی
Exec=bash -c 'cd ~/ssh-tunnel-client && ./run.sh'
Icon=network-vpn
Terminal=false
Type=Application
Categories=Network;Security;
EOF

# Make it executable
chmod +x ~/Desktop/SSH-Tunnel-Client.desktop
```

---

## 🐳 Method 3: Docker Installation

For isolated environment or testing:

### Create Dockerfile

```dockerfile
FROM ubuntu:22.04

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-tk \
    curl \
    wget \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY ssh_tunnel_client.py .
RUN pip3 install paramiko psutil netifaces

CMD ["python3", "ssh_tunnel_client.py"]
```

### Build and Run

```bash
# Build image
docker build -t ssh-tunnel-client .

# Run with GUI support (Linux)
docker run -it --rm \
    --net=host \
    -e DISPLAY=$DISPLAY \
    -v /tmp/.X11-unix:/tmp/.X11-unix \
    --privileged \
    ssh-tunnel-client
```

---

## 🔧 Method 4: Development Installation

For developers who want to contribute:

```bash
# 1. Fork the repository on GitHub

# 2. Clone your fork
git clone https://github.com/reza-ygb/ssh-tunnel-client.git
cd ssh-tunnel-client

# 3. Install development dependencies
pip3 install -r requirements.txt
pip3 install flake8 bandit pytest  # For testing

# 4. Run in development mode
sudo python3 ssh_tunnel_client.py

# 5. Make your changes and create pull request
```

---

## 🛠️ Troubleshooting Installation

### Common Issues

**❌ "curl: command not found"**
```bash
# Ubuntu/Debian:
sudo apt install curl

# CentOS/RHEL:
sudo yum install curl

# Fedora:
sudo dnf install curl

# Arch:
sudo pacman -S curl
```

**❌ "python3: command not found"**
```bash
# Usually means Python 3 is not installed
# Follow the manual installation steps above
```

**❌ "pip3: command not found"**
```bash
# Ubuntu/Debian:
sudo apt install python3-pip

# CentOS/RHEL:
sudo yum install python3-pip

# Fedora:
sudo dnf install python3-pip
```

**❌ "tkinter import error"**
```bash
# Ubuntu/Debian:
sudo apt install python3-tkinter

# CentOS/RHEL:
sudo yum install tkinter

# Fedora:
sudo dnf install python3-tkinter
```

**❌ "Permission denied"**
```bash
# Make sure you run with sudo for network configuration
sudo python3 ssh_tunnel_client.py
```

### Verification

Test your installation:

```bash
# Check Python version
python3 --version

# Check if GUI works
python3 -c "import tkinter; tkinter.Tk()"

# Check SSH Tunnel Client
sudo python3 ssh_tunnel_client.py --help
```

---

## 🔄 Uninstallation

To completely remove SSH Tunnel Client:

```bash
# Remove application files
rm -rf ~/ssh-tunnel-client

# Remove desktop shortcut
rm -f ~/Desktop/SSH-Tunnel-Client.desktop

# Remove Python packages (optional)
pip3 uninstall paramiko psutil netifaces

# Clean any remaining logs
sudo rm -f /var/log/ssh_tunnel.log
rm -f ~/ssh_tunnel.log
```

---

## 📞 Need Help?

If you encounter any issues during installation:

1. **Check our [Troubleshooting Guide](README.md#troubleshooting--faq)**
2. **Search [existing issues](https://github.com/reza-ygb/ssh-tunnel-client/issues)**
3. **Create a [new issue](https://github.com/reza-ygb/ssh-tunnel-client/issues/new)**
4. **Join our [discussions](https://github.com/reza-ygb/ssh-tunnel-client/discussions)**

Include the following information in your report:
- Linux distribution and version
- Python version
- Installation method attempted
- Complete error message
- Output of installation commands
