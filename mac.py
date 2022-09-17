#!/usr/bin/env python3
# chmod a+x name.py
#import sys

import sys
#print (sys.argv)

def cikl(mac):
#    print('func_CIKL: ',mac, 'TYPE: ', type(mac))
    R = mac.split(' ')
#    print('Rsplit_CIKL:', R, 'TYPE: ', type(R))
    for cn in range((len(R))):
        x = R[cn]
        #w = x[0:2]+x[3:5]+x[5] + x[6:8]+x[9:11] + x[11] + x [12:14] + x[15:17]
        w = x[0:2]+x[3:5]+ '.' + x[6:8]+x[9:11] + '.' + x [12:14] + x[15:17]
        print (w.upper(), '\t', w.lower())


def macdebug(sep, mac):
#    print ('macdebuc mac:', mac, 'TYPE: ', type(mac))
    """
    For python 2.X only!
    Repairs MAC-Address-like strings:
    strips unwanted separated characters
    and paires hexadecimal digits separated by sep.

    Examples of argument passing:
    macdebug('-', '''
    ce@5a#e6$7d%a3*c4
    0827.35BC.7FA6
    D3:EE:52:0B:6F:07
    ''')
    >>> macdebug('-', 'ce@5a#e6$7d%a3*c4 0827.35BC.7FA6 D3:EE:52:0B:6F:07')

    :param mac:
        MAC-Address-like string of arbitrary length, with each MAC-Addres
        separated by " ", "\n", "\t".
    :param sep:
       Required separated string character.
    :return:
        prints 'CE-5A-E6-7D-A3-C4'    'ce-5a-e6-7d-a3-c4'.
    """
    from string import hexdigits
    for item in mac.split():
        hex_only = [char for char in item if char in hexdigits]
        mac1 = "".join((x + y + sep for (x, y) in zip(hex_only[::2], hex_only[1::2]))).rstrip(sep).upper()
        mac2 = mac1.swapcase()
        print (mac1, '\t', mac2)

if len(sys.argv) > 1:
    sep = str(sys.argv[1])
    mac = sys.argv[2:]
#    print ('mac_sys: ', type(mac), mac)
    mac = " ".join (mac)
#    print ('mac_join', type(mac), mac)
    if sep =='!':
        cikl(mac)
    else:
        macdebug(sep, mac)
else:
    mac = str(input('mac: ')) 
    sep = str(input('sep: '))
    if sep == '!':
#        print ('mac_sepr INPUT:', mac, 'TYPE: ', type (mac))
        cikl(mac)
    else:
        macdebug(sep, mac)



