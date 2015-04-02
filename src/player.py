#!/usr/bin/env python

from inventory import Inventory
import players

class Player:
	def __init__(self, name, race, inventory=Inventory()):
		self.name = name
		self.race = race
		self.inventory = inventory
		players.onlinePlayers.append(self)
	
	def destroy():
		players.onlinePlayers.remove(self)
