#!/usr/bin/env python

import cPickle as pickle, loginexceptions
from player import Player

class Players:
	def __init__(self):
		self.players = []
	
	def loadPlayersFromFile(self, filename="players.p"):
		with open(filename, "rb") as f:
			playersInFile = pickle.load(f)
			print playersInFile
			self.players = self.players + playersInFile
	
	def login(self, username, password):
		for player in self.players:
			if(username == player.name):
				print "Found player in database with same name as login"

				if(password == player.password):
					print "Passwords match. Logging in..."
					
					self.players.remove(player)
					return player
				else:
					print "Passwords do not match. Aborting"
					raise loginexceptions.IncorrectPassword(password+" and "+player.password+" do not match")

		return loginexceptions.UnknownPlayer("Player "+username+" does not exist")

	def create(self, username, password, name, race, filename="players.p"):
		with open(filename, "rb") as f:
			players = pickle.load(f)
		
		self.players.append(Player(username, password, name, race))
