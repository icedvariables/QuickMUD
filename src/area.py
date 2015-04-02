#!/usr/bin/env python

import json

class Area:
	def __init__(self, filename):
		with open(filename, "r") as f:
			self.area = json.load(f)
	
	def display(self, players):
		text = []
		for y in self.area:
			line = []
			for x in y:
				line.append(x.icon)
			text.append(line)
		
		for player in players:
			text[player.y][player.x] = "P"

		ret = ""
		for y in text:
			for x in y:
				ret += x
			ret += "\n"

		return ret
