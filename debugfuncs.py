def db_print_switches(game):
	for key in game.sides['1'].pokemon:
		name = game.sides['1'].pokemon[key].name
		switchouts = game.sides['1'].pokemon[key].stats['switchouts']
		switchins = game.sides['1'].pokemon[key].stats['switchins']
		print(key + " switched out " + str(switchouts) + " and switched in " + str(switchins))

	for key in game.sides['2'].pokemon:
		name = game.sides['2'].pokemon[key].name
		switchouts = game.sides['2'].pokemon[key].stats['switchouts']
		switchins = game.sides['2'].pokemon[key].stats['switchins']
		print(key + " switched out " + str(switchouts) + " and switched in " + str(switchins))

def db_print_miss(game):
	for key in game.sides['1'].pokemon:
		name = game.sides['1'].pokemon[key].name
		misses = game.sides['1'].pokemon[key].stats['misses']
		print(key + " missed " + str(misses))

	for key in game.sides['2'].pokemon:
		name = game.sides['2'].pokemon[key].name
		misses = game.sides['2'].pokemon[key].stats['misses']
		print(key + " missed " + str(misses))


def db_print_crit(game):
	for key in game.sides['1'].pokemon:
		misses = game.sides['1'].pokemon[key].stats['crits']
		print(key + " got " + str(misses) + " crits")

	for key in game.sides['2'].pokemon:
		misses = game.sides['2'].pokemon[key].stats['crits']
		print(key + " got " + str(misses) + " crits")

def db_print_leechseed(game):
	for key in game.sides['1'].pokemon:
		if game.sides['1'].pokemon[key].leechseed != "":
			lspok = game.sides['1'].pokemon[key].leechseed
			print(key + " is " + " leechseeded by " + lspok)

	for key in game.sides['2'].pokemon:
		if game.sides['2'].pokemon[key].leechseed != "":
			lspok = game.sides['2'].pokemon[key].leechseed
			print(key + " is " + " leechseeded by " + lspok)

def db_print_moves(game):
	print("printing moves")
	print("side 1: " + game.sides['1'].move)
	print("side 2: " + game.sides['2'].move)

def db_print_statuses(game):
	for key in game.sides['1'].pokemon:
		if game.sides['1'].pokemon[key].burned != "":
			statuser = game.sides['1'].pokemon[key].burned
			print(key + " is burned by " + statuser)
		if game.sides['1'].pokemon[key].poisoned != "":
			statuser = game.sides['1'].pokemon[key].poisoned
			print(key + " is poisoned by " + statuser)
	
	for key in game.sides['2'].pokemon:
		if game.sides['2'].pokemon[key].burned != "":
			statuser = game.sides['2'].pokemon[key].burned
			print(key + " is burned by " + statuser)
		if game.sides['2'].pokemon[key].poisoned != "":
			statuser = game.sides['2'].pokemon[key].poisoned
			print(key + " is poisoned by " + statuser)

def db_print_hazards(game):
	print('hazards on side 1')
	sp1_1 = game.sides['1'].hazards['spikes1']
	sp1_2 = game.sides['1'].hazards['spikes2']
	sp1_3 = game.sides['1'].hazards['spikes3']
	ns1 = game.sides['1'].hazards['numspikes']
	sr1 = game.sides['1'].hazards['stealthrocks']
	ts1 = game.sides['1'].hazards['tspikes']
	if sp1_1 != '':
		print("1st spikes: " + sp1_1)
	if sp1_2 != '':
		print("2nd spikes: " + sp1_2)
	if sp1_3 != '':
		print("3rd spikes: " + sp1_3)
	if ns1 != 0:
		print("numspikes: " + str(ns1))
	if sr1 != '':
		print("stealth rocks: " + sr1)
	if ts1 != '':
		print("toxic spikes: " + ts1)

	print('hazards on side 2')
	sp2_1 = game.sides['2'].hazards['spikes1']
	sp2_2 = game.sides['2'].hazards['spikes2']
	sp2_3 = game.sides['2'].hazards['spikes3']
	ns2 = game.sides['2'].hazards['numspikes']
	sr2 = game.sides['2'].hazards['stealthrocks']
	ts2 = game.sides['2'].hazards['tspikes']
	if sp2_1 != '':
		print("1st spikes: " + sp2_1)
	if sp2_2 != '':
		print("2nd spikes: " + sp2_2)
	if sp2_3 != '':
		print("3rd spikes: " + sp2_3)
	if ns2 != 0:
		print("numspikes: " + str(ns2))
	if sr2 != '':
		print("stealth rocks: " + sr2)
	if ts2 != '':
		print("toxic spikes: " + ts2)

def db_print_weather(game):
	print('printing game weather')
	if game.weather['hail'] != '':
		pok = game.weather['hail']
		side = game.weather['startedby']
		print('Weather: Hail')
		print('Started by: ' + pok)
		print('Side: ' + side)
	elif game.weather['sandstorm'] != '':
		pok = game.weather['sandstorm']
		side = game.weather['startedby']
		print('Weather: Sandstorm')
		print('Started by: ' + pok)
		print('Side: ' + side)
	else:
		print('No weather')












