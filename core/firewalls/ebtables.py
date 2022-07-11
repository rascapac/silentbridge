import os

def source_nat(upstream, bridge_iface, switch_mac, client_mac, phy):
    #os.system('ebtables -t nat -A POSTROUTING -s %s -o %s -j snat --to-src %s' % (switch_mac, upstream, client_mac))
    os.system('ebtables -t nat -A POSTROUTING -s %s -o %s -j snat --to-src %s' % (switch_mac, upstream, client_mac))
    os.system('ebtables -t nat -A POSTROUTING -s %s -o %s -j snat --to-src %s' % (switch_mac, bridge_iface, client_mac))
    #os.system('ebtables -t nat -A POSTROUTING -s %s -o %s -j snat --to-src %s' % (switch_mac, bridge_iface, client_mac))
    #os.system('ebtables -t nat -A POSTROUTING -s %s -o %s -j snat --to-src %s' % (client_mac, upstream, switch_mac))
    #os.system('ebtables -t nat -A POSTROUTING -s %s -o %s -j snat --to-src %s' % (client_mac, bridge_iface, switch_mac))

def flush():
    os.system('ebtables -F')
    os.system("ebtables -t nat -F")
    os.system("ebtables -A OUTPUT -p 0x0806 -j DROP")  # _really_ block arp e.g. for nmap
    os.system("ebtables -A OUTPUT -p 0x0808 -j DROP")  # _really_ block arp e.g. for nmap
    os.system("ebtables -A OUTPUT -p 0x8035 -j DROP")  # _really_ block arp e.g. for nmap
    os.system("ebtables -A OUTPUT -p 0x80F3 -j DROP")  # _really_ block arp e.g. for nmap

def default_accept():
    os.system('ebtables -P INPUT ACCEPT')
    os.system('ebtables -P OUTPUT ACCEPT')
    os.system('ebtables -P FORWARD ACCEPT')
