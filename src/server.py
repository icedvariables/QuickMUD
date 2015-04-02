#!/usr/bin/env python

import socket, sys, thread
import clientthread

HOST = ''
PORT = 5678
MOTD = "Main server"

WELCOME_MSG = """
   ___        _      _    __  __ _   _ ____  
  / _ \ _   _(_) ___| | _|  \/  | | | |  _ \ 
 | | | | | | | |/ __| |/ / |\/| | | | | | | |
 | |_| | |_| | | (__|   <| |  | | |_| | |_| |
  \__\_\\__,_|_|\___|_|\_\_|  |_|\___/|____/ 

"""

class Server:
	def __init__(self):
		self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self._initSocket()
	
	def _initSocket(self):
		try:
			self.s.bind((HOST, PORT))
		except socket.error as e:
			print "Failed to bind socket:", e
			sys.exit()
		
		print "Socket bound to port:", PORT

		self.s.listen(10)
		print "Listening for connections..."
	
	def loop(self):
		while(True):
			c, addr = self.s.accept()
			print "Connection:", addr
			
			c.send("QuickMUD: "+MOTD+"\n\n"+WELCOME_MSG)

			thread.start_new_thread(clientthread.clientThread, (c, addr))
			


if __name__=="__main__":
	s = Server()
	s.loop()
