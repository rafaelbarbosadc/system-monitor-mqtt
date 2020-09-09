#!/bin/sh
grep 'cpu ' /proc/stat | awk '{usage=($2+$4)*100/($2+$4+$5)} {print "CPU Usage: " usage "%"}'
free -m | awk 'NR==2{printf "Memory Usage: %s/%skB (%.2f%%)\n", $3,$2,$3*100/$2 }'
df -m | awk '$NF=="/"{printf "Disk Usage: %d/%dMB (%s)\n", $3,$2,$5}'

