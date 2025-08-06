# 💼 Use Cases & Examples

Real-world examples of how to use SSH Tunnel Client for different scenarios.

---

## 🏠 Home Users

### Scenario 1: Secure Public WiFi Usage

**Situation**: You're at a coffee shop and want to secure your internet connection.

**Setup**:
```bash
# Install SSH Tunnel Client
curl -sSL https://raw.githubusercontent.com/reza-ygb/ssh-tunnel-client/main/one_line_installer.sh | bash

# Launch application
./run.sh
```

**Configuration**:
- **Server**: Your home server or VPS (e.g., `home.example.com`)
- **Port**: `22`
- **Username**: `myuser`
- **Password**: `mysecurepassword`

**Benefits**:
- ✅ All traffic encrypted
- ✅ Hide browsing from coffee shop network
- ✅ Access home network resources
- ✅ Bypass local network restrictions

---

### Scenario 2: Accessing Geo-restricted Content

**Situation**: You want to access content available in your home country while traveling.

**Setup**:
Use a server in your home country:

**Configuration**:
- **Server**: VPS in home country (e.g., `us-server.example.com`)
- **Port**: `22`
- **Username**: `traveler`

**Benefits**:
- ✅ Appear to browse from home country
- ✅ Access region-locked services
- ✅ Maintain privacy while abroad

---

## 🏢 Business Users

### Scenario 3: Remote Work Security

**Situation**: Working from home and need secure access to company resources.

**Company Server Setup**:
```bash
# On company server
sudo adduser remote_worker
sudo usermod -aG sudo remote_worker

# Configure SSH
echo "Port 2222" >> /etc/ssh/sshd_config
echo "AllowUsers remote_worker" >> /etc/ssh/sshd_config
sudo systemctl restart ssh
```

**Client Configuration**:
- **Server**: `company-vpn.example.com`
- **Port**: `2222`
- **Username**: `remote_worker`
- **Password**: Company-provided secure password

**Benefits**:
- ✅ Secure connection to office network
- ✅ Access internal company services
- ✅ Encrypted communication
- ✅ Audit trail of connections

---

### Scenario 4: Development Team Collaboration

**Situation**: Development team needs secure access to staging servers.

**Team Server Setup**:
```bash
# Create development users
for user in alice bob charlie; do
    sudo adduser $user
    sudo usermod -aG developers $user
done

# Configure group permissions
sudo groupadd developers
echo "%developers ALL=(ALL) NOPASSWD: /usr/bin/docker" >> /etc/sudoers
```

**Developer Configuration**:
- **Server**: `dev-tunnel.company.com`
- **Port**: `22`
- **Username**: Individual developer username
- **Benefits**: Shared development environment access

---

## 🎓 Educational Use

### Scenario 5: University Network Bypass

**Situation**: Student needs to bypass university network restrictions for research.

**Personal Server Setup**:
```bash
# Set up on personal VPS
sudo apt update && sudo apt upgrade -y
sudo apt install openssh-server

# Secure SSH configuration
sudo sed -i 's/#Port 22/Port 2222/' /etc/ssh/sshd_config
sudo sed -i 's/PermitRootLogin yes/PermitRootLogin no/' /etc/ssh/sshd_config
sudo systemctl restart ssh
```

**Student Configuration**:
- **Server**: Personal VPS IP address
- **Port**: `2222`
- **Username**: `student`

**Benefits**:
- ✅ Bypass university firewall
- ✅ Access blocked research resources
- ✅ Secure academic communications

---

## 🌍 Travel & Mobility

### Scenario 6: Digital Nomad Setup

**Situation**: Digital nomad working from different countries with varying internet restrictions.

**Multi-Server Configuration**:

Create config file `~/.ssh_tunnel_config.json`:
```json
{
  "servers": [
    {
      "name": "US East",
      "host": "us-east.myservers.com",
      "port": 22,
      "username": "nomad"
    },
    {
      "name": "EU West",
      "host": "eu-west.myservers.com", 
      "port": 22,
      "username": "nomad"
    },
    {
      "name": "Asia Pacific",
      "host": "ap-southeast.myservers.com",
      "port": 22,
      "username": "nomad"
    }
  ]
}
```

**Usage Strategy**:
- Use geographically closest server for best performance
- Switch servers based on content needs
- Maintain consistent online presence

---

## 🔒 Privacy & Security Focus

### Scenario 7: Journalist/Activist Security

**Situation**: Journalist in restrictive country needs secure communication.

**High-Security Setup**:

**Server Configuration** (hosted outside restrictive country):
```bash
# Use non-standard port
sudo sed -i 's/Port 22/Port 443/' /etc/ssh/sshd_config

# Disable password auth, use keys only
sudo sed -i 's/#PasswordAuthentication yes/PasswordAuthentication no/' /etc/ssh/sshd_config
sudo sed -i 's/#PubkeyAuthentication yes/PubkeyAuthentication yes/' /etc/ssh/sshd_config

# Install fail2ban for protection
sudo apt install fail2ban
```

**Client Configuration**:
- **Server**: Disguised as HTTPS traffic (port 443)
- **Authentication**: SSH keys instead of passwords
- **Additional**: Use Tor browser through tunnel for extra anonymity

---

## 💻 Technical Scenarios

### Scenario 8: Network Administrator Testing

**Situation**: Network admin testing network security and monitoring tools.

