#!/usr/bin/env python
#Autor: Nicolas Reynolds (nicolas.reynolds@gmail.com)
#Licencia: GPL 2.0

#Este script depende de py-libmpdclient
#http://musicpd.org/py-libmpdclient.shtml
#y está basado en ob-mpd-0.3.py
#http://david.chalkskeletons.com/scripts/ob-mpd-0.3.py


import mpdclient, os, sys

mpdPort = 6600

con = mpdclient.MpdController(port=mpdPort)
song = con.getCurrentSong()
ls = con.ls()

def add(dir):
	con.add(dir)

try:
	if (sys.argv[1] == "add") and sys.argv[2]:
		add(sys.argv[2])
except IndexError:
	pass

print "<?xml version='1.0' encoding='utf-8'?>"
print "<openbox_pipe_menu>"

for l in ls:
	print "		<item label='%s' >" % l
	print "			<action name='Execute'>"
#	print "				<execute>~/.config/openbox/scripts/mpd.py add \"%s\"</execute>" % l
	print "				<execute>/usr/bin/mpc add %s</execute>" % l
	print "			</action>"
	print "		</item>"
print "</openbox_pipe_menu>"

