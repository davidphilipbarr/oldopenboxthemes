#!/bin/bash

echo '<openbox_pipe_menu>'
#yeah for real?
filemanager="thunar"

for bookmark in `sed 's/[ ][^ ]*$//' .gtk-bookmarks
` ; do
  echo '<item label="'`basename ${bookmark}`'">'
  echo '<action name="Execute"><execute>'
  echo "$filemanager ${bookmark}"
  echo '</execute></action>'
  echo '</item>'
done

echo '</openbox_pipe_menu>'
