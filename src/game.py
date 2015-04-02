#!/usr/bin/env python

from area import Area
from players import Players

def joinGame(c, player):
	c.send(mainArea.display(Players.onlinePlayers))
