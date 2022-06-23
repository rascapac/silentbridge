import os

def reset_link(iface):
    os.system('ifconfig %s -multicast' % iface) 
    os.system('ethtool -r %s' % iface)

