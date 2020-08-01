import re
import string
from sqlite3 import connect
from parsefuncs import *
from debugfuncs import *
replay = """
<!DOCTYPE html>
<meta charset="utf-8" />
<!-- version 1 -->
<title>[Gen 6] OU replay: samsarin23 vs. alishahc</title>
<style>
</style>
<div class="wrapper replay-wrapper" style="max-width:1180px;margin:0 auto">
<input type="hidden" name="replayid" value="gen6ou-1152590909" />
<div class="battle"></div><div class="battle-log"></div><div class="replay-controls"></div><div class="replay-controls-2"></div>
<h1 style="font-weight:normal;text-align:center"><strong>[Gen 6] OU</strong><br /><a href="http://pokemonshowdown.com/users/samsarin23" class="subtle" target="_blank">samsarin23</a> vs. <a href="http://pokemonshowdown.com/users/alishahc" class="subtle" target="_blank">alishahc</a></h1>
<script type="text/plain" class="battle-log-data">|j|samsarin23
|j|alishahc


|player|p1|samsarin23|170|


|player|p2|alishahc|124|
|teamsize|p1|6
|teamsize|p2|6
|gametype|singles
|gen|6
|tier|[Gen 6] OU
|clearpoke
|poke|p1|Thundurus, M|item
|poke|p1|Suicune|item
|poke|p1|Metagross|item
|poke|p1|Hydreigon, F|item
|poke|p1|Jellicent, M|item
|poke|p1|Uxie|item
|poke|p2|Clefable, F|item
|poke|p2|Garchomp, M|item
|poke|p2|Jirachi|item
|poke|p2|Amoonguss, M|item
|poke|p2|Infernape, M|item
|poke|p2|Gyarados, M|item
|rule|Sleep Clause Mod: Limit one foe put to sleep
|rule|Species Clause: Limit one of each Pokmon
|rule|OHKO Clause: OHKO moves are banned
|rule|Moody Clause: Moody is banned
|rule|Evasion Moves Clause: Evasion moves are banned
|rule|Endless Battle Clause: Forcing endless battles is banned
|rule|HP Percentage Mod: HP is shown in percentages
|rule|Swagger Clause: Swagger is banned
|teampreview


|j| yeeeur


|
|start
|switch|p1a: Oopsie|Uxi|100\\/100
|switch|p2a: Jirachi|Jirachi|404\\/404
|turn|1


|j| etherealblues


|j| kushpatel98


|c| yeeeur|i like how all of samarth's pokemon are blue


|
|move|p2a: Jirachi|Thunder Wave|p1a: Oopsie
|-status|p1a: Oopsie|par
|cant|p1a: Oopsie|par
|
|upkeep
|turn|2


|j| pk slam


|
|move|p2a: Jirachi|Iron Head|p1a: Oopsie
|-damage|p1a: Oopsie|78\\/100 par
|cant|p1a: Oopsie|flinch
|
|-heal|p1a: Oopsie|84\\/100 par|[from] item: Leftovers
|upkeep
|turn|3


|j| joebigs


|
|move|p2a: Jirachi|Iron Head|p1a: Oopsie
|-damage|p1a: Oopsie|63\\/100 par
|move|p1a: Oopsie|Stealth Rock|p2a: Jirachi
|-sidestart|p2: alishahc|move: Stealth Rock
|
|-heal|p1a: Oopsie|69\\/100 par|[from] item: Leftovers
|upkeep
|turn|4


|j| sid69420


|
|move|p2a: Jirachi|Iron Head|p1a: Oopsie
|-damage|p1a: Oopsie|45\\/100 par
|cant|p1a: Oopsie|flinch
|
|-heal|p1a: Oopsie|51\\/100 par|[from] item: Leftovers
|upkeep
|turn|5


|
|switch|p1a: Metacute-Mega|Metagross|100\\/100
|move|p2a: Jirachi|Iron Head|p1a: Metacute-Mega
|-resisted|p1a: Metacute-Mega
|-damage|p1a: Metacute-Mega|88\\/100
|
|upkeep
|turn|6


|j| eviolitemachop


|
|move|p2a: Jirachi|Thunder Wave|p1a: Metacute-Mega
|-status|p1a: Metacute-Mega|par
|move|p1a: Metacute-Mega|Hammer Arm|p2a: Jirachi
|-damage|p2a: Jirachi|291\\/404
|-unboost|p1a: Metacute-Mega|spe|1
|
|-heal|p2a: Jirachi|316\\/404|[from] item: Leftovers
|upkeep
|turn|7


|
|switch|p1a: weirdassmf|Hydreigon, F|100\\/100
|move|p2a: Jirachi|Fire Punch|p1a: weirdassmf
|-resisted|p1a: weirdassmf
|-damage|p1a: weirdassmf|88\\/100
|-status|p1a: weirdassmf|brn
|
|-heal|p2a: Jirachi|341\\/404|[from] item: Leftovers
|-damage|p1a: weirdassmf|76\\/100 brn|[from] brn
|upkeep
|turn|8


|
|switch|p2a: Clefable|Clefable, F|394\\/394
|move|p1a: weirdassmf|Dark Pulse|p2a: Clefable
|-resisted|p2a: Clefable
|-damage|p2a: Clefable|308\\/394
|-damage|p1a: weirdassmf|66\\/100 brn|[from] item: Life Orb
|
|-heal|p2a: Clefable|332\\/394|[from] item: Leftovers
|-damage|p1a: weirdassmf|54\\/100 brn|[from] brn
|upkeep
|turn|9


|
|switch|p1a: Metacute-Mega|Metagross|88\\/100 par
|move|p2a: Clefable|Calm Mind|p2a: Clefable
|-boost|p2a: Clefable|spa|1
|-boost|p2a: Clefable|spd|1
|
|-heal|p2a: Clefable|356\\/394|[from] item: Leftovers
|upkeep
|turn|10


|
|detailschange|p1a: Metacute-Mega|Metagross-Mega
|-mega|p1a: Metacute-Mega|Metagross|Metagrossite
|cant|p1a: Metacute-Mega|par
|move|p2a: Clefable|Moonblast|p1a: Metacute-Mega
|-resisted|p1a: Metacute-Mega
|-damage|p1a: Metacute-Mega|65\\/100 par
|-unboost|p1a: Metacute-Mega|spa|1
|
|-heal|p2a: Clefable|380\\/394|[from] item: Leftovers
|upkeep
|turn|11


|
|move|p1a: Metacute-Mega|Bullet Punch|p2a: Clefable
|-supereffective|p2a: Clefable
|-damage|p2a: Clefable|152\\/394
|move|p2a: Clefable|Moonblast|p1a: Metacute-Mega
|-resisted|p1a: Metacute-Mega
|-damage|p1a: Metacute-Mega|43\\/100 par
|
|-heal|p2a: Clefable|176\\/394|[from] item: Leftovers
|upkeep
|turn|12


|
|switch|p2a: Jirachi|Jirachi|341\\/404
|-damage|p2a: Jirachi|316\\/404|[from] Stealth Rock
|cant|p1a: Metacute-Mega|par
|
|-heal|p2a: Jirachi|341\\/404|[from] item: Leftovers
|upkeep
|turn|13


|
|move|p2a: Jirachi|Fire Punch|p1a: Metacute-Mega
|-supereffective|p1a: Metacute-Mega
|-damage|p1a: Metacute-Mega|13\\/100 par
|move|p1a: Metacute-Mega|Hammer Arm|p2a: Jirachi
|-damage|p2a: Jirachi|180\\/404
|-unboost|p1a: Metacute-Mega|spe|1
|
|-heal|p2a: Jirachi|205\\/404|[from] item: Leftovers
|upkeep
|turn|14


|
|move|p1a: Metacute-Mega|Bullet Punch|p2a: Jirachi
|-resisted|p2a: Jirachi
|-damage|p2a: Jirachi|156\\/404
|move|p2a: Jirachi|Fire Punch|p1a: Metacute-Mega
|-supereffective|p1a: Metacute-Mega
|-damage|p1a: Metacute-Mega|0 fnt
|faint|p1a: Metacute-Mega
|
|-heal|p2a: Jirachi|181\\/404|[from] item: Leftovers
|upkeep


|
|switch|p1a: weirdassmf|Hydreigon, F|54\\/100 brn
|turn|15


|
|move|p1a: weirdassmf|Dark Pulse|p2a: Jirachi
|-supereffective|p2a: Jirachi
|-damage|p2a: Jirachi|0 fnt
|-damage|p1a: weirdassmf|44\\/100 brn|[from] item: Life Orb
|faint|p2a: Jirachi
|
|-damage|p1a: weirdassmf|32\\/100 brn|[from] brn
|upkeep


|
|switch|p2a: Clefable|Clefable, F|176\\/394
|turn|16


|
|switch|p1a: Oopsie|Uxie|51\\/100 par
|move|p2a: Clefable|Soft-Boiled|p2a: Clefable
|-heal|p2a: Clefable|373\\/394
|
|-heal|p2a: Clefable|394\\/394|[from] item: Leftovers
|-heal|p1a: Oopsie|58\\/100 par|[from] item: Leftovers
|upkeep
|turn|17


|
|move|p2a: Clefable|Moonblast|p1a: Oopsie
|-damage|p1a: Oopsie|34\\/100 par
|-unboost|p1a: Oopsie|spa|1
|move|p1a: Oopsie|Yawn|p2a: Clefable
|-start|p2a: Clefable|move: Yawn|[of] p1a: Oopsie
|
|-heal|p1a: Oopsie|40\\/100 par|[from] item: Leftovers
|upkeep
|turn|18


|l| joebigs


|l| eviolitemachop


|
|switch|p2a: Gyarados|Gyarados, M|331\\/331
|-damage|p2a: Gyarados|249\\/331|[from] Stealth Rock
|-ability|p2a: Gyarados|Intimidate|boost
|-unboost|p1a: Oopsie|atk|1
|move|p1a: Oopsie|Psyshock|p2a: Gyarados
|-damage|p2a: Gyarados|192\\/331
|
|-heal|p1a: Oopsie|46\\/100 par|[from] item: Leftovers
|upkeep
|turn|19


|
|switch|p1a: jelly-scent|Jellicent, M|100\\/100
|detailschange|p2a: Gyarados|Gyarados-Mega, M
|-mega|p2a: Gyarados|Gyarados|Gyaradosite
|-ability|p2a: Gyarados|Mold Breaker
|move|p2a: Gyarados|Crunch|p1a: jelly-scent
|-supereffective|p1a: jelly-scent
|-damage|p1a: jelly-scent|32\\/100
|
|-heal|p1a: jelly-scent|38\\/100|[from] item: Leftovers
|upkeep
|turn|20


|
|switch|p1a: weirdassmf|Hydreigon, F|32\\/100 brn
|move|p2a: Gyarados|Dragon Dance|p2a: Gyarados
|-boost|p2a: Gyarados|atk|1
|-boost|p2a: Gyarados|spe|1
|
|-damage|p1a: weirdassmf|19\\/100 brn|[from] brn
|upkeep
|turn|21


|
|move|p2a: Gyarados|Ice Fang|p1a: weirdassmf
|-supereffective|p1a: weirdassmf
|-damage|p1a: weirdassmf|0 fnt
|faint|p1a: weirdassmf
|
|upkeep


|
|switch|p1a: wundury|Thundurus, M|100\\/100
|turn|22


|j| eviolitemachop


|
|move|p1a: wundury|Thunder Wave|p2a: Gyarados
|-status|p2a: Gyarados|par
|cant|p2a: Gyarados|par
|
|upkeep
|turn|23


|
|move|p1a: wundury|Thunder|p2a: Gyarados
|-supereffective|p2a: Gyarados
|-damage|p2a: Gyarados|0 fnt
|-damage|p1a: wundury|91\\/100|[from] item: Life Orb
|faint|p2a: Gyarados
|
|upkeep


|c| yeeeur|sheesh


|l| eviolitemachop


|c| pk slam|THUNDER!


|c| pk slam|big plays only


|c| sid69420|he really wanted to kill that mofo


|c| pk slam|prankster t wave


|c| pk slam|is scary af


|
|switch|p2a: Garchomp|Garchomp, M|357\\/357
|-damage|p2a: Garchomp|335\\/357|[from] Stealth Rock
|turn|24


|c| pk slam|the age old question


|c| pk slam|does it have hp ice?


|c| sid69420|that fried Gyarados would taste so good in a taco


|
|move|p1a: wundury|Thunder Wave|p2a: Garchomp
|-immune|p2a: Garchomp
|move|p2a: Garchomp|Swords Dance|p2a: Garchomp
|-boost|p2a: Garchomp|atk|2
|
|upkeep
|turn|25


|c| sid69420|lmfaooo


|j| eviolitemachop


|
|move|p1a: wundury|Hidden Power|p2a: Garchomp
|-supereffective|p2a: Garchomp
|-damage|p2a: Garchomp|0 fnt
|-damage|p1a: wundury|81\\/100|[from] item: Life Orb
|faint|p2a: Garchomp
|
|upkeep


|c| pk slam|it does


|c| sid69420|LOL


|c| pk slam|LOL


|c| yeeeur|LMFAO


|c|alishahc|f


|c| sid69420|HP ICE BACK AT IT


|l| eviolitemachop


|j| eviolitemachop


|c| yeeeur|garchomp getting OHKO'd into szn 2


|c| sid69420|Garchomp gets murked every game


|
|switch|p2a: Infernape|Infernape, M|293\\/293
|-damage|p2a: Infernape|257\\/293|[from] Stealth Rock
|turn|26


|
|switch|p2a: Amoonguss|Amoonguss, M|431\\/431
|-damage|p2a: Amoonguss|378\\/431|[from] Stealth Rock
|move|p1a: wundury|Thunder Wave|p2a: Amoonguss
|-status|p2a: Amoonguss|par
|
|-heal|p2a: Amoonguss|404\\/431 par|[from] item: Black Sludge
|upkeep
|turn|27


|
|move|p1a: wundury|Hidden Power|p2a: Amoonguss
|-supereffective|p2a: Amoonguss
|-damage|p2a: Amoonguss|225\\/431 par
|-damage|p1a: wundury|71\\/100|[from] item: Life Orb
|move|p2a: Amoonguss|Spore|p1a: wundury
|-status|p1a: wundury|slp|[from] move: Spore
|
|-heal|p2a: Amoonguss|251\\/431 par|[from] item: Black Sludge
|upkeep
|turn|28


|
|switch|p2a: Clefable|Clefable, F|394\\/394
|cant|p1a: wundury|slp
|
|upkeep
|turn|29


|
|cant|p1a: wundury|slp
|move|p2a: Clefable|Calm Mind|p2a: Clefable
|-boost|p2a: Clefable|spa|1
|-boost|p2a: Clefable|spd|1
|
|upkeep
|turn|30


|l| eviolitemachop


|
|-curestatus|p1a: wundury|slp|[msg]
|move|p1a: wundury|Thunder Wave|p2a: Clefable
|-status|p2a: Clefable|par
|move|p2a: Clefable|Calm Mind|p2a: Clefable
|-boost|p2a: Clefable|spa|1
|-boost|p2a: Clefable|spd|1
|
|upkeep
|turn|31


|l| pk slam


|j| eviolitemachop


|
|move|p1a: wundury|Taunt|p2a: Clefable
|-start|p2a: Clefable|move: Taunt
|move|p2a: Clefable|Moonblast|p1a: wundury
|-damage|p1a: wundury|0 fnt
|faint|p1a: wundury
|
|upkeep


|
|switch|p1a: surprisemf|Suicune|100\\/100
|-ability|p1a: surprisemf|Pressure
|turn|32


|
|move|p1a: surprisemf|Hydro Pump|p2a: Clefable
|-damage|p2a: Clefable|324\\/394 par
|cant|p2a: Clefable|par
|
|-heal|p2a: Clefable|348\\/394 par|[from] item: Leftovers
|upkeep
|turn|33


|
|move|p1a: surprisemf|Calm Mind|p1a: surprisemf
|-boost|p1a: surprisemf|spa|1
|-boost|p1a: surprisemf|spd|1
|move|p2a: Clefable|Moonblast|p1a: surprisemf
|-damage|p1a: surprisemf|65\\/100
|
|-heal|p1a: surprisemf|71\\/100|[from] item: Leftovers
|-heal|p2a: Clefable|372\\/394 par|[from] item: Leftovers
|-end|p2a: Clefable|move: Taunt
|upkeep
|turn|34


|
|move|p1a: surprisemf|Calm Mind|p1a: surprisemf
|-boost|p1a: surprisemf|spa|1
|-boost|p1a: surprisemf|spd|1
|cant|p2a: Clefable|par
|
|-heal|p1a: surprisemf|78\\/100|[from] item: Leftovers
|-heal|p2a: Clefable|394\\/394 par|[from] item: Leftovers
|upkeep
|turn|35


|
|move|p1a: surprisemf|Calm Mind|p1a: surprisemf
|-boost|p1a: surprisemf|spa|1
|-boost|p1a: surprisemf|spd|1
|move|p2a: Clefable|Thunder Wave|p1a: surprisemf
|-status|p1a: surprisemf|par
|
|-heal|p1a: surprisemf|84\\/100 par|[from] item: Leftovers
|upkeep
|turn|36


|
|move|p1a: surprisemf|Calm Mind|p1a: surprisemf
|-boost|p1a: surprisemf|spa|1
|-boost|p1a: surprisemf|spd|1
|move|p2a: Clefable|Calm Mind|p2a: Clefable
|-boost|p2a: Clefable|spa|1
|-boost|p2a: Clefable|spd|1
|
|-heal|p1a: surprisemf|90\\/100 par|[from] item: Leftovers
|upkeep
|turn|37


|
|move|p1a: surprisemf|Calm Mind|p1a: surprisemf
|-boost|p1a: surprisemf|spa|1
|-boost|p1a: surprisemf|spd|1
|move|p2a: Clefable|Calm Mind|p2a: Clefable
|-boost|p2a: Clefable|spa|1
|-boost|p2a: Clefable|spd|1
|
|-heal|p1a: surprisemf|96\\/100 par|[from] item: Leftovers
|upkeep
|turn|38


|
|cant|p1a: surprisemf|par
|move|p2a: Clefable|Calm Mind|p2a: Clefable
|-boost|p2a: Clefable|spa|1
|-boost|p2a: Clefable|spd|1
|
|-heal|p1a: surprisemf|100\\/100 par|[from] item: Leftovers
|upkeep
|turn|39


|
|move|p1a: surprisemf|Calm Mind|p1a: surprisemf
|-boost|p1a: surprisemf|spa|1
|-boost|p1a: surprisemf|spd|1
|move|p2a: Clefable|Calm Mind|p2a: Clefable
|-boost|p2a: Clefable|spa|1
|-boost|p2a: Clefable|spd|1
|
|upkeep
|turn|40


|
|move|p1a: surprisemf|Hydro Pump|p2a: Clefable|[miss]
|-miss|p1a: surprisemf|p2a: Clefable
|move|p2a: Clefable|Moonblast|p1a: surprisemf
|-damage|p1a: surprisemf|72\\/100 par
|
|-heal|p1a: surprisemf|79\\/100 par|[from] item: Leftovers
|upkeep
|turn|41


|
|cant|p1a: surprisemf|par
|move|p2a: Clefable|Calm Mind|p2a: Clefable
|-boost|p2a: Clefable|spa|0
|-boost|p2a: Clefable|spd|0
|
|-heal|p1a: surprisemf|85\\/100 par|[from] item: Leftovers
|upkeep
|turn|42


|
|cant|p1a: surprisemf|par
|move|p2a: Clefable|Calm Mind|p2a: Clefable
|-boost|p2a: Clefable|spa|0
|-boost|p2a: Clefable|spd|0
|
|-heal|p1a: surprisemf|91\\/100 par|[from] item: Leftovers
|upkeep
|turn|43


|
|cant|p1a: surprisemf|par
|move|p2a: Clefable|Calm Mind|p2a: Clefable
|-boost|p2a: Clefable|spa|0
|-boost|p2a: Clefable|spd|0
|
|-heal|p1a: surprisemf|97\\/100 par|[from] item: Leftovers
|upkeep
|turn|44


|
|move|p1a: surprisemf|Ice Beam|p2a: Clefable
|-damage|p2a: Clefable|321\\/394 par
|move|p2a: Clefable|Calm Mind|p2a: Clefable
|-boost|p2a: Clefable|spa|0
|-boost|p2a: Clefable|spd|0
|
|-heal|p1a: surprisemf|100\\/100 par|[from] item: Leftovers
|-heal|p2a: Clefable|345\\/394 par|[from] item: Leftovers
|upkeep
|turn|45


|
|move|p1a: surprisemf|Hydro Pump|p2a: Clefable
|-damage|p2a: Clefable|206\\/394 par
|move|p2a: Clefable|Moonblast|p1a: surprisemf
|-damage|p1a: surprisemf|71\\/100 par
|-unboost|p1a: surprisemf|spa|1
|
|-heal|p1a: surprisemf|78\\/100 par|[from] item: Leftovers
|-heal|p2a: Clefable|230\\/394 par|[from] item: Leftovers
|upkeep
|turn|46


|
|cant|p1a: surprisemf|par
|move|p2a: Clefable|Moonblast|p1a: surprisemf
|-damage|p1a: surprisemf|50\\/100 par
|
|-heal|p1a: surprisemf|56\\/100 par|[from] item: Leftovers
|-heal|p2a: Clefable|254\\/394 par|[from] item: Leftovers
|upkeep
|turn|47


|
|move|p1a: surprisemf|Hydro Pump|p2a: Clefable
|-damage|p2a: Clefable|136\\/394 par
|move|p2a: Clefable|Moonblast|p1a: surprisemf
|-damage|p1a: surprisemf|30\\/100 par
|
|-heal|p1a: surprisemf|36\\/100 par|[from] item: Leftovers
|-heal|p2a: Clefable|160\\/394 par|[from] item: Leftovers
|upkeep
|turn|48


|
|cant|p1a: surprisemf|par
|move|p2a: Clefable|Moonblast|p1a: surprisemf
|-damage|p1a: surprisemf|10\\/100 par
|
|-heal|p1a: surprisemf|16\\/100 par|[from] item: Leftovers
|-heal|p2a: Clefable|184\\/394 par|[from] item: Leftovers
|upkeep
|turn|49


|
|move|p1a: surprisemf|Hydro Pump|p2a: Clefable
|-damage|p2a: Clefable|54\\/394 par
|move|p2a: Clefable|Moonblast|p1a: surprisemf
|-damage|p1a: surprisemf|0 fnt
|faint|p1a: surprisemf
|
|-heal|p2a: Clefable|78\\/394 par|[from] item: Leftovers
|upkeep


|
|switch|p1a: Oopsie|Uxie|46\\/100 par
|turn|50


|
|move|p1a: Oopsie|Psyshock|p2a: Clefable
|-damage|p2a: Clefable|6\\/394 par
|cant|p2a: Clefable|par
|
|-heal|p1a: Oopsie|52\\/100 par|[from] item: Leftovers
|-heal|p2a: Clefable|30\\/394 par|[from] item: Leftovers
|upkeep
|turn|51


|c| sid69420|OHHH


|
|move|p1a: Oopsie|Psyshock|p2a: Clefable
|-damage|p2a: Clefable|0 fnt
|faint|p2a: Clefable
|
|-heal|p1a: Oopsie|58\\/100 par|[from] item: Leftovers
|upkeep


|
|switch|p2a: Infernape|Infernape, M|257\\/293
|-damage|p2a: Infernape|221\\/293|[from] Stealth Rock
|turn|52


|
|switch|p1a: jelly-scent|Jellicent, M|38\\/100
|move|p2a: Infernape|Fire Blast|p1a: jelly-scent
|-resisted|p1a: jelly-scent
|-damage|p1a: jelly-scent|14\\/100
|-damage|p2a: Infernape|192\\/293|[from] item: Life Orb
|
|-heal|p1a: jelly-scent|20\\/100|[from] item: Leftovers
|upkeep
|turn|53


|
|move|p2a: Infernape|Grass Knot|p1a: jelly-scent
|-supereffective|p1a: jelly-scent
|-damage|p1a: jelly-scent|0 fnt
|-damage|p2a: Infernape|163\\/293|[from] item: Life Orb
|faint|p1a: jelly-scent
|
|upkeep


|
|switch|p1a: Oopsie|Uxie|58\\/100 par
|turn|54


|
|move|p2a: Infernape|Fire Blast|p1a: Oopsie
|-damage|p1a: Oopsie|10\\/100 par
|-damage|p2a: Infernape|134\\/293|[from] item: Life Orb
|move|p1a: Oopsie|Psyshock|p2a: Infernape
|-supereffective|p2a: Infernape
|-damage|p2a: Infernape|0 fnt
|faint|p2a: Infernape
|
|-heal|p1a: Oopsie|16\\/100 par|[from] item: Leftovers
|upkeep


|
|switch|p2a: Amoonguss|Amoonguss, M|394\\/431 par
|-damage|p2a: Amoonguss|341\\/431 par|[from] Stealth Rock
|turn|55


|
|move|p1a: Oopsie|Psyshock|p2a: Amoonguss
|-supereffective|p2a: Amoonguss
|-crit|p2a: Amoonguss
|-damage|p2a: Amoonguss|123\\/431 par
|move|p2a: Amoonguss|Giga Drain|p1a: Oopsie
|-damage|p1a: Oopsie|0 fnt
|-heal|p2a: Amoonguss|151\\/431 par|[from] drain|[of] p1a: Oopsie
|faint|p1a: Oopsie
|
|win|alishahc


|l| yeeeur


|l| etherealblues


|l| sid69420
</script>
"""




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

conn = connect('/home/ec2-user/Pokemon/pokemon.db')
curs = conn.cursor()

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
	# TODO query db for pokemon HP stat and set hp stat for pokemon
	print("querying for: " + pokactual)
	statement = "SELECT hp FROM pokedex WHERE pokemon=?"
	curs.execute(statement, (pokactual,))
	result = curs.fetchall()
	if not result:
		# TODO figure out how to actual error handle this
		print("couldn't parse pokemon for hp stat: " + pokactual)
		return
	print(result[0][0])
	game.sides[playernum].pokemon[poknickname].name = pokactual

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
			damage(m, game)

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
		# TODO ghost curse

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

conn.close()





	







