import os
import time

# Script is used to protect against a slowloris DDoS attack.
# Originally created for use with FXServer.
# Edit connectionTotal to control the number of total connections before a ban.
# Edit refreshRate to control time before script re-executes.
# Script will automatically ban those IPs using UFW Interface and reload the firewall rules
# Stores blocked IP's in a text document named blockedIPs.txt.

connectionTotal = 15
refreshRate = 3

blockedips = []
connums = []
ips = []

while True:
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
    
