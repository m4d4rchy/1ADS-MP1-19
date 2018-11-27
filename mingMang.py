#!/usr/bin/python3.5

def newBoard(n):
	board = [[0] * n for i in range(n)]
	
	pawnPlayer1(board, n, 1)
	pawnPlayer2(board, n, 2)
	return (board)

def pawnPlayer1(board, n, s):
	r = 0
	c = 0
	for i in range (n):
		board[r][0] = s
		r = r + 1
	r = r - 1
	for i in range (n - 1):
		board[r][c] = s
		c = c + 1
	return (board)

def pawnPlayer2(board, n, s):
	r = 0
	c = 1
	for i in range (n - 1):
		board[r][c] = s
		c = c + 1
	c = c - 1
	for i in range (n):
		board[r][c] = s
		r = r + 1
	return (board)

def selectPawn(board, n, player):
	pawn = [0] * 2
	err = 1
	while (err == 1):
		row = input("Select a pawn, row : ")
		column = input("Select a pawn, column : ")
		if (possiblePawn(board, n, player, row, column) == True):
			err = 0
		pawn[0] = int(row) - 1
		pawn[1] = int(column) - 1
	return (pawn)

def selectDestination(board, n, i, j):
	destination = [0] * 2
	err = 1
	while (err == 1):
		row = input("Select a destination, row : ")
		column = input("Select a destination, column : ")
		if (possibleDestination(board, n, i, j, row, column) == True):
			err = 0
		destination[0] = int(row) - 1
		destination[1] = int(column) - 1

def display(board, n):
	c = 0
	l = 0
	while (c != n):
		if (board[c][l] == 1):
			print('x', end='')
		if (board[c][l] == 2):
			print('o', end='')
		if (board[c][l] == 0):
			print('.', end='')
		print(' ',end='')
		l = l + 1
		if (l == n):
			print('\n', end='')
			l = 0
			c = c + 1
	print('\n', end='')

def possiblePawn(board, n , player, i, j):
	if (i.isdigit() == False or j.isdigit() == False):
		return (False)
	i = int(i) - 1
	j = int(j) - 1
	if (i == 0 and board[i][j + 1] == 0):
		return (True)
	elif ((i == n - 1) and board[i][j - 1] == 0):
		return (True)
	elif ((board[i][j] == 1 or board[i][j] == 2) and
	(board[i][j + 1] == 0 or board[i][j - 1] == 0)):
		return (True)
	else:
		return (False)

def possibleDestination(board, n , i, j, k, l):
	if (k.isdigit() == False or l.isdigit() == False):
		return (False)
	k = int(k) - 1
	l = int(k) - 1
	c = j + 1
	p = i + 1
	if (i == k):
		while (c != l):
			if (board[i][c] == 1 or board[i][c] == 2):
				return (False)
			c = c + 1
	elif (j == l):
		while (p != k):
			if (board[p][j] == 1 or [board[p][j]] == 2):
				return (False)
			p = p + 1
	else:
		return (True)

def mingMang(n):
	player = 1
	board = newBoard(n)
	display(board, n)
	print("Player", player, ':')
	pawn = selectPawn(board, n, player)
	destination = selectDestination(board, n, pawn[0], pawn[1])

mingMang(9)