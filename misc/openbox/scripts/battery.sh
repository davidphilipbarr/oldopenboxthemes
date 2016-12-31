Battery=$(acpi -b | grep "Battery" | sed "s/Battery 1: discharging,//" | sed "s/,*remaining//" )

Thermal=$(acpi -t | grep "Thermal")

echo "<openbox_pipe_menu>"

echo "<item label=\"$Battery\"/>"
echo "<item label=\"$Thermal\"/>"
echo "</openbox_pipe_menu>"


