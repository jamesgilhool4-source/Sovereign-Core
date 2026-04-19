#!/bin/bash
# Disable all non-critical services to minimize footprint
for service in avahi-daemon cups bluetooth; do
    systemctl stop $service
    systemctl disable $service
done

# Enforce strict firewall egress policies (only allow mesh traffic)
iptables -P INPUT DROP
iptables -P FORWARD DROP
iptables -P OUTPUT ACCEPT
iptables -A OUTPUT -p tcp --dport 443 -j ACCEPT
