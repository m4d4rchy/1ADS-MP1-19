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
	return (destination)

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
	if (board[i][j] == player and i == 0 and (board[i][j + 1] == 0 or board[i + 1][j] == 0)):
		return (True)
	elif (board[i][j] == player and (i == n - 1 or j == n - 1) and (board[i][j - 1] == 0 or board[i - 1][j] == 0)):
		return (True)
	elif (board[i][j] == player and (board[i][j + 1] == 0 or board[i][j - 1] == 0 or board[i + 1][j] == 0 or board[i- 1][j] == 0)):
		return (True)
	else:
		return (False)

def possibleDestination(board, n , i, j, k, l):
	if (k.isdigit() == False or l.isdigit() == False):
		return (False)
	k = int(k) - 1
	l = int(l) - 1
	c = j + 1
	p = i + 1
	if (i == k):
		if (l > j):
			while (c != l):
				if (board[i][c] == 1 or board[i][c] == 2):
					return (False)
				c = c + 1
		else:
			c = j - 1
			while (c != l):
				if (board[i][c] == 1 or board[i][c] == 2):
					return (False)
				c = c - 1

	elif (j == l):
		if (k > i):
			while (p != k):
				if (board[p][j] == 1 or [board[p][j]] == 2):
					return (False)
				p = p + 1
		else:
			p = i - 1
			while (p != k):
				if (board[p][j] == 1 or [board[p][j]] == 2):
					return (False)
				p = p - 1

	elif ((i != k and j != l) or (i == k and j == l)):
		return (False)
	return (True)

def move(board, n, player, i, j, k, l):
	board[i][j] = 0
	board[k][l] = player
	catchpawn(board, n, player, k, l)
	return (board)

def catchpawn(board, n, player, k , l):
	c = l + 1
	pos = -1
	while (c != n and board[k][c] != 0):
		if (board[k][c] == player):
			pos = c
		c = c + 1
	if (pos != -1 and board[k][l] == board[k][pos]):
		claimPawn(board, n, player, k, l, pos, "RIGHT")
	pos = -1
	c = l - 1
	while (c != -1 and board[k][c] != 0):
		if (board[k][c] == player):
			pos = c
		c = c - 1
	if (pos != -1 and board[k][l] == board[k][pos]):
		claimPawn(board, n, player, k, l, pos, "LEFT")
	pos = -1
	c = k - 1
	while (c != -1 and board[c][l] != 0):
		if (board[c][l] == player):
			pos = c
		c = c - 1
	if (pos != -1 and board[k][l] == board[pos][l]):
		claimPawn(board, n, player, k, l, pos, "UP")
	pos = -1
	c = k + 1
	while (c != n and board[c][l] != 0):
		if (board[c][l] == player):
			pos = c
		c = c + 1
	if (pos != -1 and board[k][l] == board[pos][l]):
		claimPawn(board, n, player, k, l, pos, "DOWN")

def claimPawn(board, n, player, k, l, pos, direction):
	if (direction == "RIGHT"):
		col = l + 1
		while (col != pos):
			board[k][col] = player
			col = col + 1
	if (direction == "LEFT"):
		col = l - 1
		while (col != pos):
			board[k][col] = player
			col = col - 1
	if (direction == "UP"):
		row = k - 1
		while (row != pos):
			board[row][l] = player
			row = row - 1
	if (direction == "DOWN"):
		row = k + 1
		while (row != pos):
			board[row][l] = player
			row = row + 1

def lose(board, n, player):
	row = 0
	col = 0
	if (pawnLeft(board, n, player) == False):
		return (False)
	#while (row != n):
		#if (possiblePawn == False):



def pawnLeft(board, n, player):
	row = 0
	col = 0
	p1 = 0
	p2 = 0
	while (row != n):
		if (board[row][col] == 1):
			p1 = p1 + 1
		if (board[row][col] == 2):
			p2 = p2 + 1
		while (col != n):
			if (board[row][col] == 1):
				p1 = p1 + 2
			if (board[row][col] == 2):
				p2 = p2 + 2
			col = col + 1
		if (col == n):
			col = 0
		row = row + 1
	if (p1 == 0 or p2 == 0):
		return (True)
	else:
		return (False)

def mingMang(n):
	player = 1
	board = newBoard(n)
	while (lose(board, n, player) == False):
		display(board, n)
		print("Player", player, ':')
		try:
			pawn = selectPawn(board, n, player)
			destination = selectDestination(board, n, pawn[0], pawn[1])
		except KeyboardInterrupt:
			print('\n')
			exit()
		board = move(board, n, player, pawn[0], pawn[1], destination[0], destination[1])
		if (player == 2):
			player = 1
		else:
			player = player + 1	

mingMang(4)