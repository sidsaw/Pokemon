import re
import string
from sqlite3 import connect
from parsefuncs import *
from debugfuncs import *
replay = """
</style>
<div class="wrapper replay-wrapper" style="max-width:1180px;margin:0 auto">
<input type="hidden" name="replayid" value="gen6ou-1157065651" />
<div class="battle"></div><div class="battle-log"></div><div class="replay-controls"></div><div class="replay-controls-2"></div>
<h1 style="font-weight:normal;text-align:center"><strong>[Gen 6] OU</strong><br /><a href="http://pokemonshowdown.com/users/nottsid69420" class="subtle" target="_blank">nottsid69420</a> vs. <a href="http://pokemonshowdown.com/users/notsid69420" class="subtle" target="_blank">notsid69420</a></h1>
<script type="text/plain" class="battle-log-data">|j|nottsid69420


|j|notsid69420


|t:|1595619452


|player|p1|nottsid69420|169|


|player|p2|notsid69420|preschooler|
|teamsize|p1|2
|teamsize|p2|5
|gametype|singles
|gen|6
|tier|[Gen 6] OU
|clearpoke
|poke|p1|Mandibuzz, F|item
|poke|p1|Mew|item
|poke|p2|Tyranitar, M|item
|poke|p2|Abomasnow, F|item
|poke|p2|Mew|item
|poke|p2|Mandibuzz, F|item
|poke|p2|Politoed, M|item
|rule|Sleep Clause Mod: Limit one foe put to sleep
|rule|Species Clause: Limit one of each Pokmon
|rule|OHKO Clause: OHKO moves are banned
|rule|Moody Clause: Moody is banned
|rule|Evasion Moves Clause: Evasion moves are banned
|rule|Endless Battle Clause: Forcing endless battles is banned
|rule|HP Percentage Mod: HP is shown in percentages
|rule|Swagger Clause: Swagger is banned
|teampreview


|
|t:|1595619472
|start
|switch|p1a: Mandibuzz|Mandibuzz, F|377\\/377
|switch|p2a: Tyranitar|Tyranitar, M|100\\/100
|-weather|Sandstorm|[from] ability: Sand Stream|[of] p2a: Tyranitar
|turn|1


|
|t:|1595619477
|move|p1a: Mandibuzz|Confide|p2a: Tyranitar
|-unboost|p2a: Tyranitar|spa|1
|move|p2a: Tyranitar|Curse|p2a: Tyranitar
|-unboost|p2a: Tyranitar|spe|1
|-boost|p2a: Tyranitar|atk|1
|-boost|p2a: Tyranitar|def|1
|
|-weather|Sandstorm|[upkeep]
|upkeep
|turn|2
"""

# |
# |t:|1595619882
# |move|p1a: Mandibuzz|Confide|p2a: Tyranitar
# |-unboost|p2a: Tyranitar|spa|1
# |move|p2a: Tyranitar|Curse|p2a: Tyranitarp
# |-unboost|p2a: Tyranitar|spe|1
# |-boost|p2a: Tyranitar|atk|1
# |-boost|p2a: Tyranitar|def|1
# |
# |-weather|Sandstorm|[upkeep]
# |upkeep
# |turn|3


# |
# |t:|1595619885
# |move|p1a: Mandibuzz|Confide|p2a: Tyranitar
# |-unboost|p2a: Tyranitar|spa|1
# |move|p2a: Tyranitar|Curse|p2a: Tyranitar
# |-unboost|p2a: Tyranitar|spe|1
# |-boost|p2a: Tyranitar|atk|1
# |-boost|p2a: Tyranitar|def|1
# |
# |-weather|Sandstorm|[upkeep]
# |upkeep
# |turn|4


# |
# |t:|1595619889
# |move|p1a: Mandibuzz|Confide|p2a: Tyranitar
# |-unboost|p2a: Tyranitar|spa|1
# |move|p2a: Tyranitar|Curse|p2a: Tyranitar
# |-unboost|p2a: Tyranitar|spe|1
# |-boost|p2a: Tyranitar|atk|1
# |-boost|p2a: Tyranitar|def|1
# |
# |-weather|Sandstorm|[upkeep]
# |upkeep
# |turn|5


