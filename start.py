import os
import time
import sys


r="\033[1;31m"
w="\033[1;37m"

if "linux" in sys.platform:
	print "Can't Reload This Page !".format(r)
	else:
		
def main():
	os.system("cls")
	time.sleep(2)
	print""" 
	 __      __       .__                                
/  \    /  \ ____ |  |   ____  ____   _____   ____   
\   \/\/   // __ \|  | _/ ___\/  _ \ /     \_/ __ \  
 \  v1.0   /\  ___/|  |_\  \__(  <_> )  Y Y  \  ___/  
  \__/\  /  \___  >____/\___  >____/|__|_|  /\___  > 
       \/       \/          \/            \/     \/  
       
      >> WINDOWS USER >>

""".format(r, w)
time.sleep(2)
os.system("cls")
print "[!] Starting webDav [!]".format(r)
time.sleep(3)
os.system("cls")
print "[1] WebDav".format(r,w)
print "[2] Exit".format(w, r)
select= input("root@hansputera~# ")
filtering(select)

def filtering(pilihan):
	if pilihan == 1:
		print """
		Usage : python2 webs.py nameweb.xyz scriptDeface.html
		""".format(w)
	elif pilihan == 2:
		print(r+"[!] Exited Program [!]"+w)
		os.sys.exit
	else:
		print(r+"[!] Exited Program [!]"+w)
		os.sys.exit








if __name__ == '__main__':
	
main()


