from getmac import get_mac_address
from termcolor import colored
import subprocess
import random


prefixes = [
    '00:60:17:',
    '00:60:18:',
    '00:60:19:',
    '00:60:1A:',
    '00:60:1B:',
    '00:60:1C:',
    '00:60:1D:',
    '00:60:1E:',
    '00:60:1F:',
    '00:60:20:',
    '00:60:21:',
    '00:60:22:',
    '00:60:23:',
    '00:60:24:',
    '00:60:25:',
    '00:60:26:',
]
digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
new_mac_address = []
identification_number = []
random_number = ''

for i in range(3):
    for y in range(2):
        random_number = str((digits[random.randint(0, (len(digits) - 1))]))
        identification_number.append(random_number)
    new_mac_address.append(''.join(identification_number))
    identification_number.clear()

formatted_new_mac_address = ':'.join(new_mac_address)
random.shuffle(prefixes)
formatted_prefix = prefixes[random.randint(0, (len(prefixes) - 1))]
formatted_new_mac_address = str(formatted_prefix) + formatted_new_mac_address

subprocess.run('ifconfig')
internet_interface = input('Which inferace address should be changed ? ')
old_mac_address = get_mac_address(interface=internet_interface)
subprocess.call(["sudo", "ifconfig", str(internet_interface), "down"])
subprocess.call(
    ["sudo", "ifconfig", str(internet_interface), "hw", "ether", str(formatted_new_mac_address)]
)
subprocess.call(["sudo", "ifconfig", str(internet_interface), "up"])
subprocess.call(["ifconfig", str(internet_interface)])
set_new_mac_address = get_mac_address(interface=internet_interface) 
if str(old_mac_address)!=str(set_new_mac_address):
        print (colored(f'Successfully changed MAC address for {internet_interface} interface !','green'))
else:
    print(colored(f'MAC address for {internet_interface} interface was not changed !!!','red'))
