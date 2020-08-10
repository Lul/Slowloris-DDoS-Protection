# Slowloris-DDoS-Protection
This script was created to help combat the issue of a slowloris DDoS attack (created for use with FXServer in particular).\
This script should be used as a **last line of defense**, and should theoretically work any game server powered by **Ubuntu 20.04**.\
This script utilizes Linux's ***UFW*** program to block IPs.

# Usage
During normal operation, run the command `netstat -ntu|awk '{print $5}'|cut -d: -f1 -s|sort|uniq -c|sort -nk1 -r` to determine how many connections a normal player establishes.\
Edit *connectionTotal* to set the connection number threshold. Any IP that establishes more connections than this variable will be banned.\
It's suggested that you run this script utilizing the Linux command ***screen*** to maintain its persistence.
