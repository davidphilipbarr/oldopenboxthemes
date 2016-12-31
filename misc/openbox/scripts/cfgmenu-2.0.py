#!/usr/bin/env python

import os
import string
import sys
from os.path import isdir

# ------------------------- Openbox Settings Menu --------------------- #
# Author: Pwnz3r - http://pstudios.ath.cx				#
# License: GNU GPL							#
#									#
# ------------------------------ Directions --------------------------- #
#									#
# Put this script into ~/.config/openbox/scripts/			#
# Insert:								#
# <menu id="config" execute="~/.config/openbox/scripts/cfgmenu.py -m" />#
# into menu.xml								#
# --------------------------------------------------------------------- 

# Directory and filename settings					#
home = os.getenv('HOME')			# No need to change
scriptdir = home + "/.config/openbox/scripts/"	# Where the script is located
scriptname = "cfgmenu-2.0.py"			# Name of the script
cfgmenu = scriptdir + scriptname		# Putting it all together
rcfile = home + "/.config/openbox/rc.xml"	# The rc.xml file's location
rcFile = file(rcfile, "r")
bool = ["yes", "no"]

def mkItem(label, option, value):
	print "  <item label=\"" + label + "\">\n\
		    <action name=\"Execute\"><execute>" + cfgmenu + " -c " + option + " \"" + value + "\"</execute></action>\n\
		    <action name=\"Reconfigure\" />\n\
		    <action name=\"Reconfigure\" />\n\
		    <action name=\"Reconfigure\" />\n\
		  </item>"

def mkMenu(id, name):
	print "<menu id=\"" + id + "\" label=\"" + name + "\">"

# Button Menu
def buttonLayoutMenu():
	mkMenu("buttons", "Button Layout")
	layouts = ["Mac Style", "Windows Style"]
	for o in layouts:
		mkItem(o, "buttons", o)
	print "</menu>"

# Theme menu
def themeMenu(int):
	directories = [home + "/.themes", "/usr/share/themes"]
	menuNames = ["User Themes", "System Themes"]
	dirlist = os.listdir(directories[int])
	mkMenu(menuNames[int], menuNames[int])
	for t in dirlist:
		# Setup fpath as the overall directory
		fpath = directories[int] + "/" + t
		# If it is a directory, look for openbox-3 inside and add the options
		if isdir(fpath) and ".thumbnails" not in fpath:
			listing = os.listdir(fpath)
			if "openbox-3" in listing:
				mkItem(t, "theme", t)
	print "</menu>"

# Dock options
def dockMenu():
	options = ["position", "stacking", "direction", "autohide"]
	mkMenu("docko", "Dock")
	for o in options:
		if o == "position":
			options = ["TopLeft", "Top", "TopRight", "Left", "Right", "Bottom", "BottomLeft", "BottomRight", "Floating"]
			mkMenu("dpos", "Position")
			for po in options:
				mkItem(po, o, po)
			print "</menu>"

		elif o == "stacking":
			options = ["Top", "Normal", "Bottom"]
			mkMenu("dlayer", "Layer")
			for po in options:
				mkItem(po, o, po)
			print "</menu>"

		elif o == "direction":
			options = ["Vertical", "Horizontal"]
			mkMenu("dorient", "Direction")
			for po in options:
				mkItem(po, o, po)
			print "</menu>"
			
		else:
			mkMenu(o, o)
			for po in bool:
				mkItem(po, o, po)
			print "</menu>"
	print "</menu>"

# Focus options
def focusMenu():
	options = ["focusNew", "followMouse", "focusLast", "raiseOnFocus"]
	for op in options:
		mkMenu(op, op)
		for o in bool:
			mkItem(o, op, o)
		print "</menu>"

# Window placement options
def placementMenu():
	mkMenu("placement", "Window Placement")
	placementOptions = ["Smart", "UnderMouse"]
	for o in placementOptions:
		mkItem(o, "policy", o)
	print "</menu>"

# Window resize options
def resizeMenu():
	mkMenu("resizing", "Resize method")
	mkItem("Draw Contents", "resize", "yes")
	mkItem("Don't Draw Contents", "resize", "no")
	print "</menu>"

def chLine():
	buffer = rcFile.readlines()
	rcFile.close()
	if sys.argv[1] == "-c":
		newLine = "  <" + sys.argv[2] + ">" + sys.argv[3] + "</" + sys.argv[2] + ">\n"
	for line in range(0, len(buffer)):
		# Window placement configuration
		if "<policy>" in buffer[line] and sys.argv[2] == "policy":
			buffer[line] = newLine
		# Focus configuration
		elif "<focusNew>" in buffer[line] and sys.argv[2] == "focusNew":
			buffer[line] = newLine
		elif "<followMouse>" in buffer[line] and sys.argv[2] == "followMouse":
			buffer[line] = newLine
		elif "<focusLast>" in buffer[line] and sys.argv[2] == "focusLast":
			buffer[line] = newLine
		elif "<raiseOnFocus>" in buffer[line] and sys.argv[2] == "raiseOnFocus":
			buffer[line] = newLine
		# Dock configuration
		elif "<position>" in buffer[line] and sys.argv[2] == "position":
			buffer[line] = newLine
		elif "<stacking>" in buffer[line] and sys.argv[2] == "stacking":
			buffer[line] = newLine
		elif "<direction>" in buffer[line] and sys.argv[2] == "direction":
			buffer[line] = newLine
		elif "<autohide>" in buffer[line] and sys.argv[2] == "autohide":
			buffer[line] = newLine
		# Window resizig technique
		elif "<drawContents>" in buffer[line] and sys.argv[2] == "resize":
			buffer[line] = "<drawContents>" + sys.argv[3] + "</drawContents>\n"
		# Change the theme
		elif "<theme>" in buffer[line] and sys.argv[2] == "theme":
			buffer[line + 1] = "<name>" + sys.argv[3] + "</name>\n"
		# Button layout
		elif "<titlelayout>" in buffer[line] and sys.argv[2] == "buttons":
			if sys.argv[3] == "Mac Style":
				buffer[line] =   "  <titlelayout>CIMLN</titlelayout>\n"
			if sys.argv[3] == "Windows Style":
				buffer[line] =   "  <titlelayout>NLIMC</titlelayout>\n"
	
	newRC = file(rcfile, "w")
	newRC.writelines(buffer)
	newRC.close()

def main():
	# Change stuff
	if sys.argv[1] == "-c":
		chLine()

	# Make menu
	elif sys.argv[1] == "-m":
		# Start menu
		print "<openbox_pipe_menu>"

		# Theme Menu
		themeMenu(0)
		themeMenu(1)

		print "<separator />"

		# Button layout menu
		buttonLayoutMenu()

		# Focus Menu
		mkMenu("focus", "Focus Options")
		focusMenu()
		print "</menu>"

		# Window placement menu
		placementMenu()

		# Resize method menu
		resizeMenu()

		# Dock options menu
		dockMenu()
				
		# End menu
		print "</openbox_pipe_menu>"

if __name__ == "__main__":
	main()
