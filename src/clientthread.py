#!/usr/bin/env python

import hashlib
import loginexceptions
from players import Players

def clientThread(c, addr):
	c.send("<L>ogin to an existing character or <C>reate one: ")
	option = c.recv(1024)
	if(option.lower().strip() == "c"):
		player = createCharacter(c, addr)
	else:
		player = login(c, addr)

def createCharacter(c, addr):
	c.send("Display name: ")
	name = c.recv(1024)
	c.send("Race: ")
	race = c.recv(1024)
	c.send("Username: ")
	username = c.recv(1024)
	c.send("Password: ")
	password = c.recv(1024)
	password = hashlib.sha224(password).hexdigest()

	c.send("Creating player...\n")

	player = Players.create(username, password, name, race)
	Players.save()
	return player

def login(c, addr):
	c.send("Username: ")
        username = c.recv(1024).strip()
	c.send("Password: ")
        password = c.recv(1024).strip()
	password = hashlib.sha224(password).hexdigest()
	
	print addr, "username:", username, "password:", password
	
	try:
		player = Players.login(username, password)
		print addr, "Correct password"
		c.send("Correct password\n")
	
	except loginexceptions.IncorrectPassword as e:
		print addr, "Incorrect password:", e
		c.send("Incorrect password\n")
		return
	
	except loginexceptions.UnknownPlayer as e:
		print addr, "Unknown player:", e
		c.send("Could not find a player with that name\n")
                return

