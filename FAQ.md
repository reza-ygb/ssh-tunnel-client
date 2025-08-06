# ❓ Frequently Asked Questions (FAQ)

Common questions and detailed answers about SSH Tunnel Client.

---

## 🚀 Getting Started

### Q: What is SSH Tunnel Client?
**A:** SSH Tunnel Client is a professional application that routes all your internet traffic through an encrypted SSH connection. It provides a user-friendly GUI interface for creating secure tunnels to SSH servers, effectively giving you a private and secure internet connection.

### Q: How is this different from a traditional VPN?
**A:** Unlike traditional VPN services:
- ✅ **You control the server** - Use your own SSH server
- ✅ **No monthly fees** - Just server hosting costs
- ✅ **No logging** - Complete privacy
- ✅ **Universal compatibility** - Works with any SSH server
- ✅ **Open source** - Fully transparent and auditable

### Q: Is it really free?
**A:** Yes! SSH Tunnel Client is completely free and open source. You only need:
- A computer running Linux
- An SSH server (can be a $5/month VPS)
- This application (free download)

---

## 🔧 Installation & Setup

### Q: Which Linux distributions are supported?
**A:** SSH Tunnel Client works on ALL major Linux distributions:

| Family | Distributions | Package Manager |
|--------|---------------|-----------------|
| **Debian** | Ubuntu, Debian, Mint, Elementary | apt |
| **Red Hat** | CentOS, RHEL, Fedora, Rocky Linux | yum/dnf |
| **Arch** | Arch Linux, Manjaro, EndeavourOS | pacman |
| **SUSE** | openSUSE Leap/Tumbleweed | zypper |
| **Others** | Alpine, Void Linux, etc. | Various |

### Q: Can I install it without root access?
**A:** You need root access to:
- Modify network routing (essential for tunneling)
- Install system dependencies
- Configure iptables rules

However, you can download and run the Python script directly if dependencies are already installed.

### Q: Does it work on Windows or macOS?
**A:** Currently, SSH Tunnel Client is designed specifically for Linux systems. The networking components use Linux-specific tools like `iptables` and `ip route`. 

For Windows/macOS users, consider:
- Running Linux in a virtual machine
- Using WSL2 on Windows
- Using traditional SSH port forwarding

### Q: What if I don't have an SSH server?
**A:** You'll need access to an SSH server. Options include:

1. **VPS Providers** ($3-10/month):
   - DigitalOcean, Linode, Vultr
   - AWS Lightsail, Google Cloud
   - Hetzner, OVH, etc.

2. **Free SSH Providers** (limited):
   - Some free tier cloud providers
   - Educational institutions
   - Free shell providers (limited bandwidth)

3. **Self-hosted**:
   - Home server with port forwarding
   - Raspberry Pi with dynamic DNS
   - Old computer as SSH server

---

## 🔒 Security & Privacy

### Q: How secure is SSH tunneling?
**A:** Very secure! SSH tunneling provides:
- **Military-grade encryption** (AES-256, ChaCha20)
- **Perfect Forward Secrecy** - each session uses unique keys
- **Authentication** - verifies server identity
- **Integrity checking** - detects tampering
- **Compression** - optional data compression

It's the same technology used by system administrators worldwide.

### Q: Are my passwords stored anywhere?
**A:** **No, never!** SSH Tunnel Client:
- ❌ Never saves passwords to disk
- ❌ Never sends passwords to third parties
- ❌ Never stores credentials in configuration files
- ✅ Only keeps passwords in memory during session
- ✅ Clears memory when disconnected

### Q: Can my ISP see my traffic?
**A:** When connected through SSH tunnel:
- **ISP sees**: Encrypted SSH traffic to your server
- **ISP cannot see**: Websites you visit, data you send/receive
- **Server sees**: Your actual internet traffic (just like your ISP normally would)

Choose your SSH server provider accordingly!

### Q: What about DNS leaks?
**A:** SSH Tunnel Client prevents DNS leaks by:
- Changing system DNS to secure servers (1.1.1.1, 8.8.8.8)
- Routing DNS queries through the tunnel
- Restoring original DNS on disconnect

### Q: Is this legal?
**A:** Using SSH tunnels is generally legal, but:
- ✅ **Legal in most countries** for privacy and security
- ⚠️ **Check local laws** in restrictive countries
- ⚠️ **Respect terms of service** of networks you use
- ⚠️ **Don't use for illegal activities**

