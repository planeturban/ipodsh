__author__ = 'ube'

from general import mkcmd

def release_button():
    return mkcmd(2, chr(0x0) + chr(0x0))

def play():
    return mkcmd(2, chr(0x0) + chr(0x1))

def volume_up():
    return mkcmd(2, chr(0x0) + chr(0x2))

def volume_down():
    return mkcmd(2, chr(0x0) + chr(0x4))

def skip_forward():
    return mkcmd(2, chr(0x0) + chr(0x8))

def skip_backwards():
    return mkcmd(2, chr(0x0) + chr(0x10))

def next_album():
    return mkcmd(2, chr(0x0) + chr(0x20))

def previous_album():
    return mkcmd(2, chr(0x0) + chr(0x40))

def stop():
    return mkcmd(2, chr(0x0) + chr(0x80))

def play_only():
    return mkcmd(2, chr(0x0) + chr(0x0) + chr(0x1))

def pause_only():
    return mkcmd(2, chr(0x0) + chr(0x0) + chr(0x2))

def toggle_mute():
    return mkcmd(2, chr(0x0) + chr(0x0) + chr(0x4))

def next_playlist():
    return mkcmd(2, chr(0x0) + chr(0x0) + chr(0x20))

def previous_playlist():
    return mkcmd(2, chr(0x0) + chr(0x0) + chr(0x40))

def toggle_shuffle():
    return mkcmd(2, chr(0x0) + chr(0x0) + chr(0x80))

def toggle_repeat():
    return mkcmd(2, chr(0x0) + chr(0x0) + chr(0x0) + chr(0x1))

def off():
    return mkcmd(2, chr(0x0) + chr(0x0) + chr(0x0) + chr(0x4))

def on():
    return mkcmd(2, chr(0x0) + chr(0x0) + chr(0x0) + chr(0x8))

def menu_button():
    return mkcmd(2, chr(0x0) + chr(0x0) + chr(0x0) + chr(0x40))

def select_button():
    return mkcmd(2, chr(0x0) + chr(0x0) + chr(0x0) + chr(0x80))

def scroll_up():
    return mkcmd(2, chr(0x0) + chr(0x0) + chr(0x0) + chr(0x0) + chr(0x1))

def scroll_down():
    return mkcmd(2, chr(0x0) + chr(0x0) + chr(0x0) + chr(0x0) + chr(0x2))

