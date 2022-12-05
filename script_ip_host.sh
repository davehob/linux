echo "What ip would you like to set for this host?:"
read ipinput

sudo cat > /etc/netplan/00-installer-config.yaml << EOF
# This is the network config written by 'subiquity'
network:
  ethernets:
    ens3:
      addresses:
      - $ipinput/24
      routes:
        - to: default
          via: 192.168.1.1
      nameservers:
        addresses:
        - 8.8.8.8
        - 8.8.4.4
        - 192.168.1.1
        search: []
  version: 2
EOF

sudo netplan apply

echo "What hostname would you like to set for this machine?:"
read hostinput


sudo cat > /etc/hosts << EOF
127.0.0.1 localhost
127.0.1.1 $hostinput

# The following lines are desirable for IPv6 capable hosts
::1     ip6-localhost ip6-loopback
fe00::0 ip6-localnet
ff00::0 ip6-mcastprefix
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters
EOF

sudo cat > /etc/hostname << EOF
$hostinput
EOF

echo "Ip and hostname changed"

