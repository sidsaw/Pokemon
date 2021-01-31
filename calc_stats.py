import re
import string
import os
import sys
from sqlite3 import connect
from parse_funcs import *
from debug_funcs import *

class Pokemon:
	def __init__(self):
		self.name = ""
		self.hpstat = 0
		# this is a percentage
		self.remaininghp = 100
		self.poisoned = ""
		self.burned = ""
		self.leechseed = ""
		self.activatedmove = ""
		self.cursed = ""
		self.confused = ""
		self.alive = True
		self.stats = dict()
		self.stats['kills'] = 0
		self.stats['totaldd'] = 0
		self.stats['directdd'] = 0
		self.stats['indirectdd'] = 0
		self.stats['activeturns'] = 0
		self.stats['switchins'] = 0
		self.stats['switchouts'] = 0
		self.stats['misses'] = 0
		self.stats['crits'] = 0


class Side:
	def __init__(self):
		
		self.playername = ""
		self.remaining = 0
		self.startingnumpok = 0
		# this is the hazards on the other side, value should be pokemon on THIS side
		# key is hazard name, value is pokemon nickname, exception is key numspikes, which takes a number
		self.hazards = dict()
		self.hazards['numspikes'] = 0
		self.hazards['spikes1'] = ""
		self.hazards['spikes2'] = ""
		self.hazards['spikes3'] = ""
		self.hazards['stealthrocks'] = ""
		self.hazards['tspikes'] = ""

		# key is be nickname, value is be pokemon object
		self.pokemon = dict()

		# Turn data
		self.activepok = ""
		self.move = ""
		self.usedmove = False
		self.switch = False


class Game:
	def __init__(self):
		self.replayid = ""

		# key is weather name, value is pokemon name
		self.weather = dict()
		self.weather['sandstorm'] = ""
		self.weather['hail'] = ""
		self.weather['startedby'] = ""

		# key is integer [1, 2], value is side object
		self.sides = dict()
		self.sides['1'] = Side()
		self.sides['2'] = Side()

		# stores last event in game
		self.lastevent = ""

test_filename = ""

if(len(sys.argv) == 2):
	test_filename = sys.argv[1]

else:
	sys.exit("Please provide only a test filename as a command line argument")

current_dir = os.getcwd()

test_filepath = os.path.join(current_dir, 'test_games', test_filename)

with open(test_filepath) as f:
	replay = f.read()

game = Game()

# get replay id
replayid = re.search('(?<=gen[0-9]ou-)[0-9]+', replay).group(0)
game.replayid = replayid

# get player names
p1name = re.search('(?<=\|player\|p1\|)[^\|]+', replay).group(0)
game.sides['1'].playername = p1name
p2name = re.search('(?<=\|player\|p2\|)[^\|]+', replay).group(0)
game.sides['2'].playername = p2name

# get pokemon on each side
p1pok = []
pattern = re.compile(r'(?<=\|poke\|p1\|)[^\|,]+')
for m in re.finditer(pattern, replay):
	p1pok.append(m.group(0))
# set number of starting pok
game.sides['1'].startingnumpok = len(p1pok)

p2pok = []
pattern = re.compile(r'(?<=\|poke\|p2\|)[^\|,]+')
for m in re.finditer(pattern, replay):
	p2pok.append(m.group(0))
# set number of starting pok
game.sides['2'].startingnumpok = len(p2pok)

# parse whole replay for pokemon and their nicknames
# group 1 is playernum, group 2 is nickname, group 3 is actual pokemon name
pattern = re.compile(r'(?<=\|switch\|p([0-9])a: )([^\|]+)\|([^\|,]+)')
for m in re.finditer(pattern, replay):
	playernum = m.group(1)
	poknickname = m.group(2)
	pokactual = m.group(3)
	# skip duplicates
	if poknickname in game.sides[playernum].pokemon:
		continue
	game.sides[playernum].pokemon[poknickname] = Pokemon()
	game.sides[playernum].pokemon[poknickname].name = pokactual
	# TODO query db for pokemon HP stat and set hp stat for pokemon
	statement = "SELECT hp FROM pokedex WHERE pokemon=?"
	#curs.execute(statement, (pokactual,))
	#result = curs.fetchall()
	#if not result:
		# TODO figure out how to actual error handle this
	#	print("couldn't parse pokemon for hp stat: " + pokactual)
	#game.sides[playernum].pokemon[poknickname].hpstat = result[0][0]

# get text before turn 1, get first 2 pokemon and possible weathers
preturn1data = re.search(r'((.|\n)*?)(?=\|turn\|1)', replay).group(0)

# get first 2 pokemon
startp1pok = re.search(r'(?<=\|switch\|p1a: )([^\|]+)\|([^\|,]+)', preturn1data).group(1)
startp2pok = re.search(r'(?<=\|switch\|p2a: )([^\|]+)\|([^\|,]+)', preturn1data).group(1)

game.sides['1'].activepok = startp1pok
game.sides['2'].activepok = startp2pok

