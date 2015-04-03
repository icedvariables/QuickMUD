#!/usr/bin/env python

import players
from player import Player

def clientThread(c, addr):
	player = createCharacter(c, addr)
	
	c.send(str(len(players.onlinePlayers))+" player(s) currently online...\n")

	c.send(player.currentArea.display(players.onlinePlayers))

def createCharacter(c, addr):
	c.send("Name: ")
	name = c.recv(1024).strip()
	c.send("Race: ").strip()
	race = c.recv(1024)

	c.send("Creating player...\n")

	player = Player(name, race)
	return player
