#!/usr/bin/env python

class Inventory:
	def __init__(self, size=10, money=0):
		self.items = [None] * size
		self.money = money

	def addItem(newItem):
		for i, item in enumerate(self.items):
			if(item == None):
				self.items[i] = newItem
				return
	
	def removeItem(anItem):
		self.items.remove(anItem)
	
	def addMoney(amount):
		self.money += amount
	
	def removeMoney(amount):
		self.money += amount