startweather = re.compile(r'(?<=-weather)\|([^\|]+)\|([^\|]+)\|\[of\] p([0-9])a: (.*)')
for m in re.finditer(startweather, preturn1data):
	# clear weather
	game.weather['sandstorm'] = ""
	game.weather['hail'] = ""
	game.weather['startedby'] = ""
	typeweather = m.group(1)
	side = m.group(3)
	pokname = m.group(4)
	# ignore if not Hail or Sandstorm
	if typeweather == 'RainDance' or typeweather == 'SunnyDay':
		continue
	if typeweather == 'Sandstorm':
		game.weather['sandstorm'] = pokname
	if typeweather == 'Hail':
		game.weather['hail'] = pokname
	game.weather['startedby'] = side

# group 1: turn number, group 2 all turn data
pattern = re.compile(r'(?<=\|turn\|)([0-9]+)((.|\n)*?)((?=\|turn\|)|(?=\|win\|))')
for m in re.finditer(pattern, replay):
	print("parsing turn " + m.group(1))
	turndata = m.group(2)
	for line in turndata.split('\n'):
		# if switch
		if re.search(r'(?<=\|switch\|p([0-9])a: )([^\|]+)', line) != None:
			m = re.search(r'(?<=\|switch\|p([0-9])a: )([^\|]+)', line)
			switch(m, game)

		# if damage
		if re.search(r'(?<=-damage\|)p([0-9])a: ([^\|]+)\|([^\|]+)\|?([^\|]+)?\|?([^\|]+)?', line) != None:
			m = re.search(r'(?<=-damage\|)p([0-9])a: ([^\|]+)\|([^\|]+)\|?([^\|]+)?\|?([^\|]+)?', line)
			#damage(m, game)

		# if move
		if re.search(r'(?<=\|move\|p([0-9])a: )([^\|]+)\|([^\|]+)', line) != None:
			m = re.search(r'(?<=\|move\|p([0-9])a: )([^\|]+)\|([^\|]+)', line)
			move(m, game)

		# if leech seed starts
		if re.search(r'(?<=-start\|p([0-9])a: )([^\|]+)\|move: Leech Seed', line) != None:
			m = re.search(r'(?<=-start\|p([0-9])a: )([^\|]+)\|move: Leech Seed', line)
			ls_start(m, game)
		
		# if leech seed ends
		if re.search(r'(?<=-end\|p([0-9])a: )([^\|]+)\|Leech Seed', line) != None:
			m = re.search(r'(?<=-end\|p([0-9])a: )([^\|]+)\|Leech Seed', line)
			ls_end(m, game)

		# if hazards start
		if re.search(r'(?<=-sidestart\|p([0-9]): )[^\|]+\|(move: )?(.*)', line) != None:
			m = re.search(r'(?<=-sidestart\|p([0-9]): )[^\|]+\|(move: )?(.*)', line)
			hazard_start(m, game)

		# if hazards end
		if re.search(r'(?<=-sideend\|p([0-9]): )[^\|]+\|(move: )?([^\|]+)', line) != None:
			m = re.search(r'(?<=-sideend\|p([0-9]): )[^\|]+\|(move: )?([^\|]+)', line)
			hazard_end(m, game)

		# if weather starts/ends/changes
		if re.search(r'-weather\|([^\|]+)(\|([^\|]+)\|?(.*)?)?', line) != None:
			m = re.search(r'-weather\|([^\|]+)(\|([^\|]+)\|?(.*)?)?', line)
			weather(m, game)

		# if poison or burn or tox starts
		if re.search(r'(?<=-status\|p([0-9])a: )([^\|]+)\|(.*)', line) != None:
			m = re.search(r'(?<=-status\|p([0-9])a: )([^\|]+)\|([^\|]+)\|?(.*)?', line)
			status_start(m, game)

		# if poison or burn or tox ends
		if re.search(r'(?<=-curestatus\|)p([0-9])a?: ([^\|]+)\|([^\|]+)', line) != None:
			m = re.search(r'(?<=-curestatus\|)p([0-9])a?: ([^\|]+)\|([^\|]+)', line)
			cure_status(m, game)

		# if crit
		if re.search(r'(?<=-crit\|p([0-9])a: )', line) != None:
			m = re.search(r'(?<=-crit\|p([0-9])a: )', line)
			crit(m, game)

		# if miss
		if re.search(r'(?<=-miss\|p([0-9])a: )([^\|]+)', line) != None:
			m = re.search(r'(?<=-miss\|p([0-9])a: )([^\|]+)', line)
			miss(m, game)

		# if faint, clear pok1 or pok2, and update death for current pokemon
		if re.search(r'(?<=faint\|p([0-9])a: )(.*)', line) != None:
			m = re.search(r'(?<=faint\|p([0-9])a: )(.*)', line)
			faint(m, game)

		# TODO if heal
		# TODO if mega
		# change HP stat and actual pok name (not nickname)
		# TODO destiny bond
		# TODO future sight
		# TODO yawn
		# TODO start flag (will handle curse, confused, future sight, sub, belly drum)
		# TODO ghost curse
		# TODO confused

		# TODO increment active turns for pokemon that are alive
		# update turn data on each side
		# clear moves
		game.sides['1'].move = ""
		game.sides['2'].move = ""
		game.sides['1'].usedmove = False
		game.sides['2'].usedmove = False
		# clear switches
		game.sides['1'].switch = False
		game.sides['2'].switch = False


# TODO increment appearance value in db for all pokemon in p1pok and p2pok

# TODO get actual player names, calculate score and return stats
db_test_damage_regex()





	







