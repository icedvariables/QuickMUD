#!/usr/bin/env python


def clientThread(c, addr, player):
	c.send("Welcome, "+player.name+"\n")
