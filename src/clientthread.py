#!/usr/bin/env python

import re
import players
from player import Player

re_coordinates = re.compile(r"^\(?(\d+)\w*,\w*(\d+)\)?$")

def clientThread(c, addr):
	player = createCharacter(c, addr)
	
	c.send(str(len(players.onlinePlayers))+" player(s) currently online...\n")
	
	loop(c, addr, player)
	
def loop(c, addr, player):
	command = ""
	while(command != "quit"):
		c.send("\n" * 20) # Crude way of clearing the screen
		c.send(player.currentArea.display(players.onlinePlayers))
		
		c.send("> ")
		command = c.recv(1024).strip()
		print "Recieved command from:", addr

		parseCommand(command, c, addr, player)

def parseCommand(command, c, addr, player):
	# Set player position
	match = re_coordinates.match(command)
	if(match):
		x = int(match.group(1))
		y = int(match.group(2))
		player.setPosition(x, y)

		c.send("Setting your position to x: "+str(x)+" y: "+str(y))
	
	else:
		c.send("Unknown command. Type 'help' for a list of commands.")

def createCharacter(c, addr):
	c.send("Name: ")
	name = c.recv(1024).strip()
	c.send("Race: ")
	race = c.recv(1024).strip()

	c.send("Creating player...\n")

	player = Player(name, race)
	return player
