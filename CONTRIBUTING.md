# Contributing to SSH Tunnel Client

Thank you for your interest in contributing to SSH Tunnel Client! We welcome contributions from everyone.

## 🚀 Quick Start

1. **Fork the repository**
2. **Clone your fork**
   ```bash
   git clone https://github.com/reza-ygb/ssh-tunnel-client.git
   cd ssh-tunnel-client
   ```
3. **Create a branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```
4. **Make your changes**
5. **Test your changes**
6. **Commit and push**
   ```bash
   git commit -m "Add your feature description"
   git push origin feature/your-feature-name
   ```
7. **Create a Pull Request**

## 🛠️ Development Setup

### Prerequisites
- Linux system (Ubuntu/Debian recommended for development)
- Python 3.6+
- sudo privileges
- Git

### Setup Development Environment
```bash
# Clone the repository
git clone https://github.com/reza-ygb/ssh-tunnel-client.git
cd ssh-tunnel-client

# Test the application
sudo python3 ssh_tunnel_client.py
```

## 📝 Code Guidelines

### Python Code Style
- Follow PEP 8 style guidelines
- Use descriptive variable and function names
- Add docstrings to functions and classes
- Keep functions focused and small
- Use type hints where appropriate

### Security Guidelines
- Never store passwords in plain text
- Validate all user inputs
- Use secure SSH practices
- Implement proper error handling
- Log security-relevant events

### Example Code Structure
```python
def connect_ssh(hostname: str, port: int, username: str, password: str) -> bool:
    """
    Establish SSH connection with proper error handling.
    
    Args:
        hostname: SSH server hostname or IP
        port: SSH server port
        username: SSH username
        password: SSH password
        
    Returns:
        bool: True if connection successful, False otherwise
    """
    try:
        # Implementation here
        pass
    except Exception as e:
        logger.error(f"SSH connection failed: {e}")
        return False
```

## 🧪 Testing

### Manual Testing
1. Test on multiple Linux distributions
2. Test connection to different SSH servers
3. Test GUI functionality
4. Test error handling
5. Verify cleanup on disconnect

### Automated Testing
```bash
# Syntax check
python -m py_compile ssh_tunnel_client.py

# Style check
flake8 ssh_tunnel_client.py

# Security check
bandit ssh_tunnel_client.py
```

## 🐛 Bug Reports

When reporting bugs, please include:
- Linux distribution and version
- Python version
- SSH Tunnel Client version
- Steps to reproduce
- Expected vs actual behavior
- Log output
- Screenshots if applicable

## 💡 Feature Requests

When suggesting features:
- Describe the use case
- Explain the problem it solves
- Consider security implications
- Think about cross-platform compatibility

## 📚 Documentation

- Update README.md for new features
- Add comments to complex code
- Update CHANGELOG.md
- Include examples in docstrings

## 🏷️ Commit Guidelines

Use clear, descriptive commit messages:
```
feat: add connection timeout configuration
fix: resolve iptables cleanup issue
docs: update installation instructions
refactor: improve error handling in SSH module
test: add unit tests for tunnel manager
```

## 🎯 Areas for Contribution

### High Priority
- [ ] Unit test suite
- [ ] SSH key authentication support
- [ ] Connection profiles management
- [ ] Multi-tunnel support
- [ ] Performance optimizations

### Medium Priority
- [ ] Dark theme for GUI
- [ ] System tray integration
- [ ] Bandwidth monitoring
- [ ] Connection statistics
- [ ] Export/import configurations

### Low Priority
- [ ] Plugin system
- [ ] Custom DNS servers
- [ ] Protocol selection (IPv4/IPv6)
- [ ] Advanced logging options

## 🔍 Code Review Process

1. All changes must be submitted via Pull Request
2. Code must pass automated checks
3. At least one maintainer review required
4. Testing on multiple distributions preferred
5. Documentation updates must accompany feature changes

## 📞 Getting Help

- 📧 Email: [maintainer-email]
- 💬 Discussions: [GitHub Discussions](https://github.com/reza-ygb/ssh-tunnel-client/discussions)
- 🐛 Issues: [GitHub Issues](https://github.com/reza-ygb/ssh-tunnel-client/issues)

## 📄 License

By contributing to SSH Tunnel Client, you agree that your contributions will be licensed under the MIT License.

---

Thank you for contributing to SSH Tunnel Client! 🙏
