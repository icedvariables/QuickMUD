#!/usr/bin/env python

from inventory import Inventory
import players, area

startingArea = area.Area("areas/main.area.json")

class Player:
	def __init__(self, name, race, inventory=Inventory()):
		self.name = name
		self.race = race
		self.inventory = inventory

		self.x = 0
		self.y = 0
		self.currentArea = startingArea

		players.onlinePlayers.append(self)
	
	def setPosition(self, x, y):
		self.x = x
		self.y = y
	
	def getPosition(self):
		return (self.x, self.y)

	def destroy(self):
		players.onlinePlayers.remove(self)
