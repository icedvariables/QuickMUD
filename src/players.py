#!/usr/bin/env python

import cPickle as pickle, loginexceptions
from player import Player

class Players:
	players = []
	
	@staticmethod
	def loadPlayersFromFile(filename="players.p"):
		with open(filename, "rb") as f:
			playersInFile = pickle.load(f)
			print playersInFile
			Players.players = Players.players + playersInFile
	
	@staticmethod
	def save(filename="players.p"):
		with open(filename, "wb") as f:
			pickle.dump(Players.players, f)

	@staticmethod
	def login(username, password):
		for player in Players.players:
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

	@staticmethod
	def create(username, password, name, race):
		player = Player(username, password, name, race)
		Players.players.append(player)
		return player

