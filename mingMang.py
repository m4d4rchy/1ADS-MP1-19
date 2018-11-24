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
	
	print("Player", player, ':')
	row = input("Select a pawn, row : ")
	column = input("Select a pawn, column : ")
	pawn[0] = row
	pawn[1] = column
	return (pawn)

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
	if (board[i][j] == 1 or board[i][j] == 2)
	while

def mingMang(n):
	player = 1
	board = newBoard(n)
	display(board, n)
	pawn = selectPawn(board, n, player)

mingMang(9)