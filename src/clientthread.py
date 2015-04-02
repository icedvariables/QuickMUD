#!/usr/bin/env python

import players
from player import Player

def clientThread(c, addr):
	player = createCharacter(c, addr)
	
	c.send(str(len(players.onlinePlayers))+" player(s) currently online...")

def createCharacter(c, addr):
	c.send("Name: ")
	name = c.recv(1024)
	c.send("Race: ")
	race = c.recv(1024)

	c.send("Creating player...\n")

	player = Player(name, race)
	return player
