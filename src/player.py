#!/usr/bin/env python

from inventory import Inventory

class Player:
	def __init__(self, username, password, name, race, inventory=Inventory()):
		self.username = username
		self.password = password
		self.name = name
		self.race = race
		self.inventory = inventory
