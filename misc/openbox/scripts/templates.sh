#!/bin/bash
#bad medicine to open templates, just like gnome!

function generate_template_menu {

ls ~/Templates | while read; do

    echo '<item label="'"${REPLY}"'">'
    echo -n '<action name="Execute"><execute>'
    echo -n "gnome-open '~/Templates/${REPLY}'"
    echo '</execute></action>'
    echo '</item>'
  done

}

echo '<openbox_pipe_menu>'

generate_template_menu

echo '</openbox_pipe_menu>'
