#!/usr/bin/python3.5
import random
import signal
import sys

def newBoard(n, p):
	c = 0
	board = [0] * n
	for i in range(n):
		board[c] = random.randint(0, p)
		c = c + 1
	return(board)

def display(board, n):
	c = 0
	l = 0
	while (l != 3):
		if (l == 0):
			for i in range(n):
				print(board[c], '| ', end = '', sep = ' ')
				c = c + 1
			print('\n', end = '', sep = '')
		if (l == 1):
			for i in range(n):
				print("----", end = '', sep = '')
			print('\n', end = '', sep = '')
		if (l == 2):
			c = 1
			for i in range(n):
				print(c, '| ', end = '', sep = ' ')
				c = c + 1
			print('\n', end = '', sep = '')
		l = l + 1

def possibleSquare(board, n, i):
	if (i.isdigit() == False):
		return (False)
	i = int(i) - 1
	if (i > n or i < 0 or board[i] == 0 or i == 0):
		return (False)
	else:
		return (True)

def selectSquare(board, n):
	err = 1
	while (err == 1):
		try:
			i = input("Choose a square : ")
			if (possibleSquare(board, n, i) == True):
				err = 0
		except KeyboardInterrupt:
			print('\n')
			exit()
	i = int(i)
	return (i - 1)

def possibleDestination(board, n, i, j):
	if (j.isdigit() == False):
		return (False)
	j = int(j) - 1
	if (j > n or j > i or j < 0):
		return (False)
	else:
		return (True)

def selectDestination(board, n, i):
	err = 1
	while (err == 1):
		try:
			j = input("Choose a destination : ")
			if (possibleDestination(board, n, i, j) == True):
				err = 0
		except KeyboardInterrupt:
			print('\n')
			exit()	
	j = int(j)
	return (j - 1)

def move(board, n , i, j):
	board[i] = board[i] - 1
	board[j] = board[j] + 1
	return (board)

def lose(board, n):
	i = 1
	d = 0
	while (i != n):
		if (board[0] > 0 and board[i] == 0):
			d = d + 1
		i = i + 1
	if (d == n - 1):
		return (True)
	else:
		return (False)

def nimble(n, p):
	board = newBoard(n, p)
	p = 1

	while (lose(board, n) == False):
		display(board, n)
		print("\n", "Player ", p, sep = '')
		i = selectSquare(board, n)
		j = selectDestination(board, n, i)
		print('\n')
		board = move(board, n, i, j)
		if (lose(board, n) == True):
			print("Winner :\n", p)
		if (p == 2):
			p = 1
		else:
			p = p + 1

nimble(10, 2)