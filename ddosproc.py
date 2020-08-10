import os
import subprocess
import time

# Script is used to protect against a slowloris DDoS attack.
# Originally created for use with FXServer.
# Stores blocked IP's in a text document named blockedIPs.txt.

# Edit connectionTotal below to control the number of total connections before a ban.
# Edit refreshRate below to control time before script re-executes.

connectionTotal = 15
refreshRate = 3


blockedips = []
connums = []
ips = []

while True:
    if os.geteuid() != 0:
        print("This script requires root privileges. Exiting.")
        break
    if os.path.isdir('/etc/ufw/'):
        ufws = subprocess.Popen(["ufw","status"], stdout=subprocess.PIPE)
        s = str(ufws.communicate())
        if 'inactive' in s:
            print('UFW Disabled. To enable, enter `sudo ufw enable` into your terminal.')
            break
    else:
        print('UFW not installed. To install, enter `sudo apt-get install ufw` into your terminal.')
        break            
    f = open('blockedIPs.txt','a')
    ns = os.popen("netstat -ntu|awk '{print $5}'|cut -d: -f1 -s|sort|uniq -c|sort -nk1 -r")
    ipl = ns.read()
    l = list(ipl.split())
    for x in range(len(l)):
        if x % 2 == 0:
            connums.append(l[x])
        else:
            ips.append(l[x])
    for x, y in enumerate(connums):
        if int(y) > connectionTotal:
            if ips[x] != '127.0.0.1' and ips[x] not in blockedips:
                print('Blocking %s with %d connections' % (ips[x], int(y)))
                os.system(str('ufw insert 2 deny from %s' % ips[x]))
                os.system(str('ufw reload'))
                blockedips.append(ips[x])
                f.write(ips[x] + '\n')   
    f.close()
    time.sleep(refreshRate)