# |
# |t:|1595619893
# |move|p1a: Mandibuzz|Confide|p2a: Tyranitar
# |-unboost|p2a: Tyranitar|spa|1
# |move|p2a: Tyranitar|Curse|p2a: Tyranitar
# |-unboost|p2a: Tyranitar|spe|1
# |-boost|p2a: Tyranitar|atk|1
# |-boost|p2a: Tyranitar|def|1
# |
# |-weather|none
# |upkeep
# |turn|6


# |
# |t:|1595619900
# |switch|p2a: Abomasnow|Abomasnow, F|100\\/100
# |-weather|Hail|[from] ability: Snow Warning|[of] p2a: Abomasnow
# |move|p1a: Mandibuzz|Confide|p2a: Abomasnow
# |-unboost|p2a: Abomasnow|spa|1
# |
# |-weather|Hail|[upkeep]
# |upkeep
# |turn|7


# |
# |t:|1595619904
# |move|p1a: Mandibuzz|Confide|p2a: Abomasnow
# |-unboost|p2a: Abomasnow|spa|1
# |move|p2a: Abomasnow|Sleep Talk||[still]
# |-fail|p2a: Abomasnow
# |
# |-weather|Hail|[upkeep]
# |upkeep
# |turn|8


# |
# |t:|1595619908
# |move|p1a: Mandibuzz|Confide|p2a: Abomasnow
# |-unboost|p2a: Abomasnow|spa|1
# |move|p2a: Abomasnow|Sleep Talk||[still]
# |-fail|p2a: Abomasnow
# |
# |-weather|Hail|[upkeep]
# |upkeep
# |turn|9


# |
# |t:|1595619978
# |move|p1a: Mandibuzz|Confide|p2a: Abomasnow
# |-unboost|p2a: Abomasnow|spa|1
# |move|p2a: Abomasnow|Sleep Talk||[still]
# |-fail|p2a: Abomasnow
# |
# |-weather|Hail|[upkeep]
# |upkeep
# |turn|10


# |
# |t:|1595619982
# |move|p1a: Mandibuzz|Confide|p2a: Abomasnow
# |-unboost|p2a: Abomasnow|spa|1
# |move|p2a: Abomasnow|Sleep Talk||[still]
# |-fail|p2a: Abomasnow
# |
# |-weather|none
# |upkeep
# |turn|11


# |
# |t:|1595619991
# |move|p1a: Mandibuzz|Rain Dance|p1a: Mandibuzz
# |-weather|RainDance
# |move|p2a: Abomasnow|Sleep Talk||[still]
# |-fail|p2a: Abomasnow
# |
# |-weather|RainDance|[upkeep]
# |upkeep
# |turn|12


# |
# |t:|1595620005
# |move|p1a: Mandibuzz|Confide|p2a: Abomasnow
# |-unboost|p2a: Abomasnow|spa|1
# |move|p2a: Abomasnow|Sleep Talk||[still]
# |-fail|p2a: Abomasnow
# |
# |-weather|RainDance|[upkeep]
# |upkeep
# |turn|13


# |
# |t:|1595620010
# |move|p1a: Mandibuzz|Confide|p2a: Abomasnow
# |-unboost|p2a: Abomasnow|spa|0
# |move|p2a: Abomasnow|Sleep Talk||[still]
# |-fail|p2a: Abomasnow
# |
# |-weather|RainDance|[upkeep]
# |upkeep
# |turn|14


# |
# |t:|1595620013
# |move|p1a: Mandibuzz|Confide|p2a: Abomasnow
# |-unboost|p2a: Abomasnow|spa|0
# |move|p2a: Abomasnow|Sleep Talk||[still]
# |-fail|p2a: Abomasnow
# |
# |-weather|RainDance|[upkeep]
# |upkeep
# |turn|15


# |
# |t:|1595620017
# |move|p1a: Mandibuzz|Confide|p2a: Abomasnow
# |-unboost|p2a: Abomasnow|spa|0
# |move|p2a: Abomasnow|Sleep Talk||[still]
# |-fail|p2a: Abomasnow
# |
# |-weather|none
# |upkeep
# |turn|16


