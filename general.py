__author__ = 'ube'
def mkcmd(lingo, s):
    sum = 0;
    s = chr(len(s) + 1) + chr(lingo) + s
    for ch in s:
        sum = sum + ord(ch)
    sum = 0x100 - (sum & 0xff)
    return chr(0xff) + chr(0x55) + s + chr(sum)

def toHex(s):
    return s.encode("hex")

def printhex(s):
    return ":".join("{:02x}".format(ord(c)) for c in s)
