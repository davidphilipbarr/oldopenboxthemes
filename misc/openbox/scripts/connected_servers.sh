
echo '<openbox_pipe_menu>'

  for host in `gconftool --all-dirs /desktop/gnome/connected_servers` ; do
    echo '<item label="'`gconftool -g ${host}/display_name`'">'
    echo '<action name="Execute"><execute>'
    echo "nautilus `gconftool -g ${host}/uri`"
    echo '</execute></action>'
    echo '</item>'
  done

echo '</openbox_pipe_menu>'