# |
# |t:|1595620021
# |move|p1a: Mandibuzz|Sunny Day|p1a: Mandibuzz
# |-weather|SunnyDay
# |move|p2a: Abomasnow|Sleep Talk||[still]
# |-fail|p2a: Abomasnow
# |
# |-weather|SunnyDay|[upkeep]
# |upkeep
# |turn|17


# |
# |t:|1595620026
# |move|p1a: Mandibuzz|Confide|p2a: Abomasnow
# |-unboost|p2a: Abomasnow|spa|0
# |move|p2a: Abomasnow|Sleep Talk||[still]
# |-fail|p2a: Abomasnow
# |
# |-weather|SunnyDay|[upkeep]
# |upkeep
# |turn|18


# |
# |t:|1595620030
# |move|p1a: Mandibuzz|Confide|p2a: Abomasnow
# |-unboost|p2a: Abomasnow|spa|0
# |move|p2a: Abomasnow|Sleep Talk||[still]
# |-fail|p2a: Abomasnow
# |
# |-weather|SunnyDay|[upkeep]
# |upkeep
# |turn|19


# |
# |t:|1595620034
# |move|p1a: Mandibuzz|Confide|p2a: Abomasnow
# |-unboost|p2a: Abomasnow|spa|0
# |move|p2a: Abomasnow|Sleep Talk||[still]
# |-fail|p2a: Abomasnow
# |
# |-weather|SunnyDay|[upkeep]
# |upkeep
# |turn|20


# |
# |t:|1595620039
# |move|p1a: Mandibuzz|Confide|p2a: Abomasnow
# |-unboost|p2a: Abomasnow|spa|0
# |move|p2a: Abomasnow|Sleep Talk||[still]
# |-fail|p2a: Abomasnow
# |
# |-weather|none
# |upkeep
# |turn|21


# |
# |t:|1595620055
# |switch|p2a: Mew|Mew|100\\/100
# |move|p1a: Mandibuzz|Confide|p2a: Mew
# |-unboost|p2a: Mew|spa|1
# |
# |upkeep
# |turn|22


# |
# |t:|1595620074
# |switch|p1a: Mew|Mew|365\\/365
# |-activate|p2a: Mew|move: Struggle
# |move|p2a: Mew|Struggle|p1a: Mew
# |-damage|p1a: Mew|329\\/365
# |-damage|p2a: Mew|75\\/100|[from] recoil
# |
# |upkeep
# |turn|23


# |
# |t:|1595620171
# |-activate|p2a: Mew|move: Struggle
# |move|p2a: Mew|Struggle|p1a: Mew
# |-damage|p1a: Mew|296\\/365
# |-damage|p2a: Mew|50\\/100|[from] recoil
# |move|p1a: Mew|Sandstorm|p1a: Mew
# |-weather|Sandstorm
# |
# |-weather|Sandstorm|[upkeep]
# |-damage|p2a: Mew|44\\/100|[from] Sandstorm
# |-damage|p1a: Mew|274\\/365|[from] Sandstorm
# |upkeep
# |turn|24


# |
# |t:|1595620180
# |move|p1a: Mew|Hail|p1a: Mew
# |-weather|Hail
# |-activate|p2a: Mew|move: Struggle
# |move|p2a: Mew|Struggle|p1a: Mew
# |-damage|p1a: Mew|241\\/365
# |-damage|p2a: Mew|19\\/100|[from] recoil
# |
# |-weather|Hail|[upkeep]
# |-damage|p2a: Mew|13\\/100|[from] Hail
# |-damage|p1a: Mew|219\\/365|[from] Hail
# |upkeep
# |turn|25


# |
# |t:|1595620189
# |-activate|p2a: Mew|move: Struggle
# |move|p2a: Mew|Struggle|p1a: Mew
# |-damage|p1a: Mew|182\\/365
# |-damage|p2a: Mew|0 fnt|[from] recoil
# |faint|p2a: Mew
# |move|p1a: Mew|Sunny Day|p1a: Mew
# |-weather|SunnyDay
# |
# |-weather|SunnyDay|[upkeep]
# |upkeep


