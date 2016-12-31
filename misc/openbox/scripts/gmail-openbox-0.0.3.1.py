#!/usr/bin/python2.3
# Authors: cduquette@gmail.com follower@myrealbox.com
# License: GPL 2.0

# Usage:
# Put an entry in your ~/.config/openbox/menu.xml like this:
# <menu id="gmail" label="gmail" execute="~/.config/openbox/scripts/gmail-openbox.py" />
# And inside <menu id="root-menu" label="openbox">, add this somewhere (wherever you want it on your menu)
# <menu id="gmail" />

import os
import sys
import logging

name = "dpbarr"
pw = "spinoza"
browser = "epiphany"
filename = "/tmp/.gmail.cache"

login = "\'https://www.google.com/accounts/ServiceLoginBoxAuth?service=mail&amp;continue=https%3A%2F%2Fgmail.google.com%2Fgmail&amp;Email=" + name + "&amp;Passwd=" + pw + "\'"

# Allow us to run using installed `libgmail` or the one in parent directory.
try:
    import libgmail
except ImportError:
    # Urghhh...
    sys.path.insert(1,
                    os.path.realpath(os.path.join(os.path.dirname(__file__),
                                                  os.path.pardir)))

    import libgmail

    
if __name__ == "__main__":
    import sys
    from getpass import getpass

    if not os.path.isfile(filename):
        ga = libgmail.GmailAccount(name, pw)

        try:
            ga.login()
        except libgmail.GmailLoginFailure:
	    print "<?xml version=\"1.0\" encoding=\"UTF-8\"?>"
            print "<openbox_pipe_menu>"
	    print "  <item label=\"login failed.\">"
            print "    <action name=\"Execute\"><execute>" + browser + " " + login + "</execute></action>"
            print "  </item>"
	    print "</openbox_pipe_menu>"
	    raise SystemExit

    else:
        ga = libgmail.GmailAccount(
            state = libgmail.GmailSessionState(filename = filename))
    
    msgtotals = ga.getUnreadMsgCount()
    
    print "<?xml version=\"1.0\" encoding=\"UTF-8\"?>"
    print "<openbox_pipe_menu>"

    if msgtotals == 0:
	print "  <item label=\"no new messages.\">"
    elif msgtotals == 1:
        print "  <item label=\"1 new message.\">"
    else:
        print "  <item label=\"" + str(msgtotals) + " new messages.\">"
    print "    <action name=\"Execute\"><execute>" + browser + " " + login + "</execute></action>"
    print "  </item>"
    print "</openbox_pipe_menu>"

    state = libgmail.GmailSessionState(account = ga).save(filename)
