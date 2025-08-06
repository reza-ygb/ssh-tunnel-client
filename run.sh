#!/bin/bash

# SSH Tunnel Client Launcher
# راه‌انداز کلاینت تونل SSH

clear
echo "=========================================="
echo "🔒 SSH Tunnel Client"
echo "کلاینت تونل SSH"
echo "=========================================="

# Check if running on Linux
if [[ "$OSTYPE" != "linux-gnu"* ]]; then
    echo "❌ This application only works on Linux"
    exit 1
fi

# Check if main script exists
if [[ ! -f "ssh_tunnel_client.py" ]] && [[ ! -f "ssh_vpn_client_v2.py" ]] && [[ ! -f "ssh_vpn_client.py" ]]; then
    echo "❌ Main script not found!"
    echo "Please run this from the project directory"
    exit 1
fi

# Choose the best available script
SCRIPT=""
if [[ -f "ssh_tunnel_client.py" ]]; then
    SCRIPT="ssh_tunnel_client.py"
elif [[ -f "ssh_vpn_client_v2.py" ]]; then
    SCRIPT="ssh_vpn_client_v2.py"
elif [[ -f "ssh_vpn_client.py" ]]; then
    SCRIPT="ssh_vpn_client.py"
fi

# Check if running as root
if [[ $EUID -eq 0 ]]; then
    echo "🚀 Starting SSH Tunnel Client..."
    python3 $SCRIPT
else
    echo "🔐 Root privileges required for network configuration"
    echo "Starting with sudo..."
    echo ""
    sudo python3 $SCRIPT
fi
