import subprocess
import random 

prefixes = ['00:60:17:','00:60:18:','00:60:19:','00:60:1A:','00:60:1B:','00:60:1C:','00:60:1D:','00:60:1E:','00:60:1F:','00:60:20:','00:60:21:','00:60:22:','00:60:23:','00:60:24:','00:60:25:','00:60:26w:']
digits = [0,1,2,3,4,5,6,7,8,9]
new_mac_address=[]
small_mac=[]
w=''

for i in range(3):
    for y in range(2):
        w = str((digits[random.randint(0,(len(digits)-1))]))
        small_mac.append(w)
    new_mac_address.append(''.join(small_mac))
    small_mac.clear()

s = ':'.join(new_mac_address)
random.shuffle(prefixes)
d = prefixes[random.randint(0,(len(prefixes)-1))]
s = str(d)+s

subprocess.run('ifconfig')
internet_interface = input('Which inferace address should be changed ? ')
subprocess.call(["sudo","ifconfig",str(internet_interface),"down"])
subprocess.call(["sudo","ifconfig",str(internet_interface),"hw","ether",str(s)])
subprocess.call(["sudo","ifconfig",str(internet_interface),"up"])
subprocess.call(["ifconfig",str(internet_interface)]) 
