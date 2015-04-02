#!/usr/bin/env python

from inventory import Inventory
import players, area

startingArea = area.Area("areas/main.area.json")

class Player:
	def __init__(self, name, race, inventory=Inventory()):
		self.name = name
		self.race = race
		self.inventory = inventory

		self.position = (0, 0)
		self.currentArea = startingArea

		players.onlinePlayers.append(self)
	
	def destroy():
		players.onlinePlayers.remove(self)
