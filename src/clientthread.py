#!/usr/bin/env python

import players
from player import Player

def clientThread(c, addr):
	player = createCharacter(c, addr)
	
	c.send(str(len(players.onlinePlayers))+" player(s) currently online...\n")
	
	loop()
	
def loop():
	command = ""
	while(command != "quit"):
		c.send("\n" * 20) # Crude way of clearing the screen
		c.send(player.currentArea.display(players.onlinePlayers))
		command = c.recv(1024)

def createCharacter(c, addr):
	c.send("Name: ")
	name = c.recv(1024).strip()
	c.send("Race: ")
	race = c.recv(1024).strip()

	c.send("Creating player...\n")

	player = Player(name, race)
	return player
