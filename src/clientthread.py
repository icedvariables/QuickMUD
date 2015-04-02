#!/usr/bin/env python

import hashlib
from players import Players

def clientThread(c, addr):
	c.send("<L>ogin to an existing character or <C>reate one: ")
	option = c.recv(1024)
	if(option.lower().strip() == "c"):
		createCharacter(c)

	c.send("Username: ")
        username = c.recv(1024).strip()
	c.send("Password: ")
        password = c.recv(1024).strip()
	password = hashlib.sha224(password)
	
	print addr, "username:", username, "password:", password
	
	try:
		player = Players.login(username, password)
		thread.start_new_thread(clientthread.clientThread, (c, addr, player))
	
	except loginexceptions.IncorrectPassword as e:
		print addr, "Incorrect password:", e
		c.send("Incorrect password")
		return
	
	except loginexceptions.UnknownPlayer as e:
		print addr, "Unknown player:", e
		c.send("Could not find a player with that name")
                return

def createCharacter(c):
	c.send("Display name: ")
	name = c.recv(1024)
	c.send("Race: ")
	race = c.recv(1024)
	c.send("Username: ")
	username = c.recv(1024)
	c.send("Password: ")
	password = c.recv(1024)
	password = hashlib.sha224(password)

	player = Players.create(username, password, name, race)
	Players.save()
	return player