*We don't provide legal advice - consult local laws.*

---

## 🖥️ Technical Questions

### Q: Why do I need sudo/root access?
**A:** Root access is required to:
```bash
# Modify network routing
sudo ip route add default via [tunnel_ip]

# Configure iptables rules  
sudo iptables -t nat -A OUTPUT -p tcp --dport 80 -j REDIRECT --to-port 1080

# Change DNS settings
echo "nameserver 1.1.1.1" | sudo tee /etc/resolv.conf
```

### Q: What ports does it use?
**A:** SSH Tunnel Client uses:
- **Local SOCKS port**: 1080 (configurable)
- **SSH port**: 22 or custom (connects to your server)
- **No inbound ports** - all connections are outbound

### Q: How much bandwidth does it use?
**A:** Overhead is minimal:
- **SSH encryption**: ~2-5% overhead
- **Compression**: Can reduce bandwidth by 10-30%
- **Keep-alive**: ~1KB every 60 seconds
- **Total overhead**: Usually <5% of your normal usage

### Q: Can I use it for gaming?
**A:** Yes, but with considerations:
- ✅ **Latency**: Adds server round-trip time
- ✅ **Stability**: Very stable connections
- ✅ **Performance**: Good for turn-based games
- ⚠️ **Real-time games**: May add 10-100ms latency

Choose a server close to game servers for best performance.

### Q: Does it work with streaming services?
**A:** Generally yes, but:
- ✅ **Technical compatibility**: Works with all services
- ⚠️ **Terms of service**: Some services prohibit proxy/tunnel use
- ⚠️ **Detection**: Advanced services may detect and block tunnels
- 💡 **Tip**: Use servers in the same country as the service

---

## 🚨 Troubleshooting

### Q: Installation fails - what should I do?
**A:** Try these steps in order:

1. **Update system**:
   ```bash
   sudo apt update && sudo apt upgrade  # Ubuntu/Debian
   sudo yum update                      # CentOS/RHEL
   ```

2. **Install manually**:
   ```bash
   # Install Python and dependencies
   sudo apt install python3 python3-pip python3-tkinter curl
   
   # Download application
   wget https://raw.githubusercontent.com/reza-ygb/ssh-tunnel-client/main/ssh_tunnel_client.py
   
   # Run directly
   sudo python3 ssh_tunnel_client.py
   ```

3. **Check Python version**:
   ```bash
   python3 --version  # Should be 3.6 or higher
   ```

### Q: GUI doesn't start - shows tkinter error?
**A:** Install GUI libraries:
```bash
# Ubuntu/Debian
sudo apt install python3-tkinter

# CentOS/RHEL
sudo yum install tkinter

# Fedora
sudo dnf install python3-tkinter

# Arch Linux
sudo pacman -S tk
```

### Q: SSH connection works manually but fails in the app?
**A:** Common causes:

1. **Different SSH settings**:
   ```bash
   # Test with same settings as app
   ssh -p 22 username@server_ip
   ```

2. **Firewall blocking connections**:
   ```bash
   # On server
   sudo ufw allow 22/tcp
   ```

3. **Server SSH configuration**:
   ```bash
   # Check SSH service
   sudo systemctl status ssh
   ```

### Q: Connected but no internet access?
**A:** Check these components:

1. **SOCKS proxy**:
   ```bash
   curl --socks5 127.0.0.1:1080 http://google.com
   ```

2. **DNS resolution**:
   ```bash
   nslookup google.com
   ```

3. **Routing table**:
   ```bash
   ip route show
   ```

4. **Reset network** (if stuck):
   ```bash
   sudo systemctl restart NetworkManager
   ```

### Q: Connection is very slow?
**A:** Optimization steps:

1. **Choose closer server** - geographical distance matters
2. **Check server bandwidth** - ensure adequate server specs
3. **Disable compression** for high-speed connections:
   ```bash
   export SSH_TUNNEL_COMPRESSION=no
   ```
4. **Use faster cipher**:
   ```bash
   export SSH_TUNNEL_CIPHER=aes128-ctr
   ```

### Q: Disconnection doesn't restore network?
**A:** Manual cleanup:

