<!-- Use this file to provide workspace-specific custom instructions to Copilot. For more details, visit https://code.visualstudio.com/docs/copilot/copilot-customization#_use-a-githubcopilotinstructionsmd-file -->

# SSH Tunnel Client - Copilot Instructions

## Project Overview
This is a professional SSH tunneling application with GUI interface for Linux systems. The project provides secure traffic routing through SSH connections with an intuitive Persian/English interface.

## Code Style and Standards
- **Language**: Python 3.6+
- **GUI Framework**: tkinter (built-in, no external dependencies)
- **SSH Library**: paramiko (auto-installed)
- **Code Style**: Clean, readable, well-documented
- **Error Handling**: Comprehensive try-catch blocks
- **Logging**: Detailed activity logging
- **Security**: No password storage, encrypted connections only

## Key Features to Maintain
- **Auto-dependency installation**: Automatically install required packages
- **Cross-platform compatibility**: Support all major Linux distributions
- **Bilingual interface**: Persian and English support
- **One-file solution**: Keep everything in single executable file
- **Security-first**: No credentials storage, clean disconnect
- **User-friendly**: Simple GUI with clear status indicators

## Development Guidelines
- Always use absolute imports for clarity
- Include error handling for network operations
- Maintain backward compatibility with older Python versions
- Use threading for non-blocking GUI operations
- Follow Linux networking best practices
- Ensure clean system state restoration on disconnect

## Testing Considerations
- Test on multiple Linux distributions
- Verify proper cleanup on unexpected disconnections
- Validate SSH connection parameters before connecting
- Test GUI responsiveness during operations
- Ensure proper privilege escalation handling

## Security Requirements
- Never store passwords in plain text
- Use secure SSH key exchange
- Validate all user inputs
- Implement proper network isolation
- Clean up iptables rules on exit
- Log security-relevant events

When generating code for this project, prioritize security, reliability, and user experience. Always include proper error handling and user feedback mechanisms.
