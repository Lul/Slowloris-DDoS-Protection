# Slowloris-DDoS-Protection
This script was created to help combat the issue of a slowloris DDoS attack (created for use with FXServer in particular). 
This script should be used as a **last line of defense**, and should theoretically work any game server powered by **Ubuntu 20.04&**. 
This script utilizes Linux's **UFW** program. 
It's suggested that you use the shell command ***netstat -ntu|awk '{print $5}'|cut -d: -f1 -s|sort|uniq -c|sort -nk1 -r*** to determine how many connections a normal player uses, so you know what to set *connectionTotal* to within the script. 
It's suggested that you run this script utilizing the Linux command **screen**.
