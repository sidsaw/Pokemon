import re
import string
replay = """
<!DOCTYPE html>
<meta charset="utf-8" />
<!-- version 1 -->
<title>[Gen 5] OU replay: eviolitemachop vs. samsarin23</title>
<style>
html,body {font-family:Verdana, sans-serif;font-size:10pt;margin:0;padding:0;}body{padding:12px 0;} .battle-log {font-family:Verdana, sans-serif;font-size:10pt;} .battle-log-inline {border:1px solid #AAAAAA;background:#EEF2F5;color:black;max-width:640px;margin:0 auto 80px;padding-bottom:5px;} .battle-log .inner {padding:4px 8px 0px 8px;} .battle-log .inner-preempt {padding:0 8px 4px 8px;} .battle-log .inner-after {margin-top:0.5em;} .battle-log h2 {margin:0.5em -8px;padding:4px 8px;border:1px solid #AAAAAA;background:#E0E7EA;border-left:0;border-right:0;font-family:Verdana, sans-serif;font-size:13pt;} .battle-log .chat {vertical-align:middle;padding:3px 0 3px 0;font-size:8pt;} .battle-log .chat strong {color:#40576A;} .battle-log .chat em {padding:1px 4px 1px 3px;color:#000000;font-style:normal;} .chat.mine {background:rgba(0,0,0,0.05);margin-left:-8px;margin-right:-8px;padding-left:8px;padding-right:8px;} .spoiler {color:#BBBBBB;background:#BBBBBB;padding:0px 3px;} .spoiler:hover, .spoiler:active, .spoiler-shown {color:#000000;background:#E2E2E2;padding:0px 3px;} .spoiler a {color:#BBBBBB;} .spoiler:hover a, .spoiler:active a, .spoiler-shown a {color:#2288CC;} .chat code, .chat .spoiler:hover code, .chat .spoiler:active code, .chat .spoiler-shown code {border:1px solid #C0C0C0;background:#EEEEEE;color:black;padding:0 2px;} .chat .spoiler code {border:1px solid #CCCCCC;background:#CCCCCC;color:#CCCCCC;} .battle-log .rated {padding:3px 4px;} .battle-log .rated strong {color:white;background:#89A;padding:1px 4px;border-radius:4px;} .spacer {margin-top:0.5em;} .message-announce {background:#6688AA;color:white;padding:1px 4px 2px;} .message-announce a, .broadcast-green a, .broadcast-blue a, .broadcast-red a {color:#DDEEFF;} .broadcast-green {background-color:#559955;color:white;padding:2px 4px;} .broadcast-blue {background-color:#6688AA;color:white;padding:2px 4px;} .infobox {border:1px solid #6688AA;padding:2px 4px;} .infobox-limited {max-height:200px;overflow:auto;overflow-x:hidden;} .broadcast-red {background-color:#AA5544;color:white;padding:2px 4px;} .message-learn-canlearn {font-weight:bold;color:#228822;text-decoration:underline;} .message-learn-cannotlearn {font-weight:bold;color:#CC2222;text-decoration:underline;} .message-effect-weak {font-weight:bold;color:#CC2222;} .message-effect-resist {font-weight:bold;color:#6688AA;} .message-effect-immune {font-weight:bold;color:#666666;} .message-learn-list {margin-top:0;margin-bottom:0;} .message-throttle-notice, .message-error {color:#992222;} .message-overflow, .chat small.message-overflow {font-size:0pt;} .message-overflow::before {font-size:9pt;content:'...';} .subtle {color:#3A4A66;}
</style>
<div class="wrapper replay-wrapper" style="max-width:1180px;margin:0 auto">
<input type="hidden" name="replayid" value="gen5ou-1122450180" />
<div class="battle"></div><div class="battle-log"></div><div class="replay-controls"></div><div class="replay-controls-2"></div>
<h1 style="font-weight:normal;text-align:center"><strong>[Gen 5] OU</strong><br /><a href="http://pokemonshowdown.com/users/eviolitemachop" class="subtle" target="_blank">eviolitemachop</a> vs. <a href="http://pokemonshowdown.com/users/samsarin23" class="subtle" target="_blank">samsarin23</a></h1>
<script type="text/plain" class="battle-log-data">|j|eviolitemachop
|j|samsarin23
|player|p1|eviolitemachop|burglar|
|player|p2|samsarin23|102|
|teamsize|p1|6
|teamsize|p2|6
|gametype|singles
|gen|5
|tier|[Gen 5] OU
|clearpoke
|poke|p1|Volcarona, F|item
|poke|p1|Espeon, F|item
|poke|p1|Starmie|item
|poke|p1|Kyurem-Black|item
|poke|p1|Lucario, M|item
|poke|p1|Weavile, M|item
|poke|p2|Metagross|item
|poke|p2|Latias, F|item
|poke|p2|Keldeo|item
|poke|p2|Forretress, F|item
|poke|p2|Thundurus-Therian, M|item
|poke|p2|Gyarados, M|item
|rule|Species Clause: Limit one of each Pokémon
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
|
|start
|switch|p1a: Espeon|Espeon, F|100\\/100
|switch|p2a: Metacute|Metagross|100\\/100
|turn|1
|
|move|p1a: Espeon|Calm Mind|p1a: Espeon
|-boost|p1a: Espeon|spa|1
|-boost|p1a: Espeon|spd|1
|move|p2a: Metacute|Stealth Rock|p1a: Espeon
|move|p1a: Espeon|Stealth Rock|p2a: Metacute|[from]Magic Bounce
|-sidestart|p2: samsarin23|move: Stealth Rock
|
|upkeep
|turn|2
|j| sooperdooperman
|
|move|p1a: Espeon|Calm Mind|p1a: Espeon
|-boost|p1a: Espeon|spa|1
|-boost|p1a: Espeon|spd|1
|move|p2a: Metacute|Stealth Rock|p1a: Espeon
|move|p1a: Espeon|Stealth Rock||[from]Magic Bounce|[still]
|-fail|p1a: Espeon
|
|upkeep
|turn|3


|j| sid69420


|
|move|p1a: Espeon|Calm Mind|p1a: Espeon
|-boost|p1a: Espeon|spa|1
|-boost|p1a: Espeon|spd|1
|move|p2a: Metacute|Signal Beam|p1a: Espeon
|-supereffective|p1a: Espeon
|-damage|p1a: Espeon|90\\/100
|
|upkeep
|turn|4


|j| pkash16


|
|move|p1a: Espeon|Calm Mind|p1a: Espeon
|-boost|p1a: Espeon|spa|1
|-boost|p1a: Espeon|spd|1
|move|p2a: Metacute|Earthquake|p1a: Espeon
|-damage|p1a: Espeon|31\\/100
|
|upkeep
|turn|5


|
|move|p1a: Espeon|Baton Pass|p1a: Espeon


|
|switch|p1a: Starmie|Starmie|100\\/100|[from]move: Baton Pass
|move|p2a: Metacute|Earthquake|p1a: Starmie
|-damage|p1a: Starmie|50\\/100
|
|upkeep
|turn|6


|
|move|p1a: Starmie|Hydro Pump|p2a: Metacute|[miss]
|-miss|p1a: Starmie|p2a: Metacute
|move|p2a: Metacute|Pursuit|p1a: Starmie
|-supereffective|p1a: Starmie
|-damage|p1a: Starmie|9\\/100
|
|upkeep
|turn|7


|c|eviolitemachop|F


|c|☆violitemachop|i keep missing hydro pumps


|
|move|p1a: Starmie|Hydro Pump|p2a: Metacute|[miss]
|-miss|p1a: Starmie|p2a: Metacute
|move|p2a: Metacute|Stealth Rock|p1a: Starmie
|-sidestart|p1: eviolitemachop|move: Stealth Rock
|
|upkeep
|turn|8


|c|eviolitemachop|LOL


|c|eviolitemachop|gd


|
|move|p1a: Starmie|Hydro Pump|p2a: Metacute
|-crit|p2a: Metacute
|-damage|p2a: Metacute|0 fnt
|-damage|p1a: Starmie|0 fnt|[from] item: Life Orb
|faint|p2a: Metacute
|faint|p1a: Starmie
|
|upkeep


|c|eviolitemachop|finally


|
|switch|p1a: Lucario|Lucario, M|100\\/100
|switch|p2a: Muchachaaaa|Latias, F|100\\/100
|-damage|p2a: Muchachaaaa|88\\/100|[from] Stealth Rock
|-damage|p1a: Lucario|98\\/100|[from] Stealth Rock
|turn|9


|
|switch|p2a: unicorn mf|Keldeo|100\\/100
|-damage|p2a: unicorn mf|94\\/100|[from] Stealth Rock
|switch|p1a: Weavile|Weavile, M|100\\/100
|-damage|p1a: Weavile|76\\/100|[from] Stealth Rock
|-ability|p1a: Weavile|Pressure
|
|upkeep
|turn|10


|
|switch|p1a: Espeon|Espeon, F|31\\/100
|-damage|p1a: Espeon|19\\/100|[from] Stealth Rock
|move|p2a: unicorn mf|Secret Sword|p1a: Espeon
|-resisted|p1a: Espeon
|-damage|p1a: Espeon|0 fnt
|faint|p1a: Espeon
|
|upkeep


|
|switch|p1a: Lucario|Lucario, M|98\\/100
|-damage|p1a: Lucario|95\\/100|[from] Stealth Rock
|turn|11


|
|move|p1a: Lucario|Extreme Speed|p2a: unicorn mf
|-damage|p2a: unicorn mf|55\\/100
|-damage|p1a: Lucario|85\\/100|[from] item: Life Orb
|move|p2a: unicorn mf|Secret Sword|p1a: Lucario
|-supereffective|p1a: Lucario
|-damage|p1a: Lucario|0 fnt
|faint|p1a: Lucario
|
|upkeep


|
|switch|p1a: Volcoronavirus|Volcarona, F, shiny|100\\/100
|-damage|p1a: Volcoronavirus|51\\/100|[from] Stealth Rock
|turn|12


|c|☆eviolitemachop|ow


|
|move|p2a: unicorn mf|Secret Sword|p1a: Volcoronavirus
|-resisted|p1a: Volcoronavirus
|-damage|p1a: Volcoronavirus|17\\/100
|move|p1a: Volcoronavirus|Giga Drain|p2a: unicorn mf
|-supereffective|p2a: unicorn mf
|-damage|p2a: unicorn mf|0 fnt
|-heal|p1a: Volcoronavirus|45\\/100|[from] drain|[of] p2a: unicorn mf
|-damage|p1a: Volcoronavirus|35\\/100|[from] item: Life Orb
|faint|p2a: unicorn mf
|
|upkeep


|
|switch|p2a: Muchachaaaa|Latias, F|88\\/100
|-damage|p2a: Muchachaaaa|76\\/100|[from] Stealth Rock
|turn|13


|
|move|p2a: Muchachaaaa|Draco Meteor|p1a: Volcoronavirus
|-damage|p1a: Volcoronavirus|0 fnt
|-unboost|p2a: Muchachaaaa|spa|2
|-damage|p2a: Muchachaaaa|66\\/100|[from] item: Life Orb
|faint|p1a: Volcoronavirus
|
|upkeep


|
|switch|p1a: Weavile|Weavile, M|76\\/100
|-damage|p1a: Weavile|51\\/100|[from] Stealth Rock
|-ability|p1a: Weavile|Pressure
|turn|14


|
|move|p2a: Muchachaaaa|Hidden Power|p1a: Weavile
|-supereffective|p1a: Weavile
|-damage|p1a: Weavile|10\\/100
|-damage|p2a: Muchachaaaa|56\\/100|[from] item: Life Orb
|move|p1a: Weavile|Pursuit|p2a: Muchachaaaa
|-supereffective|p2a: Muchachaaaa
|-damage|p2a: Muchachaaaa|0 fnt
|-damage|p1a: Weavile|0 fnt|[from] item: Life Orb
|faint|p2a: Muchachaaaa
|faint|p1a: Weavile
|
|upkeep


|
|switch|p1a: Kyurem|Kyurem-Black, shiny|100\\/100
|switch|p2a: Thundurus-Wundurus|Thundurus-Therian, M|100\\/100
|-damage|p1a: Kyurem|76\\/100|[from] Stealth Rock
|-ability|p1a: Kyurem|Teravolt
|-damage|p2a: Thundurus-Wundurus|76\\/100|[from] Stealth Rock
|turn|15


|
|move|p1a: Kyurem|Outrage|p2a: Thundurus-Wundurus
|-crit|p2a: Thundurus-Wundurus
|-damage|p2a: Thundurus-Wundurus|0 fnt
|faint|p2a: Thundurus-Wundurus
|
|upkeep


|
|switch|p2a: Fortnitetress|Forretress, F|100\\/100
|-damage|p2a: Fortnitetress|88\\/100|[from] Stealth Rock
|turn|16


|
|move|p1a: Kyurem|Outrage|p2a: Fortnitetress|[from]lockedmove
|-resisted|p2a: Fortnitetress
|-damage|p2a: Fortnitetress|56\\/100
|-start|p1a: Kyurem|confusion|[fatigue]
|move|p2a: Fortnitetress|Gyro Ball|p1a: Kyurem
|-supereffective|p1a: Kyurem
|-damage|p1a: Kyurem|19\\/100
|
|-heal|p2a: Fortnitetress|62\\/100|[from] item: Leftovers
|upkeep
|turn|17


|
|-activate|p1a: Kyurem|confusion
|move|p1a: Kyurem|Outrage|p2a: Fortnitetress
|-resisted|p2a: Fortnitetress
|-damage|p2a: Fortnitetress|26\\/100
|move|p2a: Fortnitetress|Gyro Ball|p1a: Kyurem
|-supereffective|p1a: Kyurem
|-damage|p1a: Kyurem|0 fnt
|faint|p1a: Kyurem
|
|win|samsarin23


|c|samsarin23|gg


|l| sooperdooperman
</script>
</div>
<div class="battle-log battle-log-inline"><div class="inner"><div class="battle-options"><div style="padding-top: 3px; padding-right: 3px; text-align: right"><button class="icon button" name="openBattleOptions" title="Options">Battle Options</button></div></div><div class="inner message-log"><div class="chat"><small>☆eviolitemachop joined.</small></div><div class="chat"><small>☆samsarin23 joined.</small></div><div class=""><small>Format:</small> <br><strong>[Gen 5] OU</strong></div><div class=""><small><em>Species Clause:</em> Limit one of each Pokémon</small></div><div class=""><small><em>OHKO Clause:</em> OHKO moves are banned</small></div><div class=""><small><em>Moody Clause:</em> Moody is banned</small></div><div class=""><small><em>Evasion Moves Clause:</em> Evasion moves are banned</small></div><div class=""><small><em>Endless Battle Clause:</em> Forcing endless battles is banned</small></div><div class=""><small><em>HP Percentage Mod:</em> HP is shown in percentages</small></div><div class=""><small><em>Evasion Abilities Clause:</em> Evasion abilities are banned</small></div><div class=""><small><em>Baton Pass Clause:</em> Limit one Baton Passer, can't pass Spe and other stats simultaneously</small></div><div class=""><small><em>Sleep Clause:</em> Sleep-inducing moves are banned</small></div><div class=""><small><em>Swagger Clause:</em> Swagger is banned</small></div><div class="chat battle-history"><strong>eviolitemachop's team:</strong> <em style="color:#445566;display:block;">Volcarona / Espeon / Starmie / Kyurem-Black / Lucario / Weavile</em></div><div class="chat battle-history"><strong>samsarin23's team:</strong> <em style="color:#445566;display:block;">Metagross / Latias / Keldeo / Forretress / Thundurus-Therian / Gyarados</em></div><div class="spacer battle-history"><br></div><div class="battle-history">Battle started between eviolitemachop and samsarin23!<br></div><div class="spacer battle-history"><br></div><div class="battle-history">Go! <strong>Espeon</strong>!<br></div><div class="spacer battle-history"><br></div><div class="battle-history">samsarin23 sent out Metacute (<strong>Metagross</strong>)!<br></div><div class="spacer battle-history"><br></div><h2 class="battle-history">Turn 1</h2><div class="spacer battle-history"><br></div><div class="battle-history">Espeon used <strong>Calm Mind</strong>!<br></div><div class="battle-history"><small>Espeon's Sp. Atk rose!</small><br></div><div class="battle-history"><small>Espeon's Sp. Def rose!</small><br></div><div class="spacer battle-history"><br></div><div class="battle-history">The opposing Metacute used <strong>Stealth Rock</strong>!<br></div><div class="spacer battle-history"><br></div><div class="battle-history">[Espeon's Magic Bounce]<br>Espeon bounced the Stealth Rock back!<br></div><div class="battle-history"><small>Pointed stones float in the air around the opposing team!</small><br></div><div class="spacer battle-history"><br></div><h2 class="battle-history">Turn 2</h2><div class="chat"><small> sooperdooperman joined.</small></div><div class="spacer battle-history"><br></div><div class="battle-history">Espeon used <strong>Calm Mind</strong>!<br></div><div class="battle-history"><small>Espeon's Sp. Atk rose!</small><br></div><div class="battle-history"><small>Espeon's Sp. Def rose!</small><br></div><div class="spacer battle-history"><br></div><div class="battle-history">The opposing Metacute used <strong>Stealth Rock</strong>!<br></div><div class="spacer battle-history"><br></div><div class="battle-history">[Espeon's Magic Bounce]<br>Espeon bounced the Stealth Rock back!<br></div><div class="battle-history"><small>But it failed!</small><br></div><div class="spacer battle-history"><br></div><h2 class="battle-history">Turn 3</h2><div class="chat"><small> sid69420 joined.</small></div><div class="spacer battle-history"><br></div><div class="battle-history">Espeon used <strong>Calm Mind</strong>!<br></div><div class="battle-history"><small>Espeon's Sp. Atk rose!</small><br></div><div class="battle-history"><small>Espeon's Sp. Def rose!</small><br></div><div class="spacer battle-history"><br></div><div class="battle-history">The opposing Metacute used <strong>Signal Beam</strong>!<br></div><div class="battle-history"><small>It's super effective!</small><br></div><div class="battle-history"><small>(Espeon lost 10% of its health!)</small><br></div><div class="spacer battle-history"><br></div><h2 class="battle-history">Turn 4</h2><div class="chat"><small> pkash16 joined.</small></div><div class="spacer battle-history"><br></div><div class="battle-history">Espeon used <strong>Calm Mind</strong>!<br></div><div class="battle-history"><small>Espeon's Sp. Atk rose!</small><br></div><div class="battle-history"><small>Espeon's Sp. Def rose!</small><br></div><div class="spacer battle-history"><br></div><div class="battle-history">The opposing Metacute used <strong>Earthquake</strong>!<br></div><div class="battle-history"><small>(Espeon lost 59% of its health!)</small><br></div><div class="spacer battle-history"><br></div><h2 class="battle-history">Turn 5</h2><div class="spacer battle-history"><br></div><div class="battle-history">Espeon used <strong>Baton Pass</strong>!<br></div><div class="spacer battle-history"><br></div><div class="battle-history">Go! <strong>Starmie</strong>!<br></div><div class="spacer battle-history"><br></div><div class="battle-history">The opposing Metacute used <strong>Earthquake</strong>!<br></div><div class="battle-history"><small>(Starmie lost 50% of its health!)</small><br></div><div class="spacer battle-history"><br></div><h2 class="battle-history">Turn 6</h2><div class="spacer battle-history"><br></div><div class="battle-history">Starmie used <strong>Hydro Pump</strong>!<br></div><div class="battle-history"><small>The opposing Metacute avoided the attack!</small><br></div><div class="spacer battle-history"><br></div><div class="battle-history">The opposing Metacute used <strong>Pursuit</strong>!<br></div><div class="battle-history"><small>It's super effective!</small><br></div><div class="battle-history"><small>(Starmie lost 41% of its health!)</small><br></div><div class="spacer battle-history"><br></div><h2 class="battle-history">Turn 7</h2><div class="chat chatmessage-eviolitemachop"><strong style="color:#29aa90"><small>☆</small><span class="username" data-name="eviolitemachop">eviolitemachop</span>:</strong> <em>F</em></div><div class="chat chatmessage-eviolitemachop"><strong style="color:#29aa90"><small>☆</small><span class="username" data-name="eviolitemachop">eviolitemachop</span>:</strong> <em>i keep missing hydro pumps</em></div><div class="spacer battle-history"><br></div><div class="battle-history">Starmie used <strong>Hydro Pump</strong>!<br></div><div class="battle-history"><small>The opposing Metacute avoided the attack!</small><br></div><div class="spacer battle-history"><br></div><div class="battle-history">The opposing Metacute used <strong>Stealth Rock</strong>!<br></div><div class="battle-history"><small>Pointed stones float in the air around your team!</small><br></div><div class="spacer battle-history"><br></div><h2 class="battle-history">Turn 8</h2><div class="chat chatmessage-eviolitemachop"><strong style="color:#29aa90"><small>☆</small><span class="username" data-name="eviolitemachop">eviolitemachop</span>:</strong> <em>LOL</em></div><div class="chat chatmessage-eviolitemachop"><strong style="color:#29aa90"><small>☆</small><span class="username" data-name="eviolitemachop">eviolitemachop</span>:</strong> <em>gd</em></div><div class="spacer battle-history"><br></div><div class="battle-history">Starmie used <strong>Hydro Pump</strong>!<br></div><div class="battle-history"><small>A critical hit!</small><br></div><div class="battle-history"><small>(The opposing Metacute lost 100% of its health!)</small><br></div><div class="battle-history"><small>Starmie lost some of its HP!</small><br></div><div class="spacer battle-history"><br></div><div class="battle-history">The opposing Metacute fainted!<br></div><div class="battle-history">Starmie fainted!<br></div><div class="chat chatmessage-eviolitemachop"><strong style="color:#29aa90"><small>☆</small><span class="username" data-name="eviolitemachop">eviolitemachop</span>:</strong> <em>finally</em></div><div class="spacer battle-history"><br></div><div class="battle-history">Go! <strong>Lucario</strong>!<br></div><div class="spacer battle-history"><br></div><div class="battle-history">samsarin23 sent out Muchachaaaa (<strong>Latias</strong>)!<br></div><div class="battle-history"><small>Pointed stones dug into the opposing Muchachaaaa!</small><br></div><div class="battle-history"><small>Pointed stones dug into Lucario!</small><br></div><div class="spacer battle-history"><br></div><h2 class="battle-history">Turn 9</h2><div class="spacer battle-history"><br></div><div class="battle-history">samsarin23 withdrew Muchachaaaa!<br></div><div class="battle-history">samsarin23 sent out unicorn mf (<strong>Keldeo</strong>)!<br></div><div class="battle-history"><small>Pointed stones dug into the opposing unicorn mf!</small><br></div><div class="spacer battle-history"><br></div><div class="battle-history">Lucario, come back!<br></div><div class="battle-history">Go! <strong>Weavile</strong>!<br></div><div class="battle-history"><small>Pointed stones dug into Weavile!</small><br></div><div class="battle-history">[Weavile's Pressure]<br><small>Weavile is exerting its pressure!</small><br></div><div class="spacer battle-history"><br></div><h2 class="battle-history">Turn 10</h2><div class="spacer battle-history"><br></div><div class="battle-history">Weavile, come back!<br></div><div class="battle-history">Go! <strong>Espeon</strong>!<br></div><div class="battle-history"><small>Pointed stones dug into Espeon!</small><br></div><div class="spacer battle-history"><br></div><div class="battle-history">The opposing unicorn mf used <strong>Secret Sword</strong>!<br></div><div class="battle-history"><small>It's not very effective...</small><br></div><div class="battle-history"><small>(Espeon lost 19% of its health!)</small><br></div><div class="spacer battle-history"><br></div><div class="battle-history">Espeon fainted!<br></div><div class="spacer battle-history"><br></div><div class="battle-history">Go! <strong>Lucario</strong>!<br></div><div class="battle-history"><small>Pointed stones dug into Lucario!</small><br></div><div class="spacer battle-history"><br></div><h2 class="battle-history">Turn 11</h2><div class="spacer battle-history"><br></div><div class="battle-history">Lucario used <strong>Extreme Speed</strong>!<br></div><div class="battle-history"><small>(The opposing unicorn mf lost 39% of its health!)</small><br></div><div class="battle-history"><small>Lucario lost some of its HP!</small><br></div><div class="spacer battle-history"><br></div><div class="battle-history">The opposing unicorn mf used <strong>Secret Sword</strong>!<br></div><div class="battle-history"><small>It's super effective!</small><br></div><div class="battle-history"><small>(Lucario lost 85% of its health!)</small><br></div><div class="spacer battle-history"><br></div><div class="battle-history">Lucario fainted!<br></div><div class="spacer battle-history"><br></div><div class="battle-history">Go! Volcoronavirus (<strong>Volcarona</strong>)!<br></div><div class="battle-history"><small>Pointed stones dug into Volcoronavirus!</small><br></div><div class="spacer battle-history"><br></div><h2 class="battle-history">Turn 12</h2><div class="chat chatmessage-eviolitemachop"><strong style="color:#29aa90"><small>☆</small><span class="username" data-name="eviolitemachop">eviolitemachop</span>:</strong> <em>ow</em></div><div class="spacer battle-history"><br></div><div class="battle-history">The opposing unicorn mf used <strong>Secret Sword</strong>!<br></div><div class="battle-history"><small>It's not very effective...</small><br></div><div class="battle-history"><small>(Volcoronavirus lost 34% of its health!)</small><br></div><div class="spacer battle-history"><br></div><div class="battle-history">Volcoronavirus used <strong>Giga Drain</strong>!<br></div><div class="battle-history"><small>It's super effective!</small><br></div><div class="battle-history"><small>(The opposing unicorn mf lost 55% of its health!)</small><br></div><div class="battle-history"><small>The opposing unicorn mf had its energy drained!</small><br></div><div class="battle-history"><small>Volcoronavirus lost some of its HP!</small><br></div><div class="spacer battle-history"><br></div><div class="battle-history">The opposing unicorn mf fainted!<br></div><div class="spacer battle-history"><br></div><div class="battle-history">samsarin23 sent out Muchachaaaa (<strong>Latias</strong>)!<br></div><div class="battle-history"><small>Pointed stones dug into the opposing Muchachaaaa!</small><br></div><div class="spacer battle-history"><br></div><h2 class="battle-history">Turn 13</h2><div class="spacer battle-history"><br></div><div class="battle-history">The opposing Muchachaaaa used <strong>Draco Meteor</strong>!<br></div><div class="battle-history"><small>(Volcoronavirus lost 35% of its health!)</small><br></div><div class="battle-history"><small>The opposing Muchachaaaa's Sp. Atk fell harshly!</small><br></div><div class="battle-history"><small>The opposing Muchachaaaa lost some of its HP!</small><br></div><div class="spacer battle-history"><br></div><div class="battle-history">Volcoronavirus fainted!<br></div><div class="spacer battle-history"><br></div><div class="battle-history">Go! <strong>Weavile</strong>!<br></div><div class="battle-history"><small>Pointed stones dug into Weavile!</small><br></div><div class="battle-history">[Weavile's Pressure]<br><small>Weavile is exerting its pressure!</small><br></div><div class="spacer battle-history"><br></div><h2 class="battle-history">Turn 14</h2><div class="spacer battle-history"><br></div><div class="battle-history">The opposing Muchachaaaa used <strong>Hidden Power</strong>!<br></div><div class="battle-history"><small>It's super effective!</small><br></div><div class="battle-history"><small>(Weavile lost 41% of its health!)</small><br></div><div class="battle-history"><small>The opposing Muchachaaaa lost some of its HP!</small><br></div><div class="spacer battle-history"><br></div><div class="battle-history">Weavile used <strong>Pursuit</strong>!<br></div><div class="battle-history"><small>It's super effective!</small><br></div><div class="battle-history"><small>(The opposing Muchachaaaa lost 56% of its health!)</small><br></div><div class="battle-history"><small>Weavile lost some of its HP!</small><br></div><div class="spacer battle-history"><br></div><div class="battle-history">The opposing Muchachaaaa fainted!<br></div><div class="battle-history">Weavile fainted!<br></div><div class="spacer battle-history"><br></div><div class="battle-history">Go! Kyurem (<strong>Kyurem-Black</strong>)!<br></div><div class="spacer battle-history"><br></div><div class="battle-history">samsarin23 sent out Thundurus-Wundurus (<strong>Thundurus-Therian</strong>)!<br></div><div class="battle-history"><small>Pointed stones dug into Kyurem!</small><br></div><div class="battle-history">[Kyurem's Teravolt]<br><small>Kyurem is radiating a bursting aura!</small><br></div><div class="battle-history"><small>Pointed stones dug into the opposing Thundurus-Wundurus!</small><br></div><div class="spacer battle-history"><br></div><h2 class="battle-history">Turn 15</h2><div class="spacer battle-history"><br></div><div class="battle-history">Kyurem used <strong>Outrage</strong>!<br></div><div class="battle-history"><small>A critical hit!</small><br></div><div class="battle-history"><small>(The opposing Thundurus-Wundurus lost 76% of its health!)</small><br></div><div class="spacer battle-history"><br></div><div class="battle-history">The opposing Thundurus-Wundurus fainted!<br></div><div class="spacer battle-history"><br></div><div class="battle-history">samsarin23 sent out Fortnitetress (<strong>Forretress</strong>)!<br></div><div class="battle-history"><small>Pointed stones dug into the opposing Fortnitetress!</small><br></div><div class="spacer battle-history"><br></div><h2 class="battle-history">Turn 16</h2><div class="spacer battle-history"><br></div><div class="battle-history">Kyurem used <strong>Outrage</strong>!<br></div><div class="battle-history"><small>It's not very effective...</small><br></div><div class="battle-history"><small>(The opposing Fortnitetress lost 32% of its health!)</small><br></div><div class="battle-history"><small>Kyurem became confused due to fatigue!</small><br></div><div class="spacer battle-history"><br></div><div class="battle-history">The opposing Fortnitetress used <strong>Gyro Ball</strong>!<br></div><div class="battle-history"><small>It's super effective!</small><br></div><div class="battle-history"><small>(Kyurem lost 57% of its health!)</small><br></div><div class="spacer battle-history"><br></div><div class="battle-history"><small>The opposing Fortnitetress restored a little HP using its Leftovers!</small><br></div><div class="spacer battle-history"><br></div><h2 class="battle-history">Turn 17</h2><div class="spacer battle-history"><br></div><div class="battle-history"><small>Kyurem is confused!</small><br></div><div class="battle-history">Kyurem used <strong>Outrage</strong>!<br></div><div class="battle-history"><small>It's not very effective...</small><br></div><div class="battle-history"><small>(The opposing Fortnitetress lost 36% of its health!)</small><br></div><div class="spacer battle-history"><br></div><div class="battle-history">The opposing Fortnitetress used <strong>Gyro Ball</strong>!<br></div><div class="battle-history"><small>It's super effective!</small><br></div><div class="battle-history"><small>(Kyurem lost 19% of its health!)</small><br></div><div class="spacer battle-history"><br></div><div class="battle-history">Kyurem fainted!<br></div><div class="spacer battle-history"><br></div><div class="battle-history"><strong>samsarin23</strong> won the battle!<br></div><div class="chat chatmessage-samsarin23"><strong style="color:#909f41"><small>☆</small><span class="username" data-name="samsarin23">samsarin23</span>:</strong> <em>gg</em></div><div class="chat"><small> sooperdooperman left.</small></div></div><div class="inner-preempt message-log"></div></div></div>
</div>
<script>
let daily = Math.floor(Date.now()/1000/60/60/24);document.write('<script src="https://play.pokemonshowdown.com/js/replay-embed.js?version'+daily+'"></'+'script>');
</script>
"""

printable = set(string.printable)
replay = filter(lambda x: x in printable, replay)

print("hello")
#print(re.search('(?<=gen[0-9]ou-)[0-9]+', replay))




