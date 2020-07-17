import re
import string
from sqlite3 import connect
from parsefuncs import *
from debugfuncs import *
replay = """
<div class="wrapper replay-wrapper" style="max-width:1180px;margin:0 auto">
<input type="hidden" name="replayid" value="gen5ou-1137095271" />
<div class="battle"></div><div class="battle-log"></div><div class="replay-controls"></div><div class="replay-controls-2"></div>
<h1 style="font-weight:normal;text-align:center"><strong>[Gen 5] OU</strong><br /><a href="http://pokemonshowdown.com/users/sid69420" class="subtle" target="_blank">sid69420</a> vs. <a href="http://pokemonshowdown.com/users/pkash16" class="subtle" target="_blank">pkash16</a></h1>
<script type="text/plain" class="battle-log-data">
|j|pkash16


|player|p1|sid69420|preschooler|


|player|p2|pkash16|psychic|
|teamsize|p1|6
|teamsize|p2|6
|gametype|singles
|gen|5
|tier|[Gen 5] OU
|clearpoke
|poke|p1|Terrakion|item
|poke|p1|Blissey, F|item
|poke|p1|Druddigon, F|item
|poke|p1|Bronzong|item
|poke|p1|Zapdos|item
|poke|p1|Rotom-Wash|item
|poke|p2|Ferrothorn, M|item
|poke|p2|Cofagrigus, F|item
|poke|p2|Kingdra, M|item
|poke|p2|Raikou|item
|poke|p2|Vaporeon, F|item
|poke|p2|Kabutops, M|item
|rule|Species Clause: Limit one of each Pokmon
|rule|OHKO Clause: OHKO moves are banned
|rule|Moody Clause: Moody is banned
|rule|Evasion Moves Clause: Evasion moves are banned
|rule|Endless Battle Clause: Forcing endless battles is banned
|rule|HP Percentage Mod: HP is shown in percentages
|rule|Evasion Abilities Clause: Evasion abilities are banned
|rule|Baton Pass Clause: Limit one Baton Passer, can't pass Spe and other stats simultaneously
|rule|Sleep Clause: Sleep-inducing moves are banned
|rule|Swagger Clause: Swagger is banned
|teampreview


|j| eviolitemachop


|j| kumarde


|j| bloptro


|j| samsarin23


|j| sooperdooperman


|c| kumarde|oh shit


|c| kumarde|sid about to get fucked??


|j| BuruBuri


|j| pkashMoney


|
|start
|switch|p1a: ur mom|Rotom-Wash|294\\/294
|switch|p2a: Raikou|Raikou|100\\/100
|-ability|p2a: Raikou|Pressure
|turn|1


|c| pkashMoney|lets go pkash


|
|move|p2a: Raikou|Thunder Wave|p1a: ur mom
|-status|p1a: ur mom|par
|move|p1a: ur mom|Volt Switch|p2a: Raikou
|-resisted|p2a: Raikou
|-damage|p2a: Raikou|86\\/100


|
|switch|p1a: t-pain|Blissey, F|652\\/652
|
|upkeep
|turn|2


|j| sidsucks


|c| sidsucks|fuck sid


|
|move|p2a: Raikou|Rain Dance|p2a: Raikou
|-weather|RainDance
|move|p1a: t-pain|Heal Bell|p1a: t-pain
|-activate|p1a: t-pain|move: Heal Bell
|-curestatus|p1: ur mom|par|[msg]
|
|-weather|RainDance|[upkeep]
|upkeep
|turn|3


|
|switch|p1a: ur mom|Rotom-Wash|294\\/294
|move|p2a: Raikou|Volt Switch|p1a: ur mom
|-damage|p1a: ur mom|207\\/294


|n| SIMP4PKASH|kumarde


|c| SIMP4PKASH|sup guys


|c| sidsucks|ahh


|c| sidsucks|brotherly love


|c| BuruBuri|the whole gang is here


|
|switch|p2a: angry grandpa|Ferrothorn, M|100\\/100|[from]move: Volt Switch
|
|-weather|RainDance|[upkeep]
|-heal|p1a: ur mom|225\\/294|[from] item: Leftovers
|upkeep
|turn|4


|
|move|p1a: ur mom|Sunny Day|p1a: ur mom
|-weather|SunnyDay
|move|p2a: angry grandpa|Stealth Rock|p1a: ur mom
|-sidestart|p1: sid69420|move: Stealth Rock
|
|-weather|SunnyDay|[upkeep]
|-heal|p1a: ur mom|243\\/294|[from] item: Leftovers
|upkeep
|turn|5


|
|switch|p2a: Raikou|Raikou|86\\/100
|-ability|p2a: Raikou|Pressure
|move|p1a: ur mom|Hidden Power|p2a: Raikou
|-damage|p2a: Raikou|59\\/100
|
|-weather|SunnyDay|[upkeep]
|-heal|p1a: ur mom|261\\/294|[from] item: Leftovers
|upkeep
|turn|6


|j| sidckoMode


|c| sidckoMode|PKASH


|
|move|p2a: Raikou|Thunder Wave|p1a: ur mom
|-status|p1a: ur mom|par
|move|p1a: ur mom|Thunderbolt|p2a: Raikou
|-resisted|p2a: Raikou
|-damage|p2a: Raikou|41\\/100
|
|-weather|SunnyDay|[upkeep]
|-heal|p1a: ur mom|279\\/294 par|[from] item: Leftovers
|upkeep
|turn|7


|c| sidckoMode|MORE LIKE PEE ASS


|
|move|p2a: Raikou|Rain Dance|p2a: Raikou
|-weather|RainDance
|move|p1a: ur mom|Volt Switch|p2a: Raikou
|-resisted|p2a: Raikou
|-damage|p2a: Raikou|27\\/100


|c| sidckoMode|RAIKOU


|c| SIMP4PKASH|sid: "yeah, I sent this link to the hillbillies"


|c| sidckoMode|MORE LIKE I DONT LIKE YOU


|
|switch|p1a: t-pain|Blissey, F|652\\/652
|-damage|p1a: t-pain|571\\/652|[from] Stealth Rock
|
|-weather|RainDance|[upkeep]
|-heal|p1a: t-pain|611\\/652|[from] item: Leftovers
|upkeep
|turn|8


|
|move|p2a: Raikou|Volt Switch|p1a: t-pain
|-damage|p1a: t-pain|550\\/652


|c| sidsucks|lollll


|
|switch|p2a: sid|Kingdra, M|100\\/100|[from]move: Volt Switch
|move|p1a: t-pain|Heal Bell|p1a: t-pain
|-activate|p1a: t-pain|move: Heal Bell
|-curestatus|p1: ur mom|par|[msg]
|
|-weather|RainDance|[upkeep]
|-heal|p1a: t-pain|590\\/652|[from] item: Leftovers
|upkeep
|turn|9


|c| sidckoMode|uh... guys?


|c| sidckoMode|pkash just dm'd me something kinda racist


|c| sidckoMode|should I report him?


|c| SIMP4PKASH|:O


|
|move|p2a: sid|Outrage|p1a: t-pain
|-damage|p1a: t-pain|64\\/652
|move|p1a: t-pain|Seismic Toss|p2a: sid
|-damage|p2a: sid|66\\/100
|
|-weather|RainDance|[upkeep]
|-heal|p1a: t-pain|104\\/652|[from] item: Leftovers
|upkeep
|turn|10


|c| SIMP4PKASH|yeah definitely


|c|pkash16|pics or didn't happen

|raw|<font size="1"><\\/font>


|
|switch|p1a: rick ross|Bronzong|338\\/338
|-damage|p1a: rick ross|317\\/338|[from] Stealth Rock
|move|p2a: sid|Outrage|p1a: rick ross|[from]lockedmove
|-resisted|p1a: rick ross
|-damage|p1a: rick ross|231\\/338
|
|-weather|RainDance|[upkeep]
|-heal|p1a: rick ross|252\\/338|[from] item: Leftovers
|upkeep
|turn|11


|
|move|p2a: sid|Outrage|p1a: rick ross|[from]lockedmove
|-resisted|p1a: rick ross
|-damage|p1a: rick ross|167\\/338
|-start|p2a: sid|confusion|[fatigue]
|move|p1a: rick ross|Stealth Rock|p2a: sid
|-sidestart|p2: pkash16|move: Stealth Rock
|
|-weather|RainDance|[upkeep]
|-heal|p1a: rick ross|188\\/338|[from] item: Leftovers
|upkeep
|turn|12


|l| eviolitemachop


|j| eviolitemachop


|
|switch|p2a: angry grandpa|Ferrothorn, M|100\\/100
|-damage|p2a: angry grandpa|94\\/100|[from] Stealth Rock
|move|p1a: rick ross|Reflect|p1a: rick ross
|-sidestart|p1: sid69420|Reflect
|
|-weather|RainDance|[upkeep]
|-heal|p1a: rick ross|209\\/338|[from] item: Leftovers
|-heal|p2a: angry grandpa|100\\/100|[from] item: Leftovers
|upkeep
|turn|13

|error|[Invalid choice] There's nothing to cancel

|
|switch|p1a: ur mom|Rotom-Wash|279\\/294
|-damage|p1a: ur mom|243\\/294|[from] Stealth Rock
|move|p2a: angry grandpa|Spikes|p1a: ur mom
|-sidestart|p1: sid69420|Spikes
|
|-weather|RainDance|[upkeep]
|-heal|p1a: ur mom|261\\/294|[from] item: Leftovers
|upkeep
|turn|14


|
|move|p1a: ur mom|Sunny Day|p1a: ur mom
|-weather|SunnyDay
|move|p2a: angry grandpa|Spikes|p1a: ur mom
|-sidestart|p1: sid69420|Spikes
|
|-weather|SunnyDay|[upkeep]
|-heal|p1a: ur mom|279\\/294|[from] item: Leftovers
|upkeep
|turn|15


|l| eviolitemachop


|j| eviolitemachop



|c| sidckoMode|add imgur.


|c| sidckoMode|I cant send links


|c| SIMP4PKASH|damn


|c| SIMP4PKASH|he's so racist


|
|move|p1a: ur mom|Hidden Power|p2a: angry grandpa
|-supereffective|p2a: angry grandpa
|-damage|p2a: angry grandpa|10\\/100
|move|p2a: angry grandpa|Leech Seed|p1a: ur mom
|-start|p1a: ur mom|move: Leech Seed
|
|-weather|SunnyDay|[upkeep]
|-heal|p1a: ur mom|294\\/294|[from] item: Leftovers
|-heal|p2a: angry grandpa|16\\/100|[from] item: Leftovers
|-damage|p1a: ur mom|258\\/294|[from] Leech Seed|[of] p2a: angry grandpa
|-heal|p2a: angry grandpa|26\\/100|[silent]
|upkeep
|turn|16


|c| sidckoMode|ooooooooooooooooooooooooooooooooooooo


|
|move|p1a: ur mom|Hidden Power|p2a: angry grandpa
|-supereffective|p2a: angry grandpa
|-damage|p2a: angry grandpa|0 fnt
|faint|p2a: angry grandpa
|
|-weather|SunnyDay|[upkeep]
|-heal|p1a: ur mom|276\\/294|[from] item: Leftovers
|-sideend|p1: sid69420|Reflect
|upkeep


|
|switch|p2a: Raikou|Raikou|27\\/100
|-damage|p2a: Raikou|15\\/100|[from] Stealth Rock
|-ability|p2a: Raikou|Pressure
|turn|17


|
|move|p2a: Raikou|Rain Dance|p2a: Raikou
|-weather|RainDance
|move|p1a: ur mom|Hidden Power|p2a: Raikou
|-damage|p2a: Raikou|5\\/100
|
|-weather|RainDance|[upkeep]
|-heal|p1a: ur mom|294\\/294|[from] item: Leftovers
|-damage|p1a: ur mom|258\\/294|[from] Leech Seed|[of] p2a: Raikou
|-heal|p2a: Raikou|15\\/100|[silent]
|upkeep
|turn|18


|c| SIMP4PKASH|raikou wall


|c| sidsucks|is rotom a washing machine


|c| sidsucks|or a drier


|c| sidsucks|lol


|c| SIMP4PKASH|washing machine I think


|c| sidckoMode|wash


|
|move|p2a: Raikou|Thunder Wave|p1a: ur mom
|-status|p1a: ur mom|par
|move|p1a: ur mom|Thunderbolt|p2a: Raikou
|-resisted|p2a: Raikou
|-damage|p2a: Raikou|0 fnt
|faint|p2a: Raikou
|
|-weather|RainDance|[upkeep]
|-heal|p1a: ur mom|276\\/294 par|[from] item: Leftovers
|upkeep


|c| sidckoMode|what dryer has water


|c| sidsucks|which one is the drier


|c| sidckoMode|none


|c| SIMP4PKASH|rotom-heat is a drying machine


|c| sidsucks|lmfao


|c| sidckoMode|rotom wash has a big schlong


|c| sidsucks|is sid a moron or a dumbo


|c| SIMP4PKASH|Sid stans are really... into pokemon


|
|switch|p2a: vaporwave|Vaporeon, F|100\\/100
|-damage|p2a: vaporwave|88\\/100|[from] Stealth Rock
|turn|19


|c| sidsucks|jk


|c| sidckoMode|Im really into sid


|c| sidckoMode|I think about him a lot


|
|move|p2a: vaporwave|Hydro Pump|p1a: ur mom
|-resisted|p1a: ur mom
|-damage|p1a: ur mom|91\\/294 par
|-damage|p2a: vaporwave|78\\/100|[from] item: Life Orb
|cant|p1a: ur mom|par
|
|-weather|RainDance|[upkeep]
|-heal|p1a: ur mom|109\\/294 par|[from] item: Leftovers
|-damage|p1a: ur mom|73\\/294 par|[from] Leech Seed|[of] p2a: vaporwave
|-heal|p2a: vaporwave|86\\/100|[silent]
|upkeep
|turn|20


|c| sidckoMode|vaporwave? nice name


|c| sidckoMode|sike


|
|switch|p1a: t-pain|Blissey, F|104\\/652
|-damage|p1a: t-pain|0 fnt|[from] Spikes
|faint|p1a: t-pain
|move|p2a: vaporwave|Hydro Pump|p1: t-pain|[notarget]
|-fail|p2a: vaporwave
|
|-weather|RainDance|[upkeep]
|upkeep


|
|switch|p1a: zaptres|Zapdos|384\\/384
|-damage|p1a: zaptres|288\\/384|[from] Stealth Rock
|-ability|p1a: zaptres|Pressure
|turn|21


|c| SIMP4PKASH|thunder??


|c| sidckoMode|big thunder on the way


|c| SIMP4PKASH|un real


|c| sidckoMode|simp4pkash did you attend oxford university?


|c| sidckoMode|at any point


|c| BuruBuri|yes he was my roomate at oxford


|c| BuruBuri|for grad school


|c| bloptro|He was my lover at oxford


|c| SIMP4PKASH|I'm more of a cambridge fellow myself


|c| bloptro|and also my TA :O


|c| SIMP4PKASH|cambridge college in boston aha


|
|move|p1a: zaptres|Thunderbolt|p2a: vaporwave
|-supereffective|p2a: vaporwave
|-damage|p2a: vaporwave|29\\/100
|move|p2a: vaporwave|Hydro Pump|p1a: zaptres
|-damage|p1a: zaptres|0 fnt
|-damage|p2a: vaporwave|19\\/100|[from] item: Life Orb
|faint|p1a: zaptres
|
|-weather|RainDance|[upkeep]
|upkeep


|
|switch|p1a: 6-0 god|Terrakion|323\\/323
|-damage|p1a: 6-0 god|270\\/323|[from] Spikes
|-damage|p1a: 6-0 god|250\\/323|[from] Stealth Rock
|turn|22


|
|switch|p2a: mummy|Cofagrigus, F|100\\/100
|-damage|p2a: mummy|88\\/100|[from] Stealth Rock
|move|p1a: 6-0 god|Earthquake|p2a: mummy
|-damage|p2a: mummy|57\\/100
|
|-weather|RainDance|[upkeep]
|upkeep
|turn|23


|
|switch|p1a: deepak|Druddigon, F|358\\/358
|-damage|p1a: deepak|314\\/358|[from] Stealth Rock
|-damage|p1a: deepak|255\\/358|[from] Spikes
|move|p2a: mummy|Shadow Ball|p1a: deepak
|-damage|p1a: deepak|152\\/358
|
|-weather|RainDance|[upkeep]
|-heal|p1a: deepak|174\\/358|[from] item: Leftovers
|upkeep
|turn|24


|c| sidckoMode|pkash


|c| sidckoMode|more like penis


|
|move|p1a: deepak|Crunch|p2a: mummy
|-supereffective|p2a: mummy
|-damage|p2a: mummy|13\\/100
|-activate|p2a: mummy|ability: Mummy|Sheer Force|[of] p1a: deepak
|move|p2a: mummy|Will-O-Wisp|p1a: deepak
|-status|p1a: deepak|brn
|
|-weather|none
|-heal|p1a: deepak|196\\/358 brn|[from] item: Leftovers
|-damage|p1a: deepak|152\\/358 brn|[from] brn
|upkeep
|turn|25


|c| BuruBuri|clever sidko


|c| sidckoMode|buruburi


|c| sidckoMode|more like


|c| sidckoMode|bootybooty


|c| BuruBuri|yeah, and?


|c| sidckoMode|um..


|c| BuruBuri|get fucked


|c| sidsucks|yea sid you use that damage calculator


|c| sidckoMode|uhhh..


|c| sidckoMode|shoot


|c| SIMP4PKASH|sid?


|c| SIMP4PKASH|more like suck


|c| sidckoMode|damn


|c| sidsucks|damn


|c| sidckoMode|sids a nice guy


|c| sidckoMode|so humble


|c| sidsucks|sit down...


|c| sidsucks|be humble!


|c| sidckoMode|-Sid


|c| SIMP4PKASH|sid down


|c| SIMP4PKASH|join bumble


|c| SIMP4PKASH|sidrick lamar


|c| sidckoMode|DAMN


|
|move|p1a: deepak|Crunch|p2a: mummy
|-supereffective|p2a: mummy
|-damage|p2a: mummy|0 fnt
|faint|p2a: mummy
|
|-heal|p1a: deepak|174\\/358 brn|[from] item: Leftovers
|-damage|p1a: deepak|130\\/358 brn|[from] brn
|upkeep


|c| sidckoMode|anyone wanna play hangman


|c| sidckoMode|_ _ _ _      _ _ _


|c| sidckoMode|should be a space


|
|switch|p2a: ROCKY HELMET|Kabutops, M|100\\/100
|-damage|p2a: ROCKY HELMET|88\\/100|[from] Stealth Rock
|turn|26


|c| sidckoMode|_ _ _ _


|c| sidckoMode|_ _ _


|c| sidsucks|rascism


|c| sidsucks|aqua


|c| sidsucks|jet


|c| sidsucks|i win


|c| sidckoMode|you can guess a letter


|c| sidsucks|i did


|c| sidsucks|awua


|
|move|p2a: ROCKY HELMET|Waterfall|p1a: deepak
|-resisted|p1a: deepak
|-damage|p1a: deepak|22\\/358 brn
|-activate|p1a: deepak|ability: Mummy|Swift Swim|[of] p2a: ROCKY HELMET
|move|p1a: deepak|Thunder Punch|p2a: ROCKY HELMET
|-supereffective|p2a: ROCKY HELMET
|-crit|p2a: ROCKY HELMET
|-damage|p2a: ROCKY HELMET|17\\/100
|
|-heal|p1a: deepak|44\\/358 brn|[from] item: Leftovers
|-damage|p1a: deepak|0 fnt|[from] brn
|faint|p1a: deepak
|upkeep


|c| sidsucks|aqua


|c| sidsucks|jet


|c| sidckoMode|sorry pal


|c| sidsucks|f


|
|switch|p1a: rick ross|Bronzong|209\\/338
|-damage|p1a: rick ross|188\\/338|[from] Stealth Rock
|turn|27


|c| sidckoMode|rocky helmet


|c| sidckoMode|more like


|c| sidckoMode|cock me? hell yes


|c| SIMP4PKASH|really stretching the rhyming here but


|c| sidsucks|my name is sid


|c| SIMP4PKASH|i'll allow it


|c| sidsucks|and i like oombies


|c| sidsucks|boobies


|
|switch|p2a: sid|Kingdra, M|66\\/100
|-damage|p2a: sid|54\\/100|[from] Stealth Rock
|move|p1a: rick ross|Psychic|p2a: sid
|-damage|p2a: sid|20\\/100
|
|-heal|p1a: rick ross|209\\/338|[from] item: Leftovers
|upkeep
|turn|28


|c| SIMP4PKASH|rocky helmet? more like cock me, hell yes


|c| SIMP4PKASH|hahaha


|c| sidckoMode|simp4pkash needs to close his old battles


|c| SIMP4PKASH|thak you


|
|move|p2a: sid|Rain Dance|p2a: sid
|-weather|RainDance
|move|p1a: rick ross|Psychic|p2a: sid
|-damage|p2a: sid|0 fnt
|faint|p2a: sid
|
|-weather|RainDance|[upkeep]
|-heal|p1a: rick ross|230\\/338|[from] item: Leftovers
|upkeep


|
|switch|p2a: vaporwave|Vaporeon, F|19\\/100
|-damage|p2a: vaporwave|7\\/100|[from] Stealth Rock
|turn|29


|c|sid69420|what the fuck


|c| sidckoMode|what the fuck


|c| SIMP4PKASH|holy fuck


|
|switch|p1a: ur mom|Rotom-Wash|73\\/294 par
|-damage|p1a: ur mom|37\\/294 par|[from] Stealth Rock
|move|p2a: vaporwave|Rest|p2a: vaporwave
|-status|p2a: vaporwave|slp|[from] move: Rest
|-heal|p2a: vaporwave|100\\/100 slp|[silent]
|
|-weather|RainDance|[upkeep]
|-activate|p2a: vaporwave|ability: Hydration
|-curestatus|p2a: vaporwave|slp|[msg]
|-heal|p1a: ur mom|55\\/294 par|[from] item: Leftovers
|upkeep
|turn|30


|c|sid69420|oh my god


|c| pkashMoney|gg


|c| SIMP4PKASH|holy fuck


|c| sidckoMode|bruh


|c|sid69420|oh my god


|c| sidckoMode|bruh


|c| sidckoMode|oh my god


|
|move|p2a: vaporwave|Hydro Pump|p1a: ur mom|[miss]
|-miss|p2a: vaporwave|p1a: ur mom
|cant|p1a: ur mom|par
|
|-weather|RainDance|[upkeep]
|-heal|p1a: ur mom|73\\/294 par|[from] item: Leftovers
|upkeep
|turn|31


|c| SIMP4PKASH|hOLY FHIST


|c| SIMP4PKASH|WOW


|
|move|p2a: vaporwave|Hydro Pump|p1a: ur mom|[miss]
|-miss|p2a: vaporwave|p1a: ur mom
|move|p1a: ur mom|Sunny Day|p1a: ur mom
|-weather|SunnyDay
|
|-weather|SunnyDay|[upkeep]
|-heal|p1a: ur mom|91\\/294 par|[from] item: Leftovers
|upkeep
|turn|32


|c| sidckoMode|lol


|c| SIMP4PKASH|holy shiiiit


|c| sidckoMode|the virgin rain vs the chad sun


|
|move|p2a: vaporwave|Hydro Pump|p1a: ur mom
|-resisted|p1a: ur mom
|-damage|p1a: ur mom|22\\/294 par
|-damage|p2a: vaporwave|91\\/100|[from] item: Life Orb
|move|p1a: ur mom|Thunderbolt|p2a: vaporwave
|-supereffective|p2a: vaporwave
|-crit|p2a: vaporwave
|-damage|p2a: vaporwave|0 fnt
|faint|p2a: vaporwave
|
|-weather|SunnyDay|[upkeep]
|-heal|p1a: ur mom|40\\/294 par|[from] item: Leftovers
|upkeep


|c| sidckoMode|the crit


|
|switch|p2a: ROCKY HELMET|Kabutops, M|17\\/100
|-damage|p2a: ROCKY HELMET|5\\/100|[from] Stealth Rock
|turn|33


|c| sidckoMode|hot af


|
|move|p2a: ROCKY HELMET|Aqua Jet|p1a: ur mom
|-resisted|p1a: ur mom
|-damage|p1a: ur mom|19\\/294 par
|cant|p1a: ur mom|par
|
|-weather|SunnyDay|[upkeep]
|-heal|p1a: ur mom|37\\/294 par|[from] item: Leftovers
|upkeep
|turn|34


|c| SIMP4PKASH|wow


|
|move|p2a: ROCKY HELMET|Aqua Jet|p1a: ur mom
|-resisted|p1a: ur mom
|-damage|p1a: ur mom|16\\/294 par
|move|p1a: ur mom|Volt Switch|p2a: ROCKY HELMET
|-supereffective|p2a: ROCKY HELMET
|-damage|p2a: ROCKY HELMET|0 fnt
|faint|p2a: ROCKY HELMET
|
|win|sid69420


|c| SIMP4PKASH|what a crazy game


|l| BuruBuri


|c| sidckoMode|<3
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

		# key is int [1, 2], value is side object
		self.sides = dict()
		self.sides['1'] = Side()
		self.sides['2'] = Side()





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
	game.sides[m.group(1)].pokemon[m.group(2)] = Pokemon()
	# TODO query db for pokemon HP stat and set hp stat for pokemon
	game.sides[m.group(1)].pokemon[m.group(2)].name = m.group(3)

# get first 2 pokemon
startp1pok = re.search(r'(?<=\|switch\|p1a: )([^\|]+)\|([^\|,]+)', replay).group(1)
startp2pok = re.search(r'(?<=\|switch\|p2a: )([^\|]+)\|([^\|,]+)', replay).group(1)

game.sides['1'].activepok = startp1pok
game.sides['2'].activepok = startp2pok

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
		if re.search(r'(?<=-sidestart\|p([0-9]):)', line) != None:
			m = re.search(r'(?<=-sidestart\|p([0-9]):)', line)
			# print("matched hazards")
			# # group 1 is the player num the hazards are now on
			# print(m.group(1))
			# # TODO need to match to type of hazard

		# if hazards end
		if re.search(r'(?<=-sideend\|p([0-9]):)', line) != None:
			m = re.search(r'(?<=-sideend\|p([0-9]):)', line)
			# TODO need to match to type of hazard
			# group 1 is the player num the hazards are cleared from

		# if weather starts (sandstorm or hail)

		# if weather ends
		# TODO check to see if works
		if re.search(r'-weather\|none', line) != None:
			# remove this line
			m = re.search(r'-weather\|none', line)

		# if poison or burn or tox starts
		# TODO check to see if works
		#|-status|p1a: ur mom|par
		if re.search(r'(?<=-status\|p([0-9])a: )([^\|]+)\|(.*)', line) != None:
			# check for tox or burn or psn
			m = re.search(r'(?<=-status\|p([0-9])a: )([^\|]+)\|(.*)', line)
			print("found status")
			# player num
			#print(m.group(1))
			# nickname of pokemon that is statused
			#print(m.group(2))
			# status info
			#print(m.group(3))
			#status_start(m, game)

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

		# TODO increment active turns for pokemon that are alive

# increment appearance value in db for all pokemon in p1pok and p2pok

# get actual player names, calculate score and return stats








	







