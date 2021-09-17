#! usr/bin/env python
import subprocess
import optparse



# Take command line arguments
def get_args():
    # Create an optparse object called parser
    parser = optparse.OptionParser()
    # Use the add_option method to add the interface option for users to choose a network interface
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change MAC address")
    # Use the add_option method to add the mac option for users to choose a new mac address
    parser.add_option("-m", "--mac", dest="mac_address", help="New MAC Address")
    # return the above values
    (options, arguments) = parser.parse_args()
    if not options.interface:
        # Handle error
        parser.error("[-] Please specify an interface, use --help for more information")
    elif not options.mac_address:
        # Handle error
        parser.error("[-] Please specify a Mac Address, use --help for more information")

    return options


# Change Mac Address of network interface
# Uses the subprocess module to make linux system calls
def change_mac(interface, mac_address):
    subprocess.call(["echo", f"[+] Attempting to change MAC Address for interface {interface} to {mac_address}"])
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", mac_address])
    subprocess.call(["ifconfig", interface, "up"])


# Run functions to change mac address
get_options = get_args()
change_mac(get_options.interface, get_options.mac_address)