```bash
# Reset routing
sudo ip route flush table main
sudo dhclient -r && sudo dhclient

# Reset DNS
sudo systemctl restart systemd-resolved

# Reset NetworkManager
sudo systemctl restart NetworkManager

# Reboot if needed
sudo reboot
```

---

## 🌐 Use Cases

### Q: Can I access my home network while traveling?
**A:** Yes! Set up SSH server on your home network:

1. **Configure home router** - port forward SSH (port 22)
2. **Set up dynamic DNS** - use services like DuckDNS
3. **Connect remotely** - use your home IP/domain
4. **Access home devices** - they'll be accessible through tunnel

### Q: Will this work in restrictive countries?
**A:** SSH tunneling often works where VPNs are blocked because:
- SSH traffic looks like normal server administration
- Uses common ports (22, 443)
- Widely used for legitimate purposes

However:
- ⚠️ Always respect local laws
- ⚠️ Some countries actively block SSH
- 💡 Consider using port 443 (HTTPS port)

### Q: Can multiple people use the same SSH server?
**A:** Yes! Create multiple user accounts:

```bash
# On SSH server
sudo adduser user1
sudo adduser user2
sudo adduser user3

# Each user can connect independently
```

Benefits:
- Individual authentication
- Separate home directories
- Individual bandwidth monitoring
- User-specific restrictions

---

## 💰 Cost & Economics

### Q: What does it cost to run?
**A:** Typical monthly costs:

| Component | Cost Range | Notes |
|-----------|------------|-------|
| **VPS Server** | $3-20/month | Depends on specs and location |
| **Domain** (optional) | $10-15/year | For easy server access |
| **Bandwidth** | Usually included | Most VPS include 1TB+ |
| **SSH Tunnel Client** | **FREE** | Open source |

**Total**: ~$5-25/month vs $10-15/month for commercial VPN

### Q: Which VPS provider should I choose?
**A:** Popular options:

**Budget-friendly**:
- Vultr, DigitalOcean, Linode ($5-10/month)
- Good for personal use

**High-performance**:
- AWS, Google Cloud, Azure ($10-50/month)
- Enterprise features, global locations

**Privacy-focused**:
- Mullvad, IVPN (also offer SSH access)
- Anonymous payment options

**Selection criteria**:
- Geographic location (closer = faster)
- Bandwidth allowance
- Price point
- Privacy policy
- Technical support

---

## 🔮 Future & Development

### Q: What features are planned?
**A:** Roadmap includes:
- SSH key authentication support
- Multiple tunnel profiles
- GUI improvements and themes
- Mobile Linux support (PostmarketOS, etc.)
- Performance optimizations
- Plugin system

### Q: How can I contribute?
**A:** Ways to help:
- **Report bugs** - help us improve stability
- **Suggest features** - share your ideas
- **Translate interface** - add more languages
- **Write documentation** - help other users
- **Code contributions** - submit pull requests
- **Test on distributions** - ensure compatibility

### Q: Is commercial support available?
**A:** Currently:
- ✅ **Community support** - GitHub issues and discussions
- ✅ **Documentation** - comprehensive guides
- ✅ **Open source** - modify as needed

For enterprise needs, consider:
- Hiring developers for custom features
- Setting up internal support teams
- Contributing to development for priority features

---

## 📞 Still Have Questions?

### Community Support
- **GitHub Issues**: [Technical problems and bug reports](https://github.com/reza-ygb/ssh-tunnel-client/issues)
- **GitHub Discussions**: [General questions and community help](https://github.com/reza-ygb/ssh-tunnel-client/discussions)
- **Email**: support@ssh-tunnel-client.com

### Before Asking
Please include:
- Linux distribution and version
- Python version (`python3 --version`)
- Complete error messages
- Steps you've already tried
- Your use case/goal

### Documentation
- **Installation Guide**: [INSTALL.md](INSTALL.md)
- **Usage Guide**: [USAGE.md](USAGE.md)
- **Examples**: [EXAMPLES.md](EXAMPLES.md)
- **Contributing**: [CONTRIBUTING.md](CONTRIBUTING.md)
- **Security**: [SECURITY.md](SECURITY.md)

---

**Can't find your question? [Ask the community!](https://github.com/reza-ygb/ssh-tunnel-client/discussions)** 💬
