# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-08-06

### Added
- 🚀 Initial release of SSH Tunnel Client
- 🔐 Complete SSH tunneling functionality with secure traffic routing
- 🖥️ Intuitive GUI interface with Persian/English bilingual support
- ⚡ Auto-dependency installation system
- 🐧 Universal Linux distribution support (Ubuntu, Debian, CentOS, RHEL, Fedora, Arch, openSUSE)
- 📦 One-line installation script for easy deployment
- 🛡️ Security-first design with no password storage
- 🔄 Clean disconnect with proper network settings restoration
- 📝 Comprehensive activity logging
- 🧪 Connection testing before establishing tunnel
- 💾 Configuration saving (server settings only, no passwords)
- 🚦 Real-time connection status indicators
- 📚 Professional documentation and troubleshooting guide

### Security
- Encrypted SSH tunneling for all network traffic
- No plaintext password storage
- Proper cleanup of iptables rules on exit
- Secure SOCKS proxy implementation
- Input validation for all user-provided data

### Technical Features
- Python 3.6+ compatibility
- tkinter-based GUI (no external GUI dependencies)
- paramiko library for SSH operations
- Cross-platform package manager support
- Automatic privilege escalation handling
- Threading for non-blocking GUI operations
- Comprehensive error handling and user feedback

### Documentation
- Professional README with installation badges
- MIT License
- Comprehensive troubleshooting guide
- Code documentation and comments
- Setup script for Python package distribution

### Supported Platforms
- Ubuntu/Debian (apt)
- CentOS/RHEL (yum)
- Fedora (dnf)
- Arch Linux (pacman)
- openSUSE (zypper)
- Other Linux distributions with standard package managers
