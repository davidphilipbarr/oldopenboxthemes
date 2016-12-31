

User=$(whoami)
Host=$(uname -n)
System=$(uname -s)
Release=$(uname -r)
Arch=$(uname -m)

SizeHome=$(df -HlT | grep /dev/sda1)
#SizeRoot=$(df -HlT | grep /dev/sda1)

eth0ip=$(/sbin/ifconfig eth1 | grep "inet addr:" | sed "s/.*inet addr://" | sed "s/Bcast.*//")
eth0down=$(/sbin/ifconfig eth1 | grep bytes | sed 's/.*RX bytes:[0-9]* (//' | sed 's/b).*TX.*//' | sed 's/).*TX.*//')
eth0up=$(/sbin/ifconfig eth1 | grep bytes | sed 's/.*TX bytes:[0-9]* (//' | sed 's/b).*//' | sed 's/).*//')
Battery=$(acpi -b | grep "Battery" | sed "s/Battery 1: discharging,//" | sed "s/,*remaining//")
DateDate=$(date '+Date ~ %Y.%m.%d. (%a)')
DateWeek=$(date '+Week ~ %W')
DateDay=$(date '+ Day ~ %j')
DateTime=$(date '+Time ~ %H:%M [%Z]')
UpTime=$(uptime | sed 's/.*up //' | sed 's/[0-9]* us.*//' | sed 's/ day,/d/' | sed 's/ days,/d/' | sed 's/:/h /' | sed 's/ min//'|  sed 's/,/m/')

MemoryTotal=$(echo "scale = 2; "$(top -n 1 | grep Mem: | awk '{print $3}' sed 's/k//')" /1024" | bc)
#MemoryUsed=$(echo "scale = 2; "$(top -n 1 | grep Mem: | awk '{print $5}' | sed 's/k//')" /1024" | bc)
#MemoryFree=$(echo "scale = 2; "$(top -n 1 | grep Mem: | awk '{print $7}' | sed 's/k//')" /1024" | bc)
 MemoryUsed=$(echo "scale = 2; ("$(top -n 1 | grep Mem: | awk '{print $5}' | sed 's/k//')" /1024) - ("$(top -n 1 | grep Swap: | awk '{print $8}' | sed 's/k//')" /1024)" | bc)
 MemoryFree=$(echo "scale = 2; ("$(top -n 1 | grep Mem: | awk '{print $7}' | sed 's/k//')" /1024) + ("$(top -n 1 | grep Swap: | awk '{print $8}' | sed 's/k//')" /1024)" | bc)
SwapTotal=$( echo "scale = 2; "$(top -n 1 | grep Swap: | awk '{print $2}' | sed 's/k//')" /1024" | bc)
 SwapUsed=$( echo "scale = 2; "$(top -n 1 | grep Swap: | awk '{print $4}' | sed 's/k//')" /1024" | bc)
 SwapFree=$( echo "scale = 2; "$(top -n 1 | grep Swap: | awk '{print $6}' | sed 's/k//')" /1024" | bc)

MemUsedPercent=$(echo "scale = 2; (("$(cat /proc/meminfo | grep MemTotal: | awk '{print $2}' | sed 's/k//')" /1024) - (("$(cat /proc/meminfo | grep MemFree: | awk '{print $2}' | sed 's/k//')" /1024) + ("$(cat /proc/meminfo | grep -m 1 Cached: | awk '{print $2}' | sed 's/k//')" /1024))) / ("$(cat /proc/meminfo | grep MemTotal: | awk '{print $2}' | sed 's/k//')" /1024) *100" | bc)
SwpUsedPercent=$(echo "scale = 2; (("$(cat /proc/meminfo | grep SwapTotal: | awk '{print $2}' | sed 's/k//')" /1024) - ("$(cat /proc/meminfo | grep SwapFree: | awk '{print $2}' | sed 's/k//')" /1024)) / ("$(cat /proc/meminfo | grep SwapTotal: | awk '{print $2}' | sed 's/k//')" /1024) *100" | bc)

CPUmodel=$(cat /proc/cpuinfo | grep "model name" | sed 's/.*: //')
CPUfreq=$(cat /proc/cpuinfo | grep -m 1 "cpu MHz" | sed 's/.*: //')
CPUcache=$(cat /proc/cpuinfo | grep -m 1 "cache size" | sed 's/.*: //')
echo "<openbox_pipe_menu>"
#<!--
#echo "<separator label=\"$User @ $Host \"/>"
#-->

echo "<item label=\"$System $Release $Arch\"/>"
echo "<item label=\"$DateTime\"/>"
#echo "<action name=\"Execute\"><execute>xcalendar</execute></action>"
#echo "</item>"
echo "<separator />"
#echo "<separator label = \"Filesystem ~~ Type ~~ Total ~ Used ~ Free ~ % ~ Mount\"/>"
#echo "<item label=\"$SizeRoot\"/>"
echo "<item label=\"$SizeHome\"/>"

#echo "<separator label=\"CPU ~ RAM ~ Swap | Used/Total     \"/>"
echo "<item label=\"RAM used: $MemUsed MiB/$MemTotal MiB ~ $MemUsedPercent%\"/>"
echo "<item label=\"Swp used: $SwpUsed MiB/$SwpTotal MiB ~ $SwpUsedPercent%\"/>"
#echo "<item label=\"CPU: $CPUmodel\"/>"
#echo "<item label=\"CPU @ $CPUfreq MHz\"/>"
#echo "<item label=\"CPU Cache: $CPUcache\"/>"
#echo "<separator label = \"Network ~ eth1 \"/>"
echo "<separator />"
echo "<item label=\"IP Address: $eth0ip\"/>"
echo "<item label=\"Download: "$eth0down"iB\"/>"
echo "<item label=\"Upload: "$eth0up"iB\"/>"
echo "<separator />"
echo "<item label=\"Battery:$Battery\"/>"
#echo "<separator label = \"Date ~ Time\"/>"
#echo "<item label=\"$DateDate\"/>"
#echo "<item label=\"$DateWeek\"/>"
#echo "<item label=\"$DateDay\"/>"

#echo "<item label=\"  Up ~ $UpTime\"/>"

echo "</openbox_pipe_menu>"