# |
# |t:|1595620201
# |switch|p2a: Politoed|Politoed, M|100\\/100
# |-weather|RainDance|[from] ability: Drizzle|[of] p2a: Politoed
# |turn|26


# |-message|notsid69420 forfeited.


# |
# |win|nottsid69420



# logs = ""

class Pokemon:
	def __init__(self):
		self.name = ""
		self.hpstat = 0
		self.remaininghp = 100
		self.poisoned = ""
		self.burned = ""
		self.leechseed = ""
		self.activatedmove = ""
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
		# key is hazard name, value is pokemon nickname, exception is key numspikes
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
		# key is nickname and side, value 
		self.getactualname = dict()
		
		# key is pokemon name and side, value is nickname
		self.getnickname = dict()

		# key is weather name, value is pokemon name
		self.weather = dict()
		self.weather['sandstorm'] = ""
		self.weather['hail'] = ""
		self.weather['startedby'] = ""

		# key is int [1, 2], value is side object
		self.sides = dict()
		self.sides['1'] = Side()
		self.sides['2'] = Side()

		# stores last event in game
		self.lastevent = ""


game = Game()
# get replay id
replayid = re.search('(?<=gen[0-9]ou-)[0-9]+', replay).group(0)
game.replayid = replayid

# get player names
# TODO check if works with spaces
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
	game.sides[m.group(1)].pokemon[m.group(2)] = Pokemon()
	# TODO query db for pokemon HP stat and set hp stat for pokemon
	game.sides[m.group(1)].pokemon[m.group(2)].name = m.group(3)

# get text before turn 1, get first 2 pokemon and possible weathers
preturn1data = re.search(r'((.|\n)*?)(?=\|turn\|1)', replay).group(0)

# get first 2 pokemon
startp1pok = re.search(r'(?<=\|switch\|p1a: )([^\|]+)\|([^\|,]+)', preturn1data).group(1)
startp2pok = re.search(r'(?<=\|switch\|p2a: )([^\|]+)\|([^\|,]+)', preturn1data).group(1)

game.sides['1'].activepok = startp1pok
game.sides['2'].activepok = startp2pok

startweather = re.compile(r'(?<=-weather)\|([^\|]+)\|([^\|]+)\|\[of\] p([0-9])a: (.*)')
for m in re.finditer(startweather, preturn1data):
	print('found preturn1 weather match')
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

		# if non dying damage
		# if re.search(r'(?<=-damage\|p([0-9])a: )([^\|]+)\|([0-9]+)\\/([0-9]+)', line) != None:
		# 	m = re.search(r'(?<=-damage\|p([0-9])a: )([^\|]+)\|([0-9]+)\\/([0-9]+)', line)
		# 	print("matched damage")
		# TODO remember that damage from status can come due to the pokemon itself, so "self" might be statuser

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

		# if other pokemon specific hazard starts 
		# 
		# if other pokemon specific hazard ends

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
		
		# if dying damage (faint), update kill and damage for respective pokemon
		if re.search(r'(?<=-damage\|p([0-9])a: )([^\|]+)\|0 fnt(.*)', line) != None:
			m = re.search(r'(?<=-damage\|p([0-9])a: )([^\|]+)\|0 fnt(.*)', line)
			# print("matched dying damage")
			# # group 1 is player num
			# print(m.group(1))
			# # group 2 is pokemon nickname
			# print(m.group(2))
			# # group 3 is additional data
			# # look for tox, brn, poison, leech seed, sandstorm, hail, spikes, rocks, 
			# print(m.group(3))

		# if faint, clear pok1 or pok2, and update death for current pokemon
		if re.search(r'(?<=faint\|p([0-9])a: )(.*)', line) != None:
			m = re.search(r'(?<=faint\|p([0-9])a: )(.*)', line)
			faint(m, game)

		# TODO if heal
		# TODO destiny bond
		# TODO future sight
		# TODO yawn

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


# increment appearance value in db for all pokemon in p1pok and p2pok

# get actual player names, calculate score and return stats
db_print_weather(game)







	







