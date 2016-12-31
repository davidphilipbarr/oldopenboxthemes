#!/bin/sh

ICONFIED_STR="IsUnMapped"
RAISE="wmctrl -i -a"

echo '<openbox_pipe_menu>'

DESKTOP=$(wmctrl -d | grep -v '-' | sed 's/^(w*) .*$/1/')

for win in $(wmctrl -l  | grep " $DESKTOP " | sed 's/^(w*) .*$/1/')
do
    # check if the window is unmapped
    if [ $(xwininfo -id $win | grep "IsUnMapped" | wc -l) -gt 0 ]
    then
        title=$(xwininfo -id $win | grep "Window id" | sed 's/^.*"(.*)".*$/1/')
        
        echo -n "<item label="${title:0:40}"><action name="Execute"><execute>"
        echo -n "$RAISE $win"
        echo '</execute></action></item>'
    fi
done
