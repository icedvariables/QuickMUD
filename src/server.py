#!/usr/bin/env python

import socket, sys, thread, hashlib
import clientthread, players, loginexceptions

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
		self.players = players.Players()
		self.players.loadPlayersFromFile()

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

			c.send("Username: ")
			username = c.recv(1024)
			
			c.send("Password: ")
			password = c.recv(1024)
			password = hashlib.sha224(password)
			
			print addr, "username:", username, "password:", password
			
			try:
				player = self.players.login(username, password)
				thread.start_new_thread(clientthread.clientThread, (c, addr, player))
			
			except loginexceptions.IncorrectPassword as e:
				print addr, "Incorrect password:", e
				c.send("Incorrect password")
				return

			except loginexceptions.UnknownPlayer as e:
				print addr, "Unknown player:", e
				c.send("Could not find a player with that name")
				return


if __name__=="__main__":
	s = Server()
	s.loop()
