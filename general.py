__author__ = 'ube'
def mkcmd(lingo, s):
    sum = 0;
    s = chr(len(s) + 1) + chr(lingo) + s
    for ch in s:
        sum = sum + ord(ch)
    sum = 0x100 - (sum & 0xff)
    return chr(0xff) + chr(0x55) + s + chr(sum)

def toHex(s):
    lst = []
    for ch in s:
        hv = hex(ord(ch)).replace('0x', '')
        if len(hv) == 1:
            hv = '0'+hv
        lst.append(hv)
    return reduce(lambda x,y:x+y, lst)

def printhex(s):
    return ":".join("{:02x}".format(ord(c)) for c in s)
