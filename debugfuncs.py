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