import re

import sys

def morse(text):
    encrypt = {'A':'.-','B':'-...','C':'-.-.','D':'-..','E':'.'
                ,'F':'..-','G':'--.','H':'....','I':'..','J':'.---'
                ,'K':'-.-','L':'.-..','M':'--','N':'-.','O':'---',
                'P':'.--.','Q':'--.-','R':'.-.','S':'...','T':'-','U':'..-',
                'V':'...-','W':'.--','X':'-..-','Y':'-.--','Z':'--..',' ':'.....'
                }
    decrypt = { value : key for key , value in encrypt.items()}

    if re.match(r'(\s|-|\.)+',text):
        return ''.join(decrypt[i] for i in text.split())

    return ' '.join(encrypt[i] for i in text.upper())

if __name__ == "__main__":
     print(morse(sys.argv[1]))