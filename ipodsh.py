#!/usr/bin/env python

import general
import serial
import time
import simpledock
from general import toHex

def printhelp():
    print "Commands:"
    print "play         pause           help"
    print "volup (vu)   voldown (vd)    exit"
    print "np           pp              na"
    print "pa"

playlist = 0
cmds = {'play': simpledock.play_only(),
        'pause': simpledock.pause_only(),
        'volup': simpledock.volume_up(),
        'voldown': simpledock.volume_down(),
        'skip+': simpledock.skip_forward(),
        'skip-': simpledock.skip_backwards(),
        'shuffle': simpledock.toggle_shuffle(),
        'mute': simpledock.toggle_mute(),
        'repeat': simpledock.toggle_repeat(),
        'select': simpledock.select_button(),
        'menu': simpledock.menu_button(),
        'up': simpledock.scroll_up(),
        'down': simpledock.scroll_down(),
        'vu': simpledock.volume_up(),
        'vd': simpledock.volume_down(),
        'p': simpledock.play(),
        'np': simpledock.next_playlist(),
        'pp': simpledock.previous_playlist(),
        'na': simpledock.next_album(),
        'pa': simpledock.previous_album(),
        'off': simpledock.off(),
        'on': simpledock.on(),
        'sf': simpledock.skip_forward(),
        'sb': simpledock.skip_backwards(),
        'bo': simpledock.release_button(),
        'exit': ""}

cmd = ""
debug = False
ser = serial.Serial('/dev/tty.usbserial-A700e70Q', baudrate=19200, timeout=10)
while (cmd != "exit"):
    cmd = raw_input(">> ").lower()
    if cmd in cmds.keys() and cmds[cmd]:
        s = cmds[cmd]
        bytes = ser.write(s)
        if ( debug ):
          print "Wrote %d bytes: %s" % (bytes, general.printhex(s)) 
    elif (cmd != "exit"):
        if ( cmd == "debug" ):
            debug = not debug
            print ("Debug:  "),
            print debug 
        else:
            printhelp()
