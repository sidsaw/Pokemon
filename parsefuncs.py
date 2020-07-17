def switch(m, game):
	playernum = m.group(1)
	switch_in = m.group(2)
	switch_out = game.sides[playernum].activepok
	# if the switch in is coming after a pokemon fainted
	if switch_out == "":
		game.sides[playernum].activepok = switch_in
		return
	# clear leech seed and activated moves for the active pokemon
	game.sides[playernum].pokemon[switch_out].leechseed = ""
	game.sides[playernum].pokemon[switch_out].activatedmove = ""
	# add 1 to switch out for current active pokemon
	game.sides[playernum].pokemon[switch_out].stats['switchouts'] += 1
	# add 1 to switch in for switch_in pokemon
	game.sides[playernum].pokemon[switch_in].stats['switchins'] += 1
	# change active pokemon name
	game.sides[playernum].activepok = switch_in

def faint(m, game):
	playernum = m.group(1)
	faintedpok = m.group(2)
	# update to fainted
	game.sides[playernum].pokemon[faintedpok].alive = False
	# clear active pokemon
	game.sides[playernum].activepok = ""

def miss(m, game):
	playernum = m.group(1)
	misspok = m.group(2)
	# update faints
	game.sides[playernum].pokemon[misspok].stats['misses'] += 1

def crit(m, game):
	# group 1 is player num of pokemon that was HIT with crit
	playernum = m.group(1)
	if playernum == '1':
		critpok = game.sides['2'].activepok
		game.sides['2'].pokemon[critpok].stats['crits'] += 1
	else:
		critpok = game.sides['1'].activepok
		game.sides['1'].pokemon[critpok].stats['crits'] += 1

def ls_start(m, game):
	print("in leech seed start")
	# group 1 is player number
	playernum = m.group(1)
	# group 2 is pokemon nickname
	startpok = m.group(2)
	if playernum == '1':
		# get other active pokemon (the one that used leech seed)
		ls_starter = game.sides['2'].activepok
		# set leechseed on pokemon
		game.sides['1'].pokemon[startpok].leechseed = ls_starter
	else:
		# get other active pokemon (the one that used leech seed)
		ls_starter = game.sides['1'].activepok
		# set leechseed on pokemon
		game.sides['2'].pokemon[startpok].leechseed = ls_starter

def ls_end(m, game):
	print("in leech seed end")
	# group 1 is player number
	playernum = m.group(1)
	# group 2 is pokemon nickname
	endpok = m.group(2)
	game.sides[playernum].pokemon[endpok].leechseed = ""

def status_start(m, game):
	print("lol")

def cure_status(m, game):
	print("in cure_status")
	# group 1 is player number
	# group 3 is the status condition
	playernum = m.group(1)
	statusedpok = m.group(2)
	# clear all statuses for the pokemon
	game.sides[playernum].pokemon[statusedpok].poisoned = ""
	game.sides[playernum].pokemon[statusedpok].burned = ""