**Test Lab Setup**:
```bash
# Set up multiple test servers
for i in {1..3}; do
    docker run -d --name ssh-test-$i \
        -p $((2220+i)):22 \
        -e SSH_ENABLE_PASSWORD_AUTH=true \
        linuxserver/openssh-server
done
```

**Testing Configuration**:
Test different scenarios:
- Different ports (2221, 2222, 2223)
- Various authentication methods
- Network performance under load
- Security monitoring effectiveness

---

### Scenario 9: IoT Device Management

**Situation**: Managing IoT devices on remote networks securely.

**IoT Gateway Setup**:
```bash
# On Raspberry Pi or similar IoT gateway
sudo apt install openssh-server autossh

# Set up persistent reverse tunnel
autossh -M 20000 -N -R 2222:localhost:22 user@management-server.com
```

**Management Configuration**:
- **Server**: IoT gateway with reverse tunnel
- **Port**: `2222` (forwarded)
- **Purpose**: Secure IoT device configuration and monitoring

---

## 🎮 Gaming & Entertainment

### Scenario 10: Gaming with Friends

**Situation**: Playing region-locked games or reducing latency to specific game servers.

**Gaming Server Setup**:
Choose VPS near game servers:
```bash
# For US East Coast games
# Use server in Virginia/New York

# For EU games  
# Use server in Frankfurt/London

# For Asian games
# Use server in Singapore/Tokyo
```

**Gamer Configuration**:
- **Server**: VPS near game servers
- **Port**: `22`
- **Benefits**: Reduced latency, access to region-locked games

---

## 📊 Performance Optimization Examples

### Example 1: High-Bandwidth Usage

**For streaming/downloading**:
```bash
# Use compression for better performance
export SSH_TUNNEL_COMPRESSION=yes

# Use faster cipher
export SSH_TUNNEL_CIPHER=chacha20-poly1305@openssh.com

# Increase buffer sizes
export SSH_TUNNEL_BUFFER_SIZE=65536
```

### Example 2: Low-Latency Gaming

**For real-time applications**:
```bash
# Disable compression
export SSH_TUNNEL_COMPRESSION=no

# Use fastest cipher
export SSH_TUNNEL_CIPHER=aes128-ctr

# Optimize TCP settings
echo 'net.core.rmem_max = 16777216' | sudo tee -a /etc/sysctl.conf
```

### Example 3: Battery-Optimized Mobile

**For laptops/mobile devices**:
```bash
# Reduce keep-alive frequency
export SSH_TUNNEL_KEEPALIVE=300

# Use lower encryption for battery life
export SSH_TUNNEL_CIPHER=aes128-ctr

# Enable connection sharing
export SSH_TUNNEL_MULTIPLEX=yes
```

---

## 🔧 Automation Examples

### Automated Connection Script

```bash
#!/bin/bash
# auto-tunnel.sh - Automatic tunnel establishment

# Configuration
SERVERS=(
    "primary.example.com:22:user1"
    "backup.example.com:22:user2"
    "emergency.example.com:2222:user3"
)

# Try servers in order
for server_info in "${SERVERS[@]}"; do
    IFS=':' read -r host port user <<< "$server_info"
    
    echo "Trying $host:$port with user $user..."
    
    # Test SSH connection
    if ssh -o ConnectTimeout=5 -o BatchMode=yes "$user@$host" -p "$port" exit 2>/dev/null; then
        echo "Success! Using $host:$port"
        
        # Start SSH Tunnel Client with this server
        export SSH_TUNNEL_HOST="$host"
        export SSH_TUNNEL_PORT="$port"
        export SSH_TUNNEL_USER="$user"
        
        sudo python3 ssh_tunnel_client.py --auto-connect
        break
    else
        echo "Failed to connect to $host:$port"
    fi
done
```

### Cron Job for Auto-Reconnect

```bash
# Add to crontab (crontab -e)
# Check tunnel every 5 minutes and reconnect if down
*/5 * * * * /home/user/check-tunnel.sh

# check-tunnel.sh
#!/bin/bash
if ! pgrep -f "ssh_tunnel_client.py" > /dev/null; then
    echo "Tunnel down, reconnecting..."
    cd ~/ssh-tunnel-client
    ./run.sh &
fi
```

---

## 📋 Troubleshooting by Use Case

### Home User Issues

**Problem**: "Can't access home devices"
**Solution**: 
```bash
# Add route to home network
sudo ip route add 192.168.1.0/24 via 192.168.1.1 dev eth0
```

### Business User Issues

**Problem**: "Company firewall blocks SSH"
**Solution**: Use SSH on port 443 (HTTPS port)
```bash
# On server
sudo sed -i 's/Port 22/Port 443/' /etc/ssh/sshd_config
```

### Travel Issues

**Problem**: "Different countries have different restrictions"
**Solution**: Use multiple servers and switch as needed

---

## 🎯 Best Practices by Scenario

### For Maximum Security
1. Use SSH keys instead of passwords
2. Use non-standard SSH ports
3. Enable server-side fail2ban
4. Monitor connection logs
5. Use strong encryption

### For Best Performance
1. Choose geographically close servers
2. Use servers with good bandwidth
3. Optimize SSH settings for your use case
4. Monitor and tune performance

### For Reliability
1. Have backup servers configured
2. Use auto-reconnect scripts
3. Monitor connection health
4. Have fallback plans

---

**Choose the scenario that best matches your needs and adapt the configuration accordingly!** 🚀
