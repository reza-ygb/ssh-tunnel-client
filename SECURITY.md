# Security Policy

## 🔒 Supported Versions

We actively support the following versions of SSH Tunnel Client:

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | :white_check_mark: |
| < 1.0   | :x:                |

## 🛡️ Security Features

SSH Tunnel Client is designed with security as a primary concern:

### ✅ Security Measures Implemented
- **Encrypted SSH tunneling** - All traffic is encrypted using SSH protocol
- **No password storage** - Credentials are never saved to disk
- **Input validation** - All user inputs are validated and sanitized
- **Proper cleanup** - Network settings are properly restored on disconnect
- **Secure SOCKS proxy** - Local proxy server with proper isolation
- **Privilege management** - Minimal required privileges, proper escalation handling
- **Activity logging** - Comprehensive logging for security monitoring

### 🔍 Security Best Practices
- Always run with minimum required privileges
- Use strong SSH server configurations
- Keep SSH servers updated
- Monitor connection logs regularly
- Use complex passwords or SSH keys
- Ensure proper firewall configurations

## 🚨 Reporting a Vulnerability

We take security vulnerabilities seriously. If you discover a security issue, please follow these steps:

### 📧 Private Disclosure
**DO NOT** create a public GitHub issue for security vulnerabilities.

Instead, please email us directly at:
- **Primary**: security@ssh-tunnel-client.com
- **Secondary**: [maintainer-email]

### 📝 Report Format
Please include the following information:

```
Subject: [SECURITY] Brief description of vulnerability

1. Description:
   - What is the vulnerability?
   - How can it be exploited?

2. Impact:
   - What systems are affected?
   - What could an attacker achieve?

3. Reproduction:
   - Step-by-step instructions
   - Required conditions
   - Test environment details

4. Suggested Fix:
   - If you have ideas for fixing

5. Contact Information:
   - Your preferred contact method
   - PGP key if available
```

### ⏱️ Response Timeline
- **24 hours**: Initial acknowledgment
- **72 hours**: Preliminary assessment
- **7 days**: Detailed analysis and fix timeline
- **30 days**: Fix implementation and testing
- **Release**: Security update published

### 🏆 Recognition
We believe in recognizing security researchers who help improve our security:

- **Hall of Fame**: Public recognition (with permission)
- **Priority Support**: Fast-track support for your issues
- **Early Access**: Beta access to new features
- **Credits**: Acknowledgment in release notes

## 🛡️ Security Auditing

### External Audits
We welcome external security audits and penetration testing:

- Please coordinate with us before starting
- Provide advance notice for any disruptive testing
- Share findings through our private disclosure process

### Tools Used
Our security testing includes:
- **bandit** - Python security linter
- **safety** - Dependency vulnerability checker
- **flake8** - Code quality and security patterns
- Manual code review for security patterns

## 🔐 Cryptographic Details

### SSH Implementation
- Uses `paramiko` library for SSH operations
- Supports SSH-2 protocol only
- Implements proper key exchange and authentication
- Uses industry-standard encryption algorithms

### Supported Algorithms
- **Key Exchange**: diffie-hellman-group14-sha256, ecdh-sha2-nistp256
- **Host Key**: rsa-sha2-256, rsa-sha2-512, ecdsa-sha2-nistp256
- **Encryption**: aes128-ctr, aes192-ctr, aes256-ctr
- **MAC**: hmac-sha2-256, hmac-sha2-512

## 🚫 Out of Scope

The following are considered out of scope for security reports:
- Issues requiring physical access to the machine
- Social engineering attacks
- Issues in third-party dependencies (please report to upstream)
- DoS attacks against SSH servers
- Issues requiring root access on the target system

## 📚 Security Resources

### Documentation
- [SSH Security Best Practices](https://www.ssh.com/academy/ssh/security)
- [Python Security Guidelines](https://python-security.readthedocs.io/)
- [Linux Network Security](https://www.kernel.org/doc/html/latest/networking/index.html)

### Dependencies
- [paramiko Security](https://docs.paramiko.org/en/stable/security.html)
- [Python Security Advisories](https://github.com/pypa/advisory-database)

## 📞 Contact

For security-related questions that are not vulnerabilities:
- 📧 Email: security@ssh-tunnel-client.com
- 💬 Discussions: Security category in GitHub Discussions
- 🐛 Issues: Use "security" label for non-sensitive security improvements

---

**Remember**: Security is everyone's responsibility. Help us keep SSH Tunnel Client secure! 🛡️
