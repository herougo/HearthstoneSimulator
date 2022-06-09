# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestBasicsOfAbusiveSergeant::test_card_attacking 1'] = '''0 goes first
------------------------------
0 turn
------------------------------
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)
2: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)
3: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)
4: SpellCardSlot - card_name=Coin, mana=0


Player (0) - health: 5, armour: 0, mana: 100 / 100
0: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)
2: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)
3: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)

0 plays Abusive Sergeant
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)
2: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)
3: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)
4: SpellCardSlot - card_name=Coin, mana=0

\t0: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=3, health=1)

Player (0) - health: 5, armour: 0, mana: 99 / 100
0: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)
2: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)

0 plays Abusive Sergeant
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)
2: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)
3: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)
4: SpellCardSlot - card_name=Coin, mana=0

\t0: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=3, health=1)
\t1: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=3, health=1)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)

------------------------------
1 turn
------------------------------
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)
2: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)
3: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)
4: SpellCardSlot - card_name=Coin, mana=0
5: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)

\t0: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)
\t1: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)

1 plays Abusive Sergeant
Opponent (1) - health: 5, armour: 0, mana: 99 / 100
Weapon: None
0: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)
2: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)
3: SpellCardSlot - card_name=Coin, mana=0
4: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)

\t0: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=3, health=1)
\t0: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)
\t1: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)

1 plays Abusive Sergeant
Opponent (1) - health: 5, armour: 0, mana: 98 / 100
Weapon: None
0: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)

\t0: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=3, health=1)
\t1: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=3, health=1)
\t0: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)
\t1: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)

------------------------------
0 turn
------------------------------
Opponent (1) - health: 5, armour: 0, mana: 98 / 100
Weapon: None
0: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)

\t0: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)
\t1: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)
\t0: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)
\t1: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)

Player (0) - health: 5, armour: 0, mana: 100 / 100
0: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)
2: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)

MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1) attacks MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)
MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=0) died
MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=0) died
Opponent (1) - health: 5, armour: 0, mana: 98 / 100
Weapon: None
0: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)

\t0: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)
\t0: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)

Player (0) - health: 5, armour: 0, mana: 100 / 100
0: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)
2: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)

0 plays Abusive Sergeant
Opponent (1) - health: 5, armour: 0, mana: 98 / 100
Weapon: None
0: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)

\t0: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=3, health=1)
\t0: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)
\t1: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)

Player (0) - health: 5, armour: 0, mana: 99 / 100
0: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)

0 plays Abusive Sergeant
Opponent (1) - health: 5, armour: 0, mana: 98 / 100
Weapon: None
0: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)

\t0: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=5, health=1)
\t0: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)
\t1: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)
\t2: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)

------------------------------
1 turn
------------------------------
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)
4: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)

\t0: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)
\t0: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)
\t1: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)
\t2: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)

MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1) attacks MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)
MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=0) died
MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=0) died
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)
4: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)

\t0: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)
\t1: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)

1 plays Abusive Sergeant
Opponent (1) - health: 5, armour: 0, mana: 99 / 100
Weapon: None
0: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)
1: SpellCardSlot - card_name=Coin, mana=0
2: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)
3: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)

\t0: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=3, health=1)
\t0: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)
\t1: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)

1 plays Abusive Sergeant
Opponent (1) - health: 5, armour: 0, mana: 98 / 100
Weapon: None
0: SpellCardSlot - card_name=Coin, mana=0
1: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)
2: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)

\t0: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=3, health=1)
\t1: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=3, health=1)
\t0: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)
\t1: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)

Opponent (1) - health: 5, armour: 0, mana: 98 / 100
Weapon: None
0: SpellCardSlot - card_name=Coin, mana=0
1: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)
2: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)

\t0: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=3, health=1)
\t1: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=3, health=1)
\t0: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)
\t1: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)

Game Over: Player 0 wins'''

snapshots['TestBasicsOfAbusiveSergeant::test_card_playing 1'] = '''0 goes first
------------------------------
0 turn
------------------------------
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)
2: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)
3: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)
4: SpellCardSlot - card_name=Coin, mana=0


Player (0) - health: 5, armour: 0, mana: 100 / 100
0: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)
2: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)
3: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)

0 plays Abusive Sergeant
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)
2: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)
3: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)
4: SpellCardSlot - card_name=Coin, mana=0

\t0: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=3, health=1)

Player (0) - health: 5, armour: 0, mana: 99 / 100
0: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)
2: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)

0 plays Abusive Sergeant
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)
2: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)
3: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)
4: SpellCardSlot - card_name=Coin, mana=0

\t0: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=3, health=1)
\t1: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=3, health=1)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)

------------------------------
1 turn
------------------------------
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)
2: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)
3: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)
4: SpellCardSlot - card_name=Coin, mana=0
5: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)

\t0: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)
\t1: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)

1 plays Abusive Sergeant
Opponent (1) - health: 5, armour: 0, mana: 99 / 100
Weapon: None
0: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)
2: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)
3: SpellCardSlot - card_name=Coin, mana=0
4: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)

\t0: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=3, health=1)
\t0: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)
\t1: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)

1 plays Abusive Sergeant
Opponent (1) - health: 5, armour: 0, mana: 98 / 100
Weapon: None
0: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)

\t0: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)
\t1: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=5, health=1)
\t0: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)
\t1: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)

Opponent (1) - health: 5, armour: 0, mana: 98 / 100
Weapon: None
0: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)

\t0: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)
\t1: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=5, health=1)
\t0: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)
\t1: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Abusive Sergeant, mana=1, attack=1, health=1)

Game Over: Player 0 wins'''

snapshots['TestBasicsOfAmaniBerserker::test_card_attacking 1'] = '''0 goes first
------------------------------
0 turn
------------------------------
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=2, health=3)
1: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=2, health=3)
2: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=2, health=3)
3: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=2, health=3)
4: SpellCardSlot - card_name=Coin, mana=0


Player (0) - health: 5, armour: 0, mana: 100 / 100
0: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=2, health=3)
1: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=2, health=3)
2: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=2, health=3)
3: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=2, health=3)

0 plays Amani Berserker
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=2, health=3)
1: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=2, health=3)
2: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=2, health=3)
3: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=2, health=3)
4: SpellCardSlot - card_name=Coin, mana=0

\t0: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=5, health=3)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=2, health=3)
1: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=2, health=3)
2: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=2, health=3)

0 plays Amani Berserker
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=2, health=3)
1: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=2, health=3)
2: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=2, health=3)
3: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=2, health=3)
4: SpellCardSlot - card_name=Coin, mana=0

\t0: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=5, health=3)
\t1: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=5, health=3)

Player (0) - health: 5, armour: 0, mana: 96 / 100
0: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=2, health=3)
1: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=2, health=3)

------------------------------
1 turn
------------------------------
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=2, health=3)
1: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=2, health=3)
2: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=2, health=3)
3: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=2, health=3)
4: SpellCardSlot - card_name=Coin, mana=0
5: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=2, health=3)

\t0: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=5, health=3)
\t1: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=5, health=3)

Player (0) - health: 5, armour: 0, mana: 96 / 100
0: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=2, health=3)
1: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=2, health=3)

1 plays Amani Berserker
Opponent (1) - health: 5, armour: 0, mana: 98 / 100
Weapon: None
0: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=2, health=3)
1: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=2, health=3)
2: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=2, health=3)
3: SpellCardSlot - card_name=Coin, mana=0
4: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=2, health=3)

\t0: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=5, health=3)
\t0: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=5, health=3)
\t1: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=5, health=3)

Player (0) - health: 5, armour: 0, mana: 96 / 100
0: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=2, health=3)
1: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=2, health=3)

1 plays Amani Berserker
Opponent (1) - health: 5, armour: 0, mana: 96 / 100
Weapon: None
0: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=2, health=3)
1: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=2, health=3)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=2, health=3)

\t0: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=5, health=3)
\t1: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=5, health=3)
\t0: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=5, health=3)
\t1: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=5, health=3)

Player (0) - health: 5, armour: 0, mana: 96 / 100
0: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=2, health=3)
1: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=2, health=3)

------------------------------
0 turn
------------------------------
Opponent (1) - health: 5, armour: 0, mana: 96 / 100
Weapon: None
0: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=2, health=3)
1: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=2, health=3)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=2, health=3)

\t0: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=5, health=3)
\t1: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=5, health=3)
\t0: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=5, health=3)
\t1: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=5, health=3)

Player (0) - health: 5, armour: 0, mana: 100 / 100
0: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=2, health=3)
1: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=2, health=3)
2: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=2, health=3)

MinionCardSlot - card_name=Amani Berserker, mana=2, attack=5, health=3) attacks MinionCardSlot - card_name=Amani Berserker, mana=2, attack=5, health=3)
MinionCardSlot - card_name=Amani Berserker, mana=2, attack=5, health=-2) died
MinionCardSlot - card_name=Amani Berserker, mana=2, attack=5, health=-2) died
Opponent (1) - health: 5, armour: 0, mana: 96 / 100
Weapon: None
0: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=2, health=3)
1: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=2, health=3)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=2, health=3)

\t0: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=5, health=3)
\t0: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=5, health=3)

Player (0) - health: 5, armour: 0, mana: 100 / 100
0: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=2, health=3)
1: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=2, health=3)
2: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=2, health=3)

0 plays Amani Berserker
Opponent (1) - health: 5, armour: 0, mana: 96 / 100
Weapon: None
0: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=2, health=3)
1: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=2, health=3)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=2, health=3)

\t0: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=5, health=3)
\t0: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=5, health=3)
\t1: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=5, health=3)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=2, health=3)
1: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=2, health=3)

0 plays Amani Berserker
Opponent (1) - health: 5, armour: 0, mana: 96 / 100
Weapon: None
0: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=2, health=3)
1: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=2, health=3)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=2, health=3)

\t0: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=5, health=3)
\t0: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=5, health=3)
\t1: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=5, health=3)
\t2: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=5, health=3)

Player (0) - health: 5, armour: 0, mana: 96 / 100
0: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=2, health=3)

------------------------------
1 turn
------------------------------
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=2, health=3)
1: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=2, health=3)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=2, health=3)
4: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=2, health=3)

\t0: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=5, health=3)
\t0: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=5, health=3)
\t1: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=5, health=3)
\t2: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=5, health=3)

Player (0) - health: 5, armour: 0, mana: 96 / 100
0: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=2, health=3)

MinionCardSlot - card_name=Amani Berserker, mana=2, attack=5, health=3) attacks MinionCardSlot - card_name=Amani Berserker, mana=2, attack=5, health=3)
MinionCardSlot - card_name=Amani Berserker, mana=2, attack=5, health=-2) died
MinionCardSlot - card_name=Amani Berserker, mana=2, attack=5, health=-2) died
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=2, health=3)
1: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=2, health=3)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=2, health=3)
4: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=2, health=3)

\t0: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=5, health=3)
\t1: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=5, health=3)

Player (0) - health: 5, armour: 0, mana: 96 / 100
0: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=2, health=3)

1 plays Amani Berserker
Opponent (1) - health: 5, armour: 0, mana: 98 / 100
Weapon: None
0: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=2, health=3)
1: SpellCardSlot - card_name=Coin, mana=0
2: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=2, health=3)
3: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=2, health=3)

\t0: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=5, health=3)
\t0: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=5, health=3)
\t1: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=5, health=3)

Player (0) - health: 5, armour: 0, mana: 96 / 100
0: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=2, health=3)

1 plays Amani Berserker
Opponent (1) - health: 5, armour: 0, mana: 96 / 100
Weapon: None
0: SpellCardSlot - card_name=Coin, mana=0
1: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=2, health=3)
2: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=2, health=3)

\t0: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=5, health=3)
\t1: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=5, health=3)
\t0: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=5, health=3)
\t1: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=5, health=3)

Player (0) - health: 5, armour: 0, mana: 96 / 100
0: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=2, health=3)

Opponent (1) - health: 5, armour: 0, mana: 96 / 100
Weapon: None
0: SpellCardSlot - card_name=Coin, mana=0
1: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=2, health=3)
2: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=2, health=3)

\t0: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=5, health=3)
\t1: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=5, health=3)
\t0: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=5, health=3)
\t1: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=5, health=3)

Player (0) - health: 5, armour: 0, mana: 96 / 100
0: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=2, health=3)

Game Over: Player 0 wins'''

snapshots['TestBasicsOfAmaniBerserker::test_card_playing 1'] = '''0 goes first
------------------------------
0 turn
------------------------------
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=2, health=3)
1: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=2, health=3)
2: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=2, health=3)
3: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=2, health=3)
4: SpellCardSlot - card_name=Coin, mana=0


Player (0) - health: 5, armour: 0, mana: 100 / 100
0: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=2, health=3)
1: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=2, health=3)
2: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=2, health=3)
3: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=2, health=3)

0 plays Amani Berserker
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=2, health=3)
1: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=2, health=3)
2: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=2, health=3)
3: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=2, health=3)
4: SpellCardSlot - card_name=Coin, mana=0

\t0: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=5, health=3)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=2, health=3)
1: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=2, health=3)
2: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=2, health=3)

0 plays Amani Berserker
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=2, health=3)
1: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=2, health=3)
2: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=2, health=3)
3: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=2, health=3)
4: SpellCardSlot - card_name=Coin, mana=0

\t0: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=5, health=3)
\t1: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=5, health=3)

Player (0) - health: 5, armour: 0, mana: 96 / 100
0: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=2, health=3)
1: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=2, health=3)

------------------------------
1 turn
------------------------------
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=2, health=3)
1: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=2, health=3)
2: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=2, health=3)
3: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=2, health=3)
4: SpellCardSlot - card_name=Coin, mana=0
5: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=2, health=3)

\t0: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=5, health=3)
\t1: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=5, health=3)

Player (0) - health: 5, armour: 0, mana: 96 / 100
0: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=2, health=3)
1: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=2, health=3)

1 plays Amani Berserker
Opponent (1) - health: 5, armour: 0, mana: 98 / 100
Weapon: None
0: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=2, health=3)
1: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=2, health=3)
2: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=2, health=3)
3: SpellCardSlot - card_name=Coin, mana=0
4: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=2, health=3)

\t0: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=5, health=3)
\t0: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=5, health=3)
\t1: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=5, health=3)

Player (0) - health: 5, armour: 0, mana: 96 / 100
0: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=2, health=3)
1: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=2, health=3)

1 plays Amani Berserker
Opponent (1) - health: 5, armour: 0, mana: 96 / 100
Weapon: None
0: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=2, health=3)
1: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=2, health=3)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=2, health=3)

\t0: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=5, health=3)
\t1: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=5, health=3)
\t0: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=5, health=3)
\t1: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=5, health=3)

Player (0) - health: 5, armour: 0, mana: 96 / 100
0: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=2, health=3)
1: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=2, health=3)

Opponent (1) - health: 5, armour: 0, mana: 96 / 100
Weapon: None
0: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=2, health=3)
1: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=2, health=3)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=2, health=3)

\t0: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=5, health=3)
\t1: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=5, health=3)
\t0: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=5, health=3)
\t1: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=5, health=3)

Player (0) - health: 5, armour: 0, mana: 96 / 100
0: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=2, health=3)
1: MinionCardSlot - card_name=Amani Berserker, mana=2, attack=2, health=3)

Game Over: Player 0 wins'''

snapshots['TestBasicsOfArgentSquire::test_card_attacking 1'] = '''0 goes first
------------------------------
0 turn
------------------------------
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)
2: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)
3: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)
4: SpellCardSlot - card_name=Coin, mana=0


Player (0) - health: 5, armour: 0, mana: 100 / 100
0: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)
2: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)
3: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)

0 plays Argent Squire
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)
2: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)
3: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)
4: SpellCardSlot - card_name=Coin, mana=0

\t0: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)

Player (0) - health: 5, armour: 0, mana: 99 / 100
0: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)
2: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)

0 plays Argent Squire
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)
2: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)
3: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)
4: SpellCardSlot - card_name=Coin, mana=0

\t0: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)
\t1: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)

------------------------------
1 turn
------------------------------
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)
2: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)
3: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)
4: SpellCardSlot - card_name=Coin, mana=0
5: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)

\t0: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)
\t1: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)

1 plays Argent Squire
Opponent (1) - health: 5, armour: 0, mana: 99 / 100
Weapon: None
0: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)
2: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)
3: SpellCardSlot - card_name=Coin, mana=0
4: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)

\t0: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)
\t0: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)
\t1: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)

1 plays Argent Squire
Opponent (1) - health: 5, armour: 0, mana: 98 / 100
Weapon: None
0: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)

\t0: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)
\t1: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)
\t0: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)
\t1: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)

------------------------------
0 turn
------------------------------
Opponent (1) - health: 5, armour: 0, mana: 98 / 100
Weapon: None
0: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)

\t0: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)
\t1: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)
\t0: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)
\t1: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)

Player (0) - health: 5, armour: 0, mana: 100 / 100
0: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)
2: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)

MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1) attacks MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)
MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=0) died
MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=0) died
Opponent (1) - health: 5, armour: 0, mana: 98 / 100
Weapon: None
0: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)

\t0: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)
\t0: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)

Player (0) - health: 5, armour: 0, mana: 100 / 100
0: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)
2: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)

0 plays Argent Squire
Opponent (1) - health: 5, armour: 0, mana: 98 / 100
Weapon: None
0: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)

\t0: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)
\t0: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)
\t1: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)

Player (0) - health: 5, armour: 0, mana: 99 / 100
0: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)

0 plays Argent Squire
Opponent (1) - health: 5, armour: 0, mana: 98 / 100
Weapon: None
0: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)

\t0: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)
\t0: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)
\t1: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)
\t2: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)

------------------------------
1 turn
------------------------------
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)
4: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)

\t0: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)
\t0: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)
\t1: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)
\t2: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)

MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1) attacks MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)
MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=0) died
MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=0) died
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)
4: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)

\t0: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)
\t1: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)

1 plays Argent Squire
Opponent (1) - health: 5, armour: 0, mana: 99 / 100
Weapon: None
0: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)
1: SpellCardSlot - card_name=Coin, mana=0
2: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)
3: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)

\t0: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)
\t0: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)
\t1: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)

1 plays Argent Squire
Opponent (1) - health: 5, armour: 0, mana: 98 / 100
Weapon: None
0: SpellCardSlot - card_name=Coin, mana=0
1: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)
2: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)

\t0: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)
\t1: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)
\t0: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)
\t1: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)

Opponent (1) - health: 5, armour: 0, mana: 98 / 100
Weapon: None
0: SpellCardSlot - card_name=Coin, mana=0
1: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)
2: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)

\t0: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)
\t1: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)
\t0: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)
\t1: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)

Game Over: Player 0 wins'''

snapshots['TestBasicsOfArgentSquire::test_card_playing 1'] = '''0 goes first
------------------------------
0 turn
------------------------------
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)
2: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)
3: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)
4: SpellCardSlot - card_name=Coin, mana=0


Player (0) - health: 5, armour: 0, mana: 100 / 100
0: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)
2: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)
3: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)

0 plays Argent Squire
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)
2: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)
3: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)
4: SpellCardSlot - card_name=Coin, mana=0

\t0: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)

Player (0) - health: 5, armour: 0, mana: 99 / 100
0: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)
2: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)

0 plays Argent Squire
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)
2: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)
3: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)
4: SpellCardSlot - card_name=Coin, mana=0

\t0: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)
\t1: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)

------------------------------
1 turn
------------------------------
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)
2: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)
3: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)
4: SpellCardSlot - card_name=Coin, mana=0
5: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)

\t0: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)
\t1: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)

1 plays Argent Squire
Opponent (1) - health: 5, armour: 0, mana: 99 / 100
Weapon: None
0: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)
2: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)
3: SpellCardSlot - card_name=Coin, mana=0
4: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)

\t0: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)
\t0: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)
\t1: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)

1 plays Argent Squire
Opponent (1) - health: 5, armour: 0, mana: 98 / 100
Weapon: None
0: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)

\t0: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)
\t1: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)
\t0: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)
\t1: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)

Opponent (1) - health: 5, armour: 0, mana: 98 / 100
Weapon: None
0: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)

\t0: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)
\t1: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)
\t0: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)
\t1: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Argent Squire, mana=1, attack=1, health=1)

Game Over: Player 0 wins'''

snapshots['TestBasicsOfBloodsailRaider::test_card_attacking 1'] = '''0 goes first
------------------------------
0 turn
------------------------------
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)
1: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)
2: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)
3: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)
4: SpellCardSlot - card_name=Coin, mana=0


Player (0) - health: 5, armour: 0, mana: 100 / 100
0: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)
1: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)
2: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)
3: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)

0 plays Bloodsail Raider
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)
1: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)
2: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)
3: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)
4: SpellCardSlot - card_name=Coin, mana=0

\t0: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)
1: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)
2: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)

0 plays Bloodsail Raider
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)
1: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)
2: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)
3: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)
4: SpellCardSlot - card_name=Coin, mana=0

\t0: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)
\t1: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)

Player (0) - health: 5, armour: 0, mana: 96 / 100
0: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)
1: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)

------------------------------
1 turn
------------------------------
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)
1: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)
2: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)
3: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)
4: SpellCardSlot - card_name=Coin, mana=0
5: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)

\t0: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)
\t1: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)

Player (0) - health: 5, armour: 0, mana: 96 / 100
0: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)
1: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)

1 plays Bloodsail Raider
Opponent (1) - health: 5, armour: 0, mana: 98 / 100
Weapon: None
0: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)
1: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)
2: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)
3: SpellCardSlot - card_name=Coin, mana=0
4: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)

\t0: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)
\t0: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)
\t1: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)

Player (0) - health: 5, armour: 0, mana: 96 / 100
0: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)
1: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)

1 plays Bloodsail Raider
Opponent (1) - health: 5, armour: 0, mana: 96 / 100
Weapon: None
0: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)
1: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)

\t0: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)
\t1: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)
\t0: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)
\t1: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)

Player (0) - health: 5, armour: 0, mana: 96 / 100
0: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)
1: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)

------------------------------
0 turn
------------------------------
Opponent (1) - health: 5, armour: 0, mana: 96 / 100
Weapon: None
0: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)
1: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)

\t0: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)
\t1: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)
\t0: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)
\t1: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)

Player (0) - health: 5, armour: 0, mana: 100 / 100
0: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)
1: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)
2: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)

MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3) attacks MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)
Opponent (1) - health: 5, armour: 0, mana: 96 / 100
Weapon: None
0: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)
1: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)

\t0: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=1)
\t1: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)
\t0: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=1)
\t1: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)

Player (0) - health: 5, armour: 0, mana: 100 / 100
0: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)
1: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)
2: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)

0 plays Bloodsail Raider
Opponent (1) - health: 5, armour: 0, mana: 96 / 100
Weapon: None
0: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)
1: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)

\t0: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=1)
\t1: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)
\t0: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)
\t1: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=1)
\t2: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)
1: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)

0 plays Bloodsail Raider
Opponent (1) - health: 5, armour: 0, mana: 96 / 100
Weapon: None
0: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)
1: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)

\t0: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=1)
\t1: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)
\t0: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)
\t1: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)
\t2: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=1)
\t3: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)

Player (0) - health: 5, armour: 0, mana: 96 / 100
0: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)

------------------------------
1 turn
------------------------------
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)
1: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)
4: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)

\t0: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=1)
\t1: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)
\t0: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)
\t1: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)
\t2: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=1)
\t3: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)

Player (0) - health: 5, armour: 0, mana: 96 / 100
0: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)

MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=1) attacks MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)
MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=-1) died
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)
1: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)
4: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)

\t0: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)
\t0: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=1)
\t1: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)
\t2: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=1)
\t3: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)

Player (0) - health: 5, armour: 0, mana: 96 / 100
0: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)

1 plays Bloodsail Raider
Opponent (1) - health: 5, armour: 0, mana: 98 / 100
Weapon: None
0: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)
1: SpellCardSlot - card_name=Coin, mana=0
2: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)
3: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)

\t0: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)
\t1: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)
\t0: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=1)
\t1: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)
\t2: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=1)
\t3: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)

Player (0) - health: 5, armour: 0, mana: 96 / 100
0: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)

1 plays Bloodsail Raider
Opponent (1) - health: 5, armour: 0, mana: 96 / 100
Weapon: None
0: SpellCardSlot - card_name=Coin, mana=0
1: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)
2: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)

\t0: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)
\t1: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)
\t2: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)
\t0: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=1)
\t1: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)
\t2: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=1)
\t3: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)

Player (0) - health: 5, armour: 0, mana: 96 / 100
0: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)

Opponent (1) - health: 5, armour: 0, mana: 96 / 100
Weapon: None
0: SpellCardSlot - card_name=Coin, mana=0
1: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)
2: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)

\t0: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)
\t1: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)
\t2: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)
\t0: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=1)
\t1: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)
\t2: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=1)
\t3: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)

Player (0) - health: 5, armour: 0, mana: 96 / 100
0: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)

Game Over: Player 0 wins'''

snapshots['TestBasicsOfBloodsailRaider::test_card_playing 1'] = '''0 goes first
------------------------------
0 turn
------------------------------
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)
1: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)
2: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)
3: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)
4: SpellCardSlot - card_name=Coin, mana=0


Player (0) - health: 5, armour: 0, mana: 100 / 100
0: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)
1: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)
2: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)
3: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)

0 plays Bloodsail Raider
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)
1: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)
2: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)
3: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)
4: SpellCardSlot - card_name=Coin, mana=0

\t0: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)
1: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)
2: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)

0 plays Bloodsail Raider
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)
1: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)
2: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)
3: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)
4: SpellCardSlot - card_name=Coin, mana=0

\t0: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)
\t1: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)

Player (0) - health: 5, armour: 0, mana: 96 / 100
0: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)
1: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)

------------------------------
1 turn
------------------------------
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)
1: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)
2: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)
3: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)
4: SpellCardSlot - card_name=Coin, mana=0
5: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)

\t0: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)
\t1: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)

Player (0) - health: 5, armour: 0, mana: 96 / 100
0: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)
1: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)

1 plays Bloodsail Raider
Opponent (1) - health: 5, armour: 0, mana: 98 / 100
Weapon: None
0: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)
1: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)
2: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)
3: SpellCardSlot - card_name=Coin, mana=0
4: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)

\t0: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)
\t0: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)
\t1: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)

Player (0) - health: 5, armour: 0, mana: 96 / 100
0: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)
1: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)

1 plays Bloodsail Raider
Opponent (1) - health: 5, armour: 0, mana: 96 / 100
Weapon: None
0: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)
1: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)

\t0: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)
\t1: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)
\t0: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)
\t1: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)

Player (0) - health: 5, armour: 0, mana: 96 / 100
0: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)
1: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)

Opponent (1) - health: 5, armour: 0, mana: 96 / 100
Weapon: None
0: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)
1: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)

\t0: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)
\t1: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)
\t0: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)
\t1: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)

Player (0) - health: 5, armour: 0, mana: 96 / 100
0: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)
1: MinionCardSlot - card_name=Bloodsail Raider, mana=2, attack=2, health=3)

Game Over: Player 0 wins'''

snapshots['TestBasicsOfCoin::test_card_playing 1'] = '''0 goes first
------------------------------
0 turn
------------------------------
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: SpellCardSlot - card_name=Coin, mana=0
1: SpellCardSlot - card_name=Coin, mana=0
2: SpellCardSlot - card_name=Coin, mana=0
3: SpellCardSlot - card_name=Coin, mana=0
4: SpellCardSlot - card_name=Coin, mana=0


Player (0) - health: 5, armour: 0, mana: 100 / 100
0: SpellCardSlot - card_name=Coin, mana=0
1: SpellCardSlot - card_name=Coin, mana=0
2: SpellCardSlot - card_name=Coin, mana=0
3: SpellCardSlot - card_name=Coin, mana=0

ERROR: Invalid action argument number (should be 1)
ERROR: Invalid action argument number (should be 1)
------------------------------
1 turn
------------------------------
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: SpellCardSlot - card_name=Coin, mana=0
1: SpellCardSlot - card_name=Coin, mana=0
2: SpellCardSlot - card_name=Coin, mana=0
3: SpellCardSlot - card_name=Coin, mana=0
4: SpellCardSlot - card_name=Coin, mana=0
5: SpellCardSlot - card_name=Coin, mana=0


Player (0) - health: 5, armour: 0, mana: 100 / 100
0: SpellCardSlot - card_name=Coin, mana=0
1: SpellCardSlot - card_name=Coin, mana=0
2: SpellCardSlot - card_name=Coin, mana=0
3: SpellCardSlot - card_name=Coin, mana=0

ERROR: Invalid action argument number (should be 1)
ERROR: Invalid action argument number (should be 1)
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: SpellCardSlot - card_name=Coin, mana=0
1: SpellCardSlot - card_name=Coin, mana=0
2: SpellCardSlot - card_name=Coin, mana=0
3: SpellCardSlot - card_name=Coin, mana=0
4: SpellCardSlot - card_name=Coin, mana=0
5: SpellCardSlot - card_name=Coin, mana=0


Player (0) - health: 5, armour: 0, mana: 100 / 100
0: SpellCardSlot - card_name=Coin, mana=0
1: SpellCardSlot - card_name=Coin, mana=0
2: SpellCardSlot - card_name=Coin, mana=0
3: SpellCardSlot - card_name=Coin, mana=0

Game Over: Player 0 wins'''

snapshots['TestBasicsOfDemonHunter::test_card_playing 1'] = '''0 goes first
------------------------------
0 turn
------------------------------
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
4: SpellCardSlot - card_name=Coin, mana=0


Player (0) - health: 5, armour: 0, mana: 100 / 100
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
4: SpellCardSlot - card_name=Coin, mana=0


Player (0) - health: 5, armour: 0, mana: 99 / 100
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
4: SpellCardSlot - card_name=Coin, mana=0


Player (0) - health: 5, armour: 0, mana: 99 / 100
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

ERROR: already used the hero power
------------------------------
1 turn
------------------------------
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
4: SpellCardSlot - card_name=Coin, mana=0
5: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)


Player (0) - health: 5, armour: 0, mana: 99 / 100
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

Opponent (1) - health: 5, armour: 0, mana: 99 / 100
Weapon: None
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
4: SpellCardSlot - card_name=Coin, mana=0
5: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)


Player (0) - health: 5, armour: 0, mana: 99 / 100
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

Opponent (1) - health: 5, armour: 0, mana: 99 / 100
Weapon: None
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
4: SpellCardSlot - card_name=Coin, mana=0
5: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)


Player (0) - health: 5, armour: 0, mana: 99 / 100
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

ERROR: already used the hero power
Opponent (1) - health: 5, armour: 0, mana: 99 / 100
Weapon: None
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
4: SpellCardSlot - card_name=Coin, mana=0
5: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)


Player (0) - health: 5, armour: 0, mana: 99 / 100
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

Game Over: Player 0 wins'''

snapshots['TestBasicsOfDireWolfAlpha::test_card_attacking 1'] = '''0 goes first
------------------------------
0 turn
------------------------------
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)
1: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)
2: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)
3: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)
4: SpellCardSlot - card_name=Coin, mana=0


Player (0) - health: 5, armour: 0, mana: 100 / 100
0: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)
1: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)
2: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)
3: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)

0 plays Dire Wolf Alpha
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)
1: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)
2: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)
3: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)
4: SpellCardSlot - card_name=Coin, mana=0

\t0: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)
1: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)
2: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)

0 plays Dire Wolf Alpha
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)
1: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)
2: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)
3: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)
4: SpellCardSlot - card_name=Coin, mana=0

\t0: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=3, health=2)
\t1: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=3, health=2)

Player (0) - health: 5, armour: 0, mana: 96 / 100
0: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)
1: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)

------------------------------
1 turn
------------------------------
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)
1: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)
2: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)
3: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)
4: SpellCardSlot - card_name=Coin, mana=0
5: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)

\t0: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=3, health=2)
\t1: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=3, health=2)

Player (0) - health: 5, armour: 0, mana: 96 / 100
0: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)
1: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)

1 plays Dire Wolf Alpha
Opponent (1) - health: 5, armour: 0, mana: 98 / 100
Weapon: None
0: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)
1: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)
2: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)
3: SpellCardSlot - card_name=Coin, mana=0
4: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)

\t0: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)
\t0: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=3, health=2)
\t1: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=3, health=2)

Player (0) - health: 5, armour: 0, mana: 96 / 100
0: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)
1: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)

1 plays Dire Wolf Alpha
Opponent (1) - health: 5, armour: 0, mana: 96 / 100
Weapon: None
0: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)
1: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)

\t0: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=3, health=2)
\t1: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=3, health=2)
\t0: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=3, health=2)
\t1: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=3, health=2)

Player (0) - health: 5, armour: 0, mana: 96 / 100
0: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)
1: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)

------------------------------
0 turn
------------------------------
Opponent (1) - health: 5, armour: 0, mana: 96 / 100
Weapon: None
0: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)
1: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)

\t0: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=3, health=2)
\t1: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=3, health=2)
\t0: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=3, health=2)
\t1: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=3, health=2)

Player (0) - health: 5, armour: 0, mana: 100 / 100
0: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)
1: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)
2: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)

MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=3, health=2) attacks MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=3, health=2)
MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=3, health=-1) died
MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=3, health=-1) died
Opponent (1) - health: 5, armour: 0, mana: 96 / 100
Weapon: None
0: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)
1: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)

\t0: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)
\t0: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)

Player (0) - health: 5, armour: 0, mana: 100 / 100
0: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)
1: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)
2: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)

0 plays Dire Wolf Alpha
Opponent (1) - health: 5, armour: 0, mana: 96 / 100
Weapon: None
0: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)
1: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)

\t0: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)
\t0: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=3, health=2)
\t1: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=3, health=2)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)
1: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)

0 plays Dire Wolf Alpha
Opponent (1) - health: 5, armour: 0, mana: 96 / 100
Weapon: None
0: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)
1: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)

\t0: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)
\t0: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=3, health=2)
\t1: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=4, health=2)
\t2: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=3, health=2)

Player (0) - health: 5, armour: 0, mana: 96 / 100
0: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)

------------------------------
1 turn
------------------------------
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)
1: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)
4: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)

\t0: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)
\t0: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=3, health=2)
\t1: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=4, health=2)
\t2: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=3, health=2)

Player (0) - health: 5, armour: 0, mana: 96 / 100
0: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)

MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2) attacks MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=3, health=2)
MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=-1) died
MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=3, health=0) died
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)
1: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)
4: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)

\t0: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=3, health=2)
\t1: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=3, health=2)

Player (0) - health: 5, armour: 0, mana: 96 / 100
0: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)

1 plays Dire Wolf Alpha
Opponent (1) - health: 5, armour: 0, mana: 98 / 100
Weapon: None
0: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)
1: SpellCardSlot - card_name=Coin, mana=0
2: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)
3: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)

\t0: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)
\t0: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=3, health=2)
\t1: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=3, health=2)

Player (0) - health: 5, armour: 0, mana: 96 / 100
0: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)

1 plays Dire Wolf Alpha
Opponent (1) - health: 5, armour: 0, mana: 96 / 100
Weapon: None
0: SpellCardSlot - card_name=Coin, mana=0
1: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)
2: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)

\t0: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=3, health=2)
\t1: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=3, health=2)
\t0: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=3, health=2)
\t1: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=3, health=2)

Player (0) - health: 5, armour: 0, mana: 96 / 100
0: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)

Opponent (1) - health: 5, armour: 0, mana: 96 / 100
Weapon: None
0: SpellCardSlot - card_name=Coin, mana=0
1: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)
2: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)

\t0: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=3, health=2)
\t1: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=3, health=2)
\t0: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=3, health=2)
\t1: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=3, health=2)

Player (0) - health: 5, armour: 0, mana: 96 / 100
0: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)

Game Over: Player 0 wins'''

snapshots['TestBasicsOfDireWolfAlpha::test_card_playing 1'] = '''0 goes first
------------------------------
0 turn
------------------------------
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)
1: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)
2: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)
3: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)
4: SpellCardSlot - card_name=Coin, mana=0


Player (0) - health: 5, armour: 0, mana: 100 / 100
0: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)
1: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)
2: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)
3: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)

0 plays Dire Wolf Alpha
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)
1: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)
2: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)
3: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)
4: SpellCardSlot - card_name=Coin, mana=0

\t0: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)
1: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)
2: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)

0 plays Dire Wolf Alpha
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)
1: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)
2: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)
3: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)
4: SpellCardSlot - card_name=Coin, mana=0

\t0: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=3, health=2)
\t1: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=3, health=2)

Player (0) - health: 5, armour: 0, mana: 96 / 100
0: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)
1: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)

------------------------------
1 turn
------------------------------
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)
1: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)
2: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)
3: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)
4: SpellCardSlot - card_name=Coin, mana=0
5: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)

\t0: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=3, health=2)
\t1: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=3, health=2)

Player (0) - health: 5, armour: 0, mana: 96 / 100
0: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)
1: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)

1 plays Dire Wolf Alpha
Opponent (1) - health: 5, armour: 0, mana: 98 / 100
Weapon: None
0: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)
1: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)
2: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)
3: SpellCardSlot - card_name=Coin, mana=0
4: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)

\t0: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)
\t0: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=3, health=2)
\t1: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=3, health=2)

Player (0) - health: 5, armour: 0, mana: 96 / 100
0: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)
1: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)

1 plays Dire Wolf Alpha
Opponent (1) - health: 5, armour: 0, mana: 96 / 100
Weapon: None
0: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)
1: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)

\t0: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=3, health=2)
\t1: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=3, health=2)
\t0: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=3, health=2)
\t1: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=3, health=2)

Player (0) - health: 5, armour: 0, mana: 96 / 100
0: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)
1: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)

Opponent (1) - health: 5, armour: 0, mana: 96 / 100
Weapon: None
0: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)
1: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)

\t0: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=3, health=2)
\t1: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=3, health=2)
\t0: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=3, health=2)
\t1: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=3, health=2)

Player (0) - health: 5, armour: 0, mana: 96 / 100
0: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)
1: MinionCardSlot - card_name=Dire Wolf Alpha, mana=2, attack=2, health=2)

Game Over: Player 0 wins'''

snapshots['TestBasicsOfDruid::test_card_playing 1'] = '''0 goes first
------------------------------
0 turn
------------------------------
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
4: SpellCardSlot - card_name=Coin, mana=0


Player (0) - health: 5, armour: 0, mana: 100 / 100
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
4: SpellCardSlot - card_name=Coin, mana=0


Player (0) - health: 5, armour: 1, mana: 98 / 100
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
4: SpellCardSlot - card_name=Coin, mana=0


Player (0) - health: 5, armour: 1, mana: 98 / 100
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

ERROR: already used the hero power
------------------------------
1 turn
------------------------------
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
4: SpellCardSlot - card_name=Coin, mana=0
5: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)


Player (0) - health: 5, armour: 1, mana: 98 / 100
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

Opponent (1) - health: 5, armour: 1, mana: 98 / 100
Weapon: None
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
4: SpellCardSlot - card_name=Coin, mana=0
5: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)


Player (0) - health: 5, armour: 1, mana: 98 / 100
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

Opponent (1) - health: 5, armour: 1, mana: 98 / 100
Weapon: None
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
4: SpellCardSlot - card_name=Coin, mana=0
5: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)


Player (0) - health: 5, armour: 1, mana: 98 / 100
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

ERROR: already used the hero power
Opponent (1) - health: 5, armour: 1, mana: 98 / 100
Weapon: None
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
4: SpellCardSlot - card_name=Coin, mana=0
5: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)


Player (0) - health: 5, armour: 1, mana: 98 / 100
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

Game Over: Player 0 wins'''

snapshots['TestBasicsOfFaerieDragon::test_card_attacking 1'] = '''0 goes first
------------------------------
0 turn
------------------------------
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)
1: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)
2: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)
3: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)
4: SpellCardSlot - card_name=Coin, mana=0


Player (0) - health: 5, armour: 0, mana: 100 / 100
0: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)
1: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)
2: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)
3: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)

0 plays Faerie Dragon
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)
1: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)
2: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)
3: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)
4: SpellCardSlot - card_name=Coin, mana=0

\t0: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)
1: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)
2: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)

0 plays Faerie Dragon
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)
1: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)
2: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)
3: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)
4: SpellCardSlot - card_name=Coin, mana=0

\t0: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)
\t1: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)

Player (0) - health: 5, armour: 0, mana: 96 / 100
0: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)
1: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)

------------------------------
1 turn
------------------------------
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)
1: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)
2: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)
3: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)
4: SpellCardSlot - card_name=Coin, mana=0
5: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)

\t0: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)
\t1: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)

Player (0) - health: 5, armour: 0, mana: 96 / 100
0: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)
1: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)

1 plays Faerie Dragon
Opponent (1) - health: 5, armour: 0, mana: 98 / 100
Weapon: None
0: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)
1: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)
2: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)
3: SpellCardSlot - card_name=Coin, mana=0
4: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)

\t0: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)
\t0: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)
\t1: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)

Player (0) - health: 5, armour: 0, mana: 96 / 100
0: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)
1: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)

1 plays Faerie Dragon
Opponent (1) - health: 5, armour: 0, mana: 96 / 100
Weapon: None
0: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)
1: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)

\t0: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)
\t1: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)
\t0: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)
\t1: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)

Player (0) - health: 5, armour: 0, mana: 96 / 100
0: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)
1: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)

------------------------------
0 turn
------------------------------
Opponent (1) - health: 5, armour: 0, mana: 96 / 100
Weapon: None
0: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)
1: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)

\t0: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)
\t1: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)
\t0: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)
\t1: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)

Player (0) - health: 5, armour: 0, mana: 100 / 100
0: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)
1: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)
2: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)

MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2) attacks MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)
MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=-1) died
MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=-1) died
Opponent (1) - health: 5, armour: 0, mana: 96 / 100
Weapon: None
0: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)
1: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)

\t0: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)
\t0: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)

Player (0) - health: 5, armour: 0, mana: 100 / 100
0: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)
1: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)
2: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)

0 plays Faerie Dragon
Opponent (1) - health: 5, armour: 0, mana: 96 / 100
Weapon: None
0: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)
1: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)

\t0: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)
\t0: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)
\t1: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)
1: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)

0 plays Faerie Dragon
Opponent (1) - health: 5, armour: 0, mana: 96 / 100
Weapon: None
0: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)
1: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)

\t0: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)
\t0: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)
\t1: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)
\t2: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)

Player (0) - health: 5, armour: 0, mana: 96 / 100
0: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)

------------------------------
1 turn
------------------------------
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)
1: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)
4: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)

\t0: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)
\t0: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)
\t1: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)
\t2: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)

Player (0) - health: 5, armour: 0, mana: 96 / 100
0: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)

MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2) attacks MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)
MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=-1) died
MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=-1) died
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)
1: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)
4: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)

\t0: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)
\t1: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)

Player (0) - health: 5, armour: 0, mana: 96 / 100
0: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)

1 plays Faerie Dragon
Opponent (1) - health: 5, armour: 0, mana: 98 / 100
Weapon: None
0: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)
1: SpellCardSlot - card_name=Coin, mana=0
2: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)
3: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)

\t0: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)
\t0: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)
\t1: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)

Player (0) - health: 5, armour: 0, mana: 96 / 100
0: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)

1 plays Faerie Dragon
Opponent (1) - health: 5, armour: 0, mana: 96 / 100
Weapon: None
0: SpellCardSlot - card_name=Coin, mana=0
1: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)
2: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)

\t0: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)
\t1: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)
\t0: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)
\t1: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)

Player (0) - health: 5, armour: 0, mana: 96 / 100
0: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)

Opponent (1) - health: 5, armour: 0, mana: 96 / 100
Weapon: None
0: SpellCardSlot - card_name=Coin, mana=0
1: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)
2: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)

\t0: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)
\t1: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)
\t0: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)
\t1: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)

Player (0) - health: 5, armour: 0, mana: 96 / 100
0: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)

Game Over: Player 0 wins'''

snapshots['TestBasicsOfFaerieDragon::test_card_playing 1'] = '''0 goes first
------------------------------
0 turn
------------------------------
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)
1: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)
2: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)
3: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)
4: SpellCardSlot - card_name=Coin, mana=0


Player (0) - health: 5, armour: 0, mana: 100 / 100
0: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)
1: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)
2: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)
3: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)

0 plays Faerie Dragon
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)
1: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)
2: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)
3: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)
4: SpellCardSlot - card_name=Coin, mana=0

\t0: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)
1: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)
2: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)

0 plays Faerie Dragon
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)
1: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)
2: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)
3: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)
4: SpellCardSlot - card_name=Coin, mana=0

\t0: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)
\t1: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)

Player (0) - health: 5, armour: 0, mana: 96 / 100
0: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)
1: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)

------------------------------
1 turn
------------------------------
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)
1: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)
2: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)
3: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)
4: SpellCardSlot - card_name=Coin, mana=0
5: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)

\t0: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)
\t1: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)

Player (0) - health: 5, armour: 0, mana: 96 / 100
0: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)
1: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)

1 plays Faerie Dragon
Opponent (1) - health: 5, armour: 0, mana: 98 / 100
Weapon: None
0: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)
1: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)
2: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)
3: SpellCardSlot - card_name=Coin, mana=0
4: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)

\t0: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)
\t0: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)
\t1: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)

Player (0) - health: 5, armour: 0, mana: 96 / 100
0: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)
1: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)

1 plays Faerie Dragon
Opponent (1) - health: 5, armour: 0, mana: 96 / 100
Weapon: None
0: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)
1: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)

\t0: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)
\t1: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)
\t0: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)
\t1: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)

Player (0) - health: 5, armour: 0, mana: 96 / 100
0: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)
1: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)

Opponent (1) - health: 5, armour: 0, mana: 96 / 100
Weapon: None
0: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)
1: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)

\t0: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)
\t1: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)
\t0: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)
\t1: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)

Player (0) - health: 5, armour: 0, mana: 96 / 100
0: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)
1: MinionCardSlot - card_name=Faerie Dragon, mana=2, attack=3, health=2)

Game Over: Player 0 wins'''

snapshots['TestBasicsOfHealingTotem::test_card_playing 1'] = '''0 goes first
------------------------------
0 turn
------------------------------
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Healing Totem, mana=1, attack=0, health=2)
1: MinionCardSlot - card_name=Healing Totem, mana=1, attack=0, health=2)
2: MinionCardSlot - card_name=Healing Totem, mana=1, attack=0, health=2)
3: MinionCardSlot - card_name=Healing Totem, mana=1, attack=0, health=2)
4: SpellCardSlot - card_name=Coin, mana=0


Player (0) - health: 5, armour: 0, mana: 100 / 100
0: MinionCardSlot - card_name=Healing Totem, mana=1, attack=0, health=2)
1: MinionCardSlot - card_name=Healing Totem, mana=1, attack=0, health=2)
2: MinionCardSlot - card_name=Healing Totem, mana=1, attack=0, health=2)
3: MinionCardSlot - card_name=Healing Totem, mana=1, attack=0, health=2)

0 plays Healing Totem
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Healing Totem, mana=1, attack=0, health=2)
1: MinionCardSlot - card_name=Healing Totem, mana=1, attack=0, health=2)
2: MinionCardSlot - card_name=Healing Totem, mana=1, attack=0, health=2)
3: MinionCardSlot - card_name=Healing Totem, mana=1, attack=0, health=2)
4: SpellCardSlot - card_name=Coin, mana=0

\t0: MinionCardSlot - card_name=Healing Totem, mana=1, attack=0, health=2)

Player (0) - health: 5, armour: 0, mana: 99 / 100
0: MinionCardSlot - card_name=Healing Totem, mana=1, attack=0, health=2)
1: MinionCardSlot - card_name=Healing Totem, mana=1, attack=0, health=2)
2: MinionCardSlot - card_name=Healing Totem, mana=1, attack=0, health=2)

0 plays Healing Totem
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Healing Totem, mana=1, attack=0, health=2)
1: MinionCardSlot - card_name=Healing Totem, mana=1, attack=0, health=2)
2: MinionCardSlot - card_name=Healing Totem, mana=1, attack=0, health=2)
3: MinionCardSlot - card_name=Healing Totem, mana=1, attack=0, health=2)
4: SpellCardSlot - card_name=Coin, mana=0

\t0: MinionCardSlot - card_name=Healing Totem, mana=1, attack=0, health=2)
\t1: MinionCardSlot - card_name=Healing Totem, mana=1, attack=0, health=2)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Healing Totem, mana=1, attack=0, health=2)
1: MinionCardSlot - card_name=Healing Totem, mana=1, attack=0, health=2)

------------------------------
1 turn
------------------------------
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Healing Totem, mana=1, attack=0, health=2)
1: MinionCardSlot - card_name=Healing Totem, mana=1, attack=0, health=2)
2: MinionCardSlot - card_name=Healing Totem, mana=1, attack=0, health=2)
3: MinionCardSlot - card_name=Healing Totem, mana=1, attack=0, health=2)
4: SpellCardSlot - card_name=Coin, mana=0
5: MinionCardSlot - card_name=Healing Totem, mana=1, attack=0, health=2)

\t0: MinionCardSlot - card_name=Healing Totem, mana=1, attack=0, health=2)
\t1: MinionCardSlot - card_name=Healing Totem, mana=1, attack=0, health=2)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Healing Totem, mana=1, attack=0, health=2)
1: MinionCardSlot - card_name=Healing Totem, mana=1, attack=0, health=2)

1 plays Healing Totem
Opponent (1) - health: 5, armour: 0, mana: 99 / 100
Weapon: None
0: MinionCardSlot - card_name=Healing Totem, mana=1, attack=0, health=2)
1: MinionCardSlot - card_name=Healing Totem, mana=1, attack=0, health=2)
2: MinionCardSlot - card_name=Healing Totem, mana=1, attack=0, health=2)
3: SpellCardSlot - card_name=Coin, mana=0
4: MinionCardSlot - card_name=Healing Totem, mana=1, attack=0, health=2)

\t0: MinionCardSlot - card_name=Healing Totem, mana=1, attack=0, health=2)
\t0: MinionCardSlot - card_name=Healing Totem, mana=1, attack=0, health=2)
\t1: MinionCardSlot - card_name=Healing Totem, mana=1, attack=0, health=2)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Healing Totem, mana=1, attack=0, health=2)
1: MinionCardSlot - card_name=Healing Totem, mana=1, attack=0, health=2)

1 plays Healing Totem
Opponent (1) - health: 5, armour: 0, mana: 98 / 100
Weapon: None
0: MinionCardSlot - card_name=Healing Totem, mana=1, attack=0, health=2)
1: MinionCardSlot - card_name=Healing Totem, mana=1, attack=0, health=2)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Healing Totem, mana=1, attack=0, health=2)

\t0: MinionCardSlot - card_name=Healing Totem, mana=1, attack=0, health=2)
\t1: MinionCardSlot - card_name=Healing Totem, mana=1, attack=0, health=2)
\t0: MinionCardSlot - card_name=Healing Totem, mana=1, attack=0, health=2)
\t1: MinionCardSlot - card_name=Healing Totem, mana=1, attack=0, health=2)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Healing Totem, mana=1, attack=0, health=2)
1: MinionCardSlot - card_name=Healing Totem, mana=1, attack=0, health=2)

Opponent (1) - health: 5, armour: 0, mana: 98 / 100
Weapon: None
0: MinionCardSlot - card_name=Healing Totem, mana=1, attack=0, health=2)
1: MinionCardSlot - card_name=Healing Totem, mana=1, attack=0, health=2)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Healing Totem, mana=1, attack=0, health=2)

\t0: MinionCardSlot - card_name=Healing Totem, mana=1, attack=0, health=2)
\t1: MinionCardSlot - card_name=Healing Totem, mana=1, attack=0, health=2)
\t0: MinionCardSlot - card_name=Healing Totem, mana=1, attack=0, health=2)
\t1: MinionCardSlot - card_name=Healing Totem, mana=1, attack=0, health=2)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Healing Totem, mana=1, attack=0, health=2)
1: MinionCardSlot - card_name=Healing Totem, mana=1, attack=0, health=2)

Game Over: Player 0 wins'''

snapshots['TestBasicsOfHunter::test_card_playing 1'] = '''0 goes first
------------------------------
0 turn
------------------------------
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
4: SpellCardSlot - card_name=Coin, mana=0


Player (0) - health: 5, armour: 0, mana: 100 / 100
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

Opponent (1) - health: 3, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
4: SpellCardSlot - card_name=Coin, mana=0


Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

Opponent (1) - health: 3, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
4: SpellCardSlot - card_name=Coin, mana=0


Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

ERROR: already used the hero power
------------------------------
1 turn
------------------------------
Opponent (1) - health: 3, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
4: SpellCardSlot - card_name=Coin, mana=0
5: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)


Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

Opponent (1) - health: 3, armour: 0, mana: 98 / 100
Weapon: None
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
4: SpellCardSlot - card_name=Coin, mana=0
5: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)


Player (0) - health: 3, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

Opponent (1) - health: 3, armour: 0, mana: 98 / 100
Weapon: None
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
4: SpellCardSlot - card_name=Coin, mana=0
5: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)


Player (0) - health: 3, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

ERROR: already used the hero power
Opponent (1) - health: 3, armour: 0, mana: 98 / 100
Weapon: None
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
4: SpellCardSlot - card_name=Coin, mana=0
5: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)


Player (0) - health: 3, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

Game Over: Player 0 wins'''

snapshots['TestBasicsOfLeperGnome::test_card_attacking 1'] = '''0 goes first
------------------------------
0 turn
------------------------------
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)
1: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)
2: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)
3: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)
4: SpellCardSlot - card_name=Coin, mana=0


Player (0) - health: 5, armour: 0, mana: 100 / 100
0: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)
1: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)
2: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)
3: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)

0 plays Leper Gnome
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)
1: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)
2: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)
3: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)
4: SpellCardSlot - card_name=Coin, mana=0

\t0: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)

Player (0) - health: 5, armour: 0, mana: 99 / 100
0: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)
1: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)
2: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)

0 plays Leper Gnome
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)
1: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)
2: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)
3: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)
4: SpellCardSlot - card_name=Coin, mana=0

\t0: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)
\t1: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)
1: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)

------------------------------
1 turn
------------------------------
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)
1: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)
2: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)
3: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)
4: SpellCardSlot - card_name=Coin, mana=0
5: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)

\t0: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)
\t1: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)
1: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)

1 plays Leper Gnome
Opponent (1) - health: 5, armour: 0, mana: 99 / 100
Weapon: None
0: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)
1: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)
2: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)
3: SpellCardSlot - card_name=Coin, mana=0
4: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)

\t0: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)
\t0: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)
\t1: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)
1: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)

1 plays Leper Gnome
Opponent (1) - health: 5, armour: 0, mana: 98 / 100
Weapon: None
0: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)
1: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)

\t0: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)
\t1: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)
\t0: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)
\t1: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)
1: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)

------------------------------
0 turn
------------------------------
Opponent (1) - health: 5, armour: 0, mana: 98 / 100
Weapon: None
0: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)
1: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)

\t0: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)
\t1: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)
\t0: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)
\t1: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)

Player (0) - health: 5, armour: 0, mana: 100 / 100
0: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)
1: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)
2: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)

MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1) attacks MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)
MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=-1) died
MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=-1) died
Opponent (1) - health: 3, armour: 0, mana: 98 / 100
Weapon: None
0: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)
1: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)

\t0: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)
\t0: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)

Player (0) - health: 3, armour: 0, mana: 100 / 100
0: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)
1: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)
2: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)

0 plays Leper Gnome
Opponent (1) - health: 3, armour: 0, mana: 98 / 100
Weapon: None
0: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)
1: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)

\t0: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)
\t0: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)
\t1: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)

Player (0) - health: 3, armour: 0, mana: 99 / 100
0: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)
1: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)

0 plays Leper Gnome
Opponent (1) - health: 3, armour: 0, mana: 98 / 100
Weapon: None
0: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)
1: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)

\t0: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)
\t0: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)
\t1: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)
\t2: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)

Player (0) - health: 3, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)

------------------------------
1 turn
------------------------------
Opponent (1) - health: 3, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)
1: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)
4: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)

\t0: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)
\t0: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)
\t1: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)
\t2: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)

Player (0) - health: 3, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)

MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1) attacks MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)
MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=-1) died
MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=-1) died
Opponent (1) - health: 1, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)
1: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)
4: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)

\t0: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)
\t1: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)

Player (0) - health: 1, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)

1 plays Leper Gnome
Opponent (1) - health: 1, armour: 0, mana: 99 / 100
Weapon: None
0: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)
1: SpellCardSlot - card_name=Coin, mana=0
2: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)
3: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)

\t0: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)
\t0: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)
\t1: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)

Player (0) - health: 1, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)

1 plays Leper Gnome
Opponent (1) - health: 1, armour: 0, mana: 98 / 100
Weapon: None
0: SpellCardSlot - card_name=Coin, mana=0
1: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)
2: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)

\t0: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)
\t1: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)
\t0: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)
\t1: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)

Player (0) - health: 1, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)

Opponent (1) - health: 1, armour: 0, mana: 98 / 100
Weapon: None
0: SpellCardSlot - card_name=Coin, mana=0
1: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)
2: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)

\t0: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)
\t1: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)
\t0: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)
\t1: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)

Player (0) - health: 1, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)

Game Over: Player 0 wins'''

snapshots['TestBasicsOfLeperGnome::test_card_playing 1'] = '''0 goes first
------------------------------
0 turn
------------------------------
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)
1: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)
2: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)
3: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)
4: SpellCardSlot - card_name=Coin, mana=0


Player (0) - health: 5, armour: 0, mana: 100 / 100
0: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)
1: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)
2: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)
3: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)

0 plays Leper Gnome
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)
1: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)
2: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)
3: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)
4: SpellCardSlot - card_name=Coin, mana=0

\t0: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)

Player (0) - health: 5, armour: 0, mana: 99 / 100
0: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)
1: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)
2: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)

0 plays Leper Gnome
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)
1: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)
2: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)
3: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)
4: SpellCardSlot - card_name=Coin, mana=0

\t0: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)
\t1: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)
1: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)

------------------------------
1 turn
------------------------------
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)
1: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)
2: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)
3: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)
4: SpellCardSlot - card_name=Coin, mana=0
5: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)

\t0: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)
\t1: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)
1: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)

1 plays Leper Gnome
Opponent (1) - health: 5, armour: 0, mana: 99 / 100
Weapon: None
0: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)
1: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)
2: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)
3: SpellCardSlot - card_name=Coin, mana=0
4: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)

\t0: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)
\t0: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)
\t1: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)
1: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)

1 plays Leper Gnome
Opponent (1) - health: 5, armour: 0, mana: 98 / 100
Weapon: None
0: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)
1: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)

\t0: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)
\t1: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)
\t0: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)
\t1: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)
1: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)

Opponent (1) - health: 5, armour: 0, mana: 98 / 100
Weapon: None
0: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)
1: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)

\t0: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)
\t1: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)
\t0: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)
\t1: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)
1: MinionCardSlot - card_name=Leper Gnome, mana=1, attack=2, health=1)

Game Over: Player 0 wins'''

snapshots['TestBasicsOfLootHoarder::test_card_attacking 1'] = '''0 goes first
------------------------------
0 turn
------------------------------
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
1: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
2: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
3: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
4: SpellCardSlot - card_name=Coin, mana=0


Player (0) - health: 5, armour: 0, mana: 100 / 100
0: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
1: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
2: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
3: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)

0 plays Loot Hoarder
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
1: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
2: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
3: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
4: SpellCardSlot - card_name=Coin, mana=0

\t0: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
1: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
2: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)

0 plays Loot Hoarder
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
1: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
2: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
3: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
4: SpellCardSlot - card_name=Coin, mana=0

\t0: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
\t1: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)

Player (0) - health: 5, armour: 0, mana: 96 / 100
0: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
1: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)

------------------------------
1 turn
------------------------------
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
1: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
2: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
3: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
4: SpellCardSlot - card_name=Coin, mana=0
5: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)

\t0: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
\t1: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)

Player (0) - health: 5, armour: 0, mana: 96 / 100
0: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
1: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)

1 plays Loot Hoarder
Opponent (1) - health: 5, armour: 0, mana: 98 / 100
Weapon: None
0: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
1: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
2: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
3: SpellCardSlot - card_name=Coin, mana=0
4: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)

\t0: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
\t0: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
\t1: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)

Player (0) - health: 5, armour: 0, mana: 96 / 100
0: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
1: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)

1 plays Loot Hoarder
Opponent (1) - health: 5, armour: 0, mana: 96 / 100
Weapon: None
0: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
1: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)

\t0: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
\t1: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
\t0: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
\t1: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)

Player (0) - health: 5, armour: 0, mana: 96 / 100
0: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
1: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)

------------------------------
0 turn
------------------------------
Opponent (1) - health: 5, armour: 0, mana: 96 / 100
Weapon: None
0: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
1: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)

\t0: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
\t1: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
\t0: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
\t1: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)

Player (0) - health: 5, armour: 0, mana: 100 / 100
0: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
1: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
2: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)

MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1) attacks MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=-1) died
MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=-1) died
Opponent (1) - health: 5, armour: 0, mana: 96 / 100
Weapon: None
0: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
1: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
4: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)

\t0: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
\t0: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)

Player (0) - health: 5, armour: 0, mana: 100 / 100
0: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
1: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
2: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
3: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)

0 plays Loot Hoarder
Opponent (1) - health: 5, armour: 0, mana: 96 / 100
Weapon: None
0: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
1: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
4: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)

\t0: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
\t0: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
\t1: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
1: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
2: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)

0 plays Loot Hoarder
Opponent (1) - health: 5, armour: 0, mana: 96 / 100
Weapon: None
0: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
1: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
4: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)

\t0: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
\t0: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
\t1: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
\t2: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)

Player (0) - health: 5, armour: 0, mana: 96 / 100
0: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
1: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)

------------------------------
1 turn
------------------------------
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
1: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
4: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
5: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)

\t0: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
\t0: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
\t1: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
\t2: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)

Player (0) - health: 5, armour: 0, mana: 96 / 100
0: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
1: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)

MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1) attacks MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=-1) died
MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=-1) died
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
1: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
4: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
5: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
6: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)

\t0: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
\t1: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)

Player (0) - health: 5, armour: 0, mana: 96 / 100
0: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
1: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
2: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)

1 plays Loot Hoarder
Opponent (1) - health: 5, armour: 0, mana: 98 / 100
Weapon: None
0: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
1: SpellCardSlot - card_name=Coin, mana=0
2: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
3: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
4: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
5: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)

\t0: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
\t0: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
\t1: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)

Player (0) - health: 5, armour: 0, mana: 96 / 100
0: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
1: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
2: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)

1 plays Loot Hoarder
Opponent (1) - health: 5, armour: 0, mana: 96 / 100
Weapon: None
0: SpellCardSlot - card_name=Coin, mana=0
1: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
2: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
3: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
4: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)

\t0: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
\t1: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
\t0: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
\t1: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)

Player (0) - health: 5, armour: 0, mana: 96 / 100
0: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
1: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
2: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)

Opponent (1) - health: 5, armour: 0, mana: 96 / 100
Weapon: None
0: SpellCardSlot - card_name=Coin, mana=0
1: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
2: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
3: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
4: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)

\t0: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
\t1: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
\t0: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
\t1: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)

Player (0) - health: 5, armour: 0, mana: 96 / 100
0: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
1: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
2: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)

Game Over: Player 0 wins'''

snapshots['TestBasicsOfLootHoarder::test_card_playing 1'] = '''0 goes first
------------------------------
0 turn
------------------------------
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
1: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
2: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
3: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
4: SpellCardSlot - card_name=Coin, mana=0


Player (0) - health: 5, armour: 0, mana: 100 / 100
0: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
1: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
2: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
3: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)

0 plays Loot Hoarder
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
1: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
2: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
3: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
4: SpellCardSlot - card_name=Coin, mana=0

\t0: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
1: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
2: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)

0 plays Loot Hoarder
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
1: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
2: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
3: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
4: SpellCardSlot - card_name=Coin, mana=0

\t0: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
\t1: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)

Player (0) - health: 5, armour: 0, mana: 96 / 100
0: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
1: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)

------------------------------
1 turn
------------------------------
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
1: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
2: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
3: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
4: SpellCardSlot - card_name=Coin, mana=0
5: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)

\t0: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
\t1: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)

Player (0) - health: 5, armour: 0, mana: 96 / 100
0: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
1: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)

1 plays Loot Hoarder
Opponent (1) - health: 5, armour: 0, mana: 98 / 100
Weapon: None
0: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
1: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
2: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
3: SpellCardSlot - card_name=Coin, mana=0
4: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)

\t0: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
\t0: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
\t1: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)

Player (0) - health: 5, armour: 0, mana: 96 / 100
0: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
1: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)

1 plays Loot Hoarder
Opponent (1) - health: 5, armour: 0, mana: 96 / 100
Weapon: None
0: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
1: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)

\t0: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
\t1: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
\t0: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
\t1: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)

Player (0) - health: 5, armour: 0, mana: 96 / 100
0: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
1: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)

Opponent (1) - health: 5, armour: 0, mana: 96 / 100
Weapon: None
0: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
1: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)

\t0: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
\t1: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
\t0: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
\t1: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)

Player (0) - health: 5, armour: 0, mana: 96 / 100
0: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)
1: MinionCardSlot - card_name=Loot Hoarder, mana=2, attack=2, health=1)

Game Over: Player 0 wins'''

snapshots['TestBasicsOfMadBomber::test_card_attacking 1'] = '''0 goes first
------------------------------
0 turn
------------------------------
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=2)
1: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=2)
2: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=2)
3: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=2)
4: SpellCardSlot - card_name=Coin, mana=0


Player (0) - health: 5, armour: 0, mana: 100 / 100
0: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=2)
1: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=2)
2: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=2)
3: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=2)

0 plays Mad Bomber
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=2)
1: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=2)
2: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=2)
3: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=2)
4: SpellCardSlot - card_name=Coin, mana=0

\t0: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=0)

Player (0) - health: 4, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=2)
1: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=2)
2: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=2)

0 plays Mad Bomber
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=2)
1: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=2)
2: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=2)
3: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=2)
4: SpellCardSlot - card_name=Coin, mana=0

\t0: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=0)
\t1: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=-1)

Player (0) - health: 4, armour: 0, mana: 96 / 100
0: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=2)
1: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=2)

------------------------------
1 turn
------------------------------
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=2)
1: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=2)
2: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=2)
3: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=2)
4: SpellCardSlot - card_name=Coin, mana=0
5: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=2)

\t0: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=0)
\t1: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=-1)

Player (0) - health: 4, armour: 0, mana: 96 / 100
0: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=2)
1: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=2)

1 plays Mad Bomber
Opponent (1) - health: 5, armour: 0, mana: 98 / 100
Weapon: None
0: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=2)
1: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=2)
2: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=2)
3: SpellCardSlot - card_name=Coin, mana=0
4: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=2)

\t0: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=-1)
\t0: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=0)
\t1: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=-1)

Player (0) - health: 4, armour: 0, mana: 96 / 100
0: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=2)
1: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=2)

1 plays Mad Bomber
Opponent (1) - health: 4, armour: 0, mana: 96 / 100
Weapon: None
0: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=2)
1: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=2)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=2)

\t0: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=1)
\t1: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=-2)
\t0: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=0)
\t1: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=-1)

Player (0) - health: 4, armour: 0, mana: 96 / 100
0: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=2)
1: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=2)

------------------------------
0 turn
------------------------------
Opponent (1) - health: 4, armour: 0, mana: 96 / 100
Weapon: None
0: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=2)
1: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=2)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=2)

\t0: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=1)
\t1: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=-2)
\t0: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=0)
\t1: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=-1)

Player (0) - health: 4, armour: 0, mana: 100 / 100
0: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=2)
1: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=2)
2: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=2)

MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=0) attacks MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=1)
MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=-3) died
MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=-2) died
Opponent (1) - health: 4, armour: 0, mana: 96 / 100
Weapon: None
0: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=2)
1: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=2)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=2)

\t0: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=-2)
\t0: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=-1)

Player (0) - health: 4, armour: 0, mana: 100 / 100
0: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=2)
1: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=2)
2: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=2)

0 plays Mad Bomber
Opponent (1) - health: 4, armour: 0, mana: 96 / 100
Weapon: None
0: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=2)
1: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=2)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=2)

\t0: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=-2)
\t0: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=1)
\t1: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=-2)

Player (0) - health: 3, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=2)
1: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=2)

0 plays Mad Bomber
Opponent (1) - health: 4, armour: 0, mana: 96 / 100
Weapon: None
0: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=2)
1: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=2)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=2)

\t0: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=-2)
\t0: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=1)
\t1: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=0)
\t2: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=-2)

Player (0) - health: 2, armour: 0, mana: 96 / 100
0: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=2)

------------------------------
1 turn
------------------------------
Opponent (1) - health: 4, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=2)
1: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=2)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=2)
4: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=2)

\t0: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=-2)
\t0: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=1)
\t1: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=0)
\t2: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=-2)

Player (0) - health: 2, armour: 0, mana: 96 / 100
0: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=2)

MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=-2) attacks MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=1)
MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=-5) died
MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=-2) died
Opponent (1) - health: 4, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=2)
1: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=2)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=2)
4: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=2)

\t0: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=0)
\t1: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=-2)

Player (0) - health: 2, armour: 0, mana: 96 / 100
0: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=2)

1 plays Mad Bomber
Opponent (1) - health: 2, armour: 0, mana: 98 / 100
Weapon: None
0: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=2)
1: SpellCardSlot - card_name=Coin, mana=0
2: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=2)
3: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=2)

\t0: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=1)
\t0: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=0)
\t1: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=-2)

Player (0) - health: 2, armour: 0, mana: 96 / 100
0: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=2)

1 plays Mad Bomber
Opponent (1) - health: 1, armour: 0, mana: 96 / 100
Weapon: None
0: SpellCardSlot - card_name=Coin, mana=0
1: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=2)
2: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=2)

\t0: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=2)
\t1: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=-1)
\t0: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=0)
\t1: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=-2)

Player (0) - health: 2, armour: 0, mana: 96 / 100
0: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=2)

Opponent (1) - health: 1, armour: 0, mana: 96 / 100
Weapon: None
0: SpellCardSlot - card_name=Coin, mana=0
1: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=2)
2: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=2)

\t0: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=2)
\t1: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=-1)
\t0: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=0)
\t1: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=-2)

Player (0) - health: 2, armour: 0, mana: 96 / 100
0: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=2)

Game Over: Player 0 wins'''

snapshots['TestBasicsOfMadBomber::test_card_playing 1'] = '''0 goes first
------------------------------
0 turn
------------------------------
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=2)
1: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=2)
2: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=2)
3: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=2)
4: SpellCardSlot - card_name=Coin, mana=0


Player (0) - health: 5, armour: 0, mana: 100 / 100
0: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=2)
1: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=2)
2: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=2)
3: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=2)

0 plays Mad Bomber
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=2)
1: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=2)
2: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=2)
3: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=2)
4: SpellCardSlot - card_name=Coin, mana=0

\t0: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=0)

Player (0) - health: 4, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=2)
1: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=2)
2: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=2)

0 plays Mad Bomber
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=2)
1: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=2)
2: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=2)
3: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=2)
4: SpellCardSlot - card_name=Coin, mana=0

\t0: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=0)
\t1: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=-1)

Player (0) - health: 4, armour: 0, mana: 96 / 100
0: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=2)
1: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=2)

------------------------------
1 turn
------------------------------
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=2)
1: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=2)
2: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=2)
3: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=2)
4: SpellCardSlot - card_name=Coin, mana=0
5: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=2)

\t0: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=0)
\t1: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=-1)

Player (0) - health: 4, armour: 0, mana: 96 / 100
0: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=2)
1: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=2)

1 plays Mad Bomber
Opponent (1) - health: 5, armour: 0, mana: 98 / 100
Weapon: None
0: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=2)
1: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=2)
2: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=2)
3: SpellCardSlot - card_name=Coin, mana=0
4: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=2)

\t0: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=-1)
\t0: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=0)
\t1: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=-1)

Player (0) - health: 4, armour: 0, mana: 96 / 100
0: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=2)
1: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=2)

1 plays Mad Bomber
Opponent (1) - health: 4, armour: 0, mana: 96 / 100
Weapon: None
0: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=2)
1: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=2)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=2)

\t0: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=1)
\t1: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=-2)
\t0: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=0)
\t1: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=-1)

Player (0) - health: 4, armour: 0, mana: 96 / 100
0: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=2)
1: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=2)

Opponent (1) - health: 4, armour: 0, mana: 96 / 100
Weapon: None
0: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=2)
1: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=2)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=2)

\t0: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=1)
\t1: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=-2)
\t0: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=0)
\t1: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=-1)

Player (0) - health: 4, armour: 0, mana: 96 / 100
0: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=2)
1: MinionCardSlot - card_name=Mad Bomber, mana=2, attack=3, health=2)

Game Over: Player 0 wins'''

snapshots['TestBasicsOfMage::test_card_playing 1'] = '''0 goes first
------------------------------
0 turn
------------------------------
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
4: SpellCardSlot - card_name=Coin, mana=0


Player (0) - health: 5, armour: 0, mana: 100 / 100
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
4: SpellCardSlot - card_name=Coin, mana=0


Player (0) - health: 4, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
4: SpellCardSlot - card_name=Coin, mana=0


Player (0) - health: 4, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

ERROR: already used the hero power
------------------------------
1 turn
------------------------------
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
4: SpellCardSlot - card_name=Coin, mana=0
5: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)


Player (0) - health: 4, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

Opponent (1) - health: 5, armour: 0, mana: 98 / 100
Weapon: None
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
4: SpellCardSlot - card_name=Coin, mana=0
5: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)


Player (0) - health: 3, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

Opponent (1) - health: 5, armour: 0, mana: 98 / 100
Weapon: None
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
4: SpellCardSlot - card_name=Coin, mana=0
5: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)


Player (0) - health: 3, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

ERROR: already used the hero power
Opponent (1) - health: 5, armour: 0, mana: 98 / 100
Weapon: None
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
4: SpellCardSlot - card_name=Coin, mana=0
5: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)


Player (0) - health: 3, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

Game Over: Player 0 wins'''

snapshots['TestBasicsOfPaladin::test_card_playing 1'] = '''0 goes first
------------------------------
0 turn
------------------------------
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
4: SpellCardSlot - card_name=Coin, mana=0


Player (0) - health: 5, armour: 0, mana: 100 / 100
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

0 summons Silver Hand Recruit
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
4: SpellCardSlot - card_name=Coin, mana=0

\t0: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
4: SpellCardSlot - card_name=Coin, mana=0

\t0: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

ERROR: already used the hero power
------------------------------
1 turn
------------------------------
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
4: SpellCardSlot - card_name=Coin, mana=0
5: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

\t0: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

1 summons Silver Hand Recruit
Opponent (1) - health: 5, armour: 0, mana: 98 / 100
Weapon: None
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
4: SpellCardSlot - card_name=Coin, mana=0
5: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

\t0: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)
\t0: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

Opponent (1) - health: 5, armour: 0, mana: 98 / 100
Weapon: None
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
4: SpellCardSlot - card_name=Coin, mana=0
5: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

\t0: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)
\t0: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

ERROR: already used the hero power
Opponent (1) - health: 5, armour: 0, mana: 98 / 100
Weapon: None
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
4: SpellCardSlot - card_name=Coin, mana=0
5: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

\t0: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)
\t0: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

Game Over: Player 0 wins'''

snapshots['TestBasicsOfPriest::test_card_playing 1'] = '''0 goes first
------------------------------
0 turn
------------------------------
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
4: SpellCardSlot - card_name=Coin, mana=0


Player (0) - health: 5, armour: 0, mana: 100 / 100
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
4: SpellCardSlot - card_name=Coin, mana=0


Player (0) - health: 7, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
4: SpellCardSlot - card_name=Coin, mana=0


Player (0) - health: 7, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

ERROR: already used the hero power
------------------------------
1 turn
------------------------------
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
4: SpellCardSlot - card_name=Coin, mana=0
5: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)


Player (0) - health: 7, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

Opponent (1) - health: 5, armour: 0, mana: 98 / 100
Weapon: None
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
4: SpellCardSlot - card_name=Coin, mana=0
5: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)


Player (0) - health: 9, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

Opponent (1) - health: 5, armour: 0, mana: 98 / 100
Weapon: None
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
4: SpellCardSlot - card_name=Coin, mana=0
5: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)


Player (0) - health: 9, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

ERROR: already used the hero power
Opponent (1) - health: 5, armour: 0, mana: 98 / 100
Weapon: None
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
4: SpellCardSlot - card_name=Coin, mana=0
5: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)


Player (0) - health: 9, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

Game Over: Player 0 wins'''

snapshots['TestBasicsOfRogue::test_card_playing 1'] = '''0 goes first
------------------------------
0 turn
------------------------------
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
4: SpellCardSlot - card_name=Coin, mana=0


Player (0) - health: 5, armour: 0, mana: 100 / 100
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
4: SpellCardSlot - card_name=Coin, mana=0


Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
4: SpellCardSlot - card_name=Coin, mana=0


Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

ERROR: already used the hero power
------------------------------
1 turn
------------------------------
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
4: SpellCardSlot - card_name=Coin, mana=0
5: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)


Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

Opponent (1) - health: 5, armour: 0, mana: 98 / 100
Weapon: Rogue Dagger 1/2, 1 attack, 2 durability
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
4: SpellCardSlot - card_name=Coin, mana=0
5: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)


Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

Opponent (1) - health: 5, armour: 0, mana: 98 / 100
Weapon: Rogue Dagger 1/2, 1 attack, 2 durability
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
4: SpellCardSlot - card_name=Coin, mana=0
5: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)


Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

ERROR: already used the hero power
Opponent (1) - health: 5, armour: 0, mana: 98 / 100
Weapon: Rogue Dagger 1/2, 1 attack, 2 durability
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
4: SpellCardSlot - card_name=Coin, mana=0
5: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)


Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

Game Over: Player 0 wins'''

snapshots['TestBasicsOfSearingTotem::test_card_attacking 1'] = '''0 goes first
------------------------------
0 turn
------------------------------
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)
2: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)
3: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)
4: SpellCardSlot - card_name=Coin, mana=0


Player (0) - health: 5, armour: 0, mana: 100 / 100
0: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)
2: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)
3: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)

0 plays Searing Totem
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)
2: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)
3: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)
4: SpellCardSlot - card_name=Coin, mana=0

\t0: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)

Player (0) - health: 5, armour: 0, mana: 99 / 100
0: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)
2: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)

0 plays Searing Totem
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)
2: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)
3: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)
4: SpellCardSlot - card_name=Coin, mana=0

\t0: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)
\t1: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)

------------------------------
1 turn
------------------------------
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)
2: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)
3: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)
4: SpellCardSlot - card_name=Coin, mana=0
5: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)

\t0: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)
\t1: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)

1 plays Searing Totem
Opponent (1) - health: 5, armour: 0, mana: 99 / 100
Weapon: None
0: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)
2: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)
3: SpellCardSlot - card_name=Coin, mana=0
4: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)

\t0: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)
\t0: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)
\t1: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)

1 plays Searing Totem
Opponent (1) - health: 5, armour: 0, mana: 98 / 100
Weapon: None
0: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)

\t0: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)
\t1: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)
\t0: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)
\t1: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)

------------------------------
0 turn
------------------------------
Opponent (1) - health: 5, armour: 0, mana: 98 / 100
Weapon: None
0: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)

\t0: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)
\t1: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)
\t0: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)
\t1: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)

Player (0) - health: 5, armour: 0, mana: 100 / 100
0: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)
2: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)

MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1) attacks MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)
MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=0) died
MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=0) died
Opponent (1) - health: 5, armour: 0, mana: 98 / 100
Weapon: None
0: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)

\t0: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)
\t0: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)

Player (0) - health: 5, armour: 0, mana: 100 / 100
0: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)
2: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)

0 plays Searing Totem
Opponent (1) - health: 5, armour: 0, mana: 98 / 100
Weapon: None
0: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)

\t0: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)
\t0: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)
\t1: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)

Player (0) - health: 5, armour: 0, mana: 99 / 100
0: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)

0 plays Searing Totem
Opponent (1) - health: 5, armour: 0, mana: 98 / 100
Weapon: None
0: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)

\t0: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)
\t0: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)
\t1: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)
\t2: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)

------------------------------
1 turn
------------------------------
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)
4: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)

\t0: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)
\t0: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)
\t1: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)
\t2: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)

MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1) attacks MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)
MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=0) died
MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=0) died
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)
4: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)

\t0: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)
\t1: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)

1 plays Searing Totem
Opponent (1) - health: 5, armour: 0, mana: 99 / 100
Weapon: None
0: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)
1: SpellCardSlot - card_name=Coin, mana=0
2: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)
3: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)

\t0: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)
\t0: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)
\t1: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)

1 plays Searing Totem
Opponent (1) - health: 5, armour: 0, mana: 98 / 100
Weapon: None
0: SpellCardSlot - card_name=Coin, mana=0
1: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)
2: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)

\t0: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)
\t1: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)
\t0: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)
\t1: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)

Opponent (1) - health: 5, armour: 0, mana: 98 / 100
Weapon: None
0: SpellCardSlot - card_name=Coin, mana=0
1: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)
2: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)

\t0: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)
\t1: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)
\t0: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)
\t1: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)

Game Over: Player 0 wins'''

snapshots['TestBasicsOfSearingTotem::test_card_playing 1'] = '''0 goes first
------------------------------
0 turn
------------------------------
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)
2: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)
3: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)
4: SpellCardSlot - card_name=Coin, mana=0


Player (0) - health: 5, armour: 0, mana: 100 / 100
0: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)
2: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)
3: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)

0 plays Searing Totem
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)
2: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)
3: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)
4: SpellCardSlot - card_name=Coin, mana=0

\t0: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)

Player (0) - health: 5, armour: 0, mana: 99 / 100
0: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)
2: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)

0 plays Searing Totem
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)
2: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)
3: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)
4: SpellCardSlot - card_name=Coin, mana=0

\t0: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)
\t1: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)

------------------------------
1 turn
------------------------------
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)
2: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)
3: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)
4: SpellCardSlot - card_name=Coin, mana=0
5: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)

\t0: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)
\t1: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)

1 plays Searing Totem
Opponent (1) - health: 5, armour: 0, mana: 99 / 100
Weapon: None
0: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)
2: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)
3: SpellCardSlot - card_name=Coin, mana=0
4: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)

\t0: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)
\t0: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)
\t1: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)

1 plays Searing Totem
Opponent (1) - health: 5, armour: 0, mana: 98 / 100
Weapon: None
0: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)

\t0: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)
\t1: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)
\t0: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)
\t1: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)

Opponent (1) - health: 5, armour: 0, mana: 98 / 100
Weapon: None
0: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)

\t0: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)
\t1: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)
\t0: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)
\t1: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Searing Totem, mana=1, attack=1, health=1)

Game Over: Player 0 wins'''

snapshots['TestBasicsOfShaman::test_card_playing 1'] = '''0 goes first
------------------------------
0 turn
------------------------------
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
4: SpellCardSlot - card_name=Coin, mana=0


Player (0) - health: 5, armour: 0, mana: 100 / 100
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

0 summons Healing Totem
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
4: SpellCardSlot - card_name=Coin, mana=0

\t0: MinionCardSlot - card_name=Healing Totem, mana=1, attack=0, health=2)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
4: SpellCardSlot - card_name=Coin, mana=0

\t0: MinionCardSlot - card_name=Healing Totem, mana=1, attack=0, health=2)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

ERROR: already used the hero power
------------------------------
1 turn
------------------------------
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
4: SpellCardSlot - card_name=Coin, mana=0
5: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

\t0: MinionCardSlot - card_name=Healing Totem, mana=1, attack=0, health=2)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

1 summons Healing Totem
Opponent (1) - health: 5, armour: 0, mana: 98 / 100
Weapon: None
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
4: SpellCardSlot - card_name=Coin, mana=0
5: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

\t0: MinionCardSlot - card_name=Healing Totem, mana=1, attack=0, health=2)
\t0: MinionCardSlot - card_name=Healing Totem, mana=1, attack=0, health=2)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

Opponent (1) - health: 5, armour: 0, mana: 98 / 100
Weapon: None
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
4: SpellCardSlot - card_name=Coin, mana=0
5: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

\t0: MinionCardSlot - card_name=Healing Totem, mana=1, attack=0, health=2)
\t0: MinionCardSlot - card_name=Healing Totem, mana=1, attack=0, health=2)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

ERROR: already used the hero power
Opponent (1) - health: 5, armour: 0, mana: 98 / 100
Weapon: None
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
4: SpellCardSlot - card_name=Coin, mana=0
5: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

\t0: MinionCardSlot - card_name=Healing Totem, mana=1, attack=0, health=2)
\t0: MinionCardSlot - card_name=Healing Totem, mana=1, attack=0, health=2)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

Game Over: Player 0 wins'''

snapshots['TestBasicsOfShieldbearer::test_card_playing 1'] = '''0 goes first
------------------------------
0 turn
------------------------------
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Shieldbearer, mana=1, attack=0, health=4)
1: MinionCardSlot - card_name=Shieldbearer, mana=1, attack=0, health=4)
2: MinionCardSlot - card_name=Shieldbearer, mana=1, attack=0, health=4)
3: MinionCardSlot - card_name=Shieldbearer, mana=1, attack=0, health=4)
4: SpellCardSlot - card_name=Coin, mana=0


Player (0) - health: 5, armour: 0, mana: 100 / 100
0: MinionCardSlot - card_name=Shieldbearer, mana=1, attack=0, health=4)
1: MinionCardSlot - card_name=Shieldbearer, mana=1, attack=0, health=4)
2: MinionCardSlot - card_name=Shieldbearer, mana=1, attack=0, health=4)
3: MinionCardSlot - card_name=Shieldbearer, mana=1, attack=0, health=4)

0 plays Shieldbearer
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Shieldbearer, mana=1, attack=0, health=4)
1: MinionCardSlot - card_name=Shieldbearer, mana=1, attack=0, health=4)
2: MinionCardSlot - card_name=Shieldbearer, mana=1, attack=0, health=4)
3: MinionCardSlot - card_name=Shieldbearer, mana=1, attack=0, health=4)
4: SpellCardSlot - card_name=Coin, mana=0

\t0: MinionCardSlot - card_name=Shieldbearer, mana=1, attack=0, health=4)

Player (0) - health: 5, armour: 0, mana: 99 / 100
0: MinionCardSlot - card_name=Shieldbearer, mana=1, attack=0, health=4)
1: MinionCardSlot - card_name=Shieldbearer, mana=1, attack=0, health=4)
2: MinionCardSlot - card_name=Shieldbearer, mana=1, attack=0, health=4)

0 plays Shieldbearer
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Shieldbearer, mana=1, attack=0, health=4)
1: MinionCardSlot - card_name=Shieldbearer, mana=1, attack=0, health=4)
2: MinionCardSlot - card_name=Shieldbearer, mana=1, attack=0, health=4)
3: MinionCardSlot - card_name=Shieldbearer, mana=1, attack=0, health=4)
4: SpellCardSlot - card_name=Coin, mana=0

\t0: MinionCardSlot - card_name=Shieldbearer, mana=1, attack=0, health=4)
\t1: MinionCardSlot - card_name=Shieldbearer, mana=1, attack=0, health=4)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Shieldbearer, mana=1, attack=0, health=4)
1: MinionCardSlot - card_name=Shieldbearer, mana=1, attack=0, health=4)

------------------------------
1 turn
------------------------------
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Shieldbearer, mana=1, attack=0, health=4)
1: MinionCardSlot - card_name=Shieldbearer, mana=1, attack=0, health=4)
2: MinionCardSlot - card_name=Shieldbearer, mana=1, attack=0, health=4)
3: MinionCardSlot - card_name=Shieldbearer, mana=1, attack=0, health=4)
4: SpellCardSlot - card_name=Coin, mana=0
5: MinionCardSlot - card_name=Shieldbearer, mana=1, attack=0, health=4)

\t0: MinionCardSlot - card_name=Shieldbearer, mana=1, attack=0, health=4)
\t1: MinionCardSlot - card_name=Shieldbearer, mana=1, attack=0, health=4)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Shieldbearer, mana=1, attack=0, health=4)
1: MinionCardSlot - card_name=Shieldbearer, mana=1, attack=0, health=4)

1 plays Shieldbearer
Opponent (1) - health: 5, armour: 0, mana: 99 / 100
Weapon: None
0: MinionCardSlot - card_name=Shieldbearer, mana=1, attack=0, health=4)
1: MinionCardSlot - card_name=Shieldbearer, mana=1, attack=0, health=4)
2: MinionCardSlot - card_name=Shieldbearer, mana=1, attack=0, health=4)
3: SpellCardSlot - card_name=Coin, mana=0
4: MinionCardSlot - card_name=Shieldbearer, mana=1, attack=0, health=4)

\t0: MinionCardSlot - card_name=Shieldbearer, mana=1, attack=0, health=4)
\t0: MinionCardSlot - card_name=Shieldbearer, mana=1, attack=0, health=4)
\t1: MinionCardSlot - card_name=Shieldbearer, mana=1, attack=0, health=4)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Shieldbearer, mana=1, attack=0, health=4)
1: MinionCardSlot - card_name=Shieldbearer, mana=1, attack=0, health=4)

1 plays Shieldbearer
Opponent (1) - health: 5, armour: 0, mana: 98 / 100
Weapon: None
0: MinionCardSlot - card_name=Shieldbearer, mana=1, attack=0, health=4)
1: MinionCardSlot - card_name=Shieldbearer, mana=1, attack=0, health=4)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Shieldbearer, mana=1, attack=0, health=4)

\t0: MinionCardSlot - card_name=Shieldbearer, mana=1, attack=0, health=4)
\t1: MinionCardSlot - card_name=Shieldbearer, mana=1, attack=0, health=4)
\t0: MinionCardSlot - card_name=Shieldbearer, mana=1, attack=0, health=4)
\t1: MinionCardSlot - card_name=Shieldbearer, mana=1, attack=0, health=4)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Shieldbearer, mana=1, attack=0, health=4)
1: MinionCardSlot - card_name=Shieldbearer, mana=1, attack=0, health=4)

Opponent (1) - health: 5, armour: 0, mana: 98 / 100
Weapon: None
0: MinionCardSlot - card_name=Shieldbearer, mana=1, attack=0, health=4)
1: MinionCardSlot - card_name=Shieldbearer, mana=1, attack=0, health=4)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Shieldbearer, mana=1, attack=0, health=4)

\t0: MinionCardSlot - card_name=Shieldbearer, mana=1, attack=0, health=4)
\t1: MinionCardSlot - card_name=Shieldbearer, mana=1, attack=0, health=4)
\t0: MinionCardSlot - card_name=Shieldbearer, mana=1, attack=0, health=4)
\t1: MinionCardSlot - card_name=Shieldbearer, mana=1, attack=0, health=4)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Shieldbearer, mana=1, attack=0, health=4)
1: MinionCardSlot - card_name=Shieldbearer, mana=1, attack=0, health=4)

Game Over: Player 0 wins'''

snapshots['TestBasicsOfSilverHandRecruit::test_card_attacking 1'] = '''0 goes first
------------------------------
0 turn
------------------------------
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)
2: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)
3: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)
4: SpellCardSlot - card_name=Coin, mana=0


Player (0) - health: 5, armour: 0, mana: 100 / 100
0: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)
2: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)
3: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)

0 plays Silver Hand Recruit
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)
2: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)
3: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)
4: SpellCardSlot - card_name=Coin, mana=0

\t0: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)

Player (0) - health: 5, armour: 0, mana: 99 / 100
0: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)
2: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)

0 plays Silver Hand Recruit
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)
2: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)
3: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)
4: SpellCardSlot - card_name=Coin, mana=0

\t0: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)
\t1: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)

------------------------------
1 turn
------------------------------
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)
2: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)
3: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)
4: SpellCardSlot - card_name=Coin, mana=0
5: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)

\t0: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)
\t1: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)

1 plays Silver Hand Recruit
Opponent (1) - health: 5, armour: 0, mana: 99 / 100
Weapon: None
0: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)
2: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)
3: SpellCardSlot - card_name=Coin, mana=0
4: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)

\t0: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)
\t0: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)
\t1: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)

1 plays Silver Hand Recruit
Opponent (1) - health: 5, armour: 0, mana: 98 / 100
Weapon: None
0: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)

\t0: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)
\t1: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)
\t0: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)
\t1: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)

------------------------------
0 turn
------------------------------
Opponent (1) - health: 5, armour: 0, mana: 98 / 100
Weapon: None
0: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)

\t0: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)
\t1: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)
\t0: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)
\t1: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)

Player (0) - health: 5, armour: 0, mana: 100 / 100
0: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)
2: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)

MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1) attacks MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)
MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=0) died
MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=0) died
Opponent (1) - health: 5, armour: 0, mana: 98 / 100
Weapon: None
0: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)

\t0: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)
\t0: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)

Player (0) - health: 5, armour: 0, mana: 100 / 100
0: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)
2: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)

0 plays Silver Hand Recruit
Opponent (1) - health: 5, armour: 0, mana: 98 / 100
Weapon: None
0: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)

\t0: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)
\t0: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)
\t1: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)

Player (0) - health: 5, armour: 0, mana: 99 / 100
0: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)

0 plays Silver Hand Recruit
Opponent (1) - health: 5, armour: 0, mana: 98 / 100
Weapon: None
0: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)

\t0: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)
\t0: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)
\t1: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)
\t2: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)

------------------------------
1 turn
------------------------------
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)
4: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)

\t0: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)
\t0: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)
\t1: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)
\t2: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)

MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1) attacks MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)
MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=0) died
MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=0) died
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)
4: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)

\t0: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)
\t1: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)

1 plays Silver Hand Recruit
Opponent (1) - health: 5, armour: 0, mana: 99 / 100
Weapon: None
0: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)
1: SpellCardSlot - card_name=Coin, mana=0
2: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)
3: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)

\t0: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)
\t0: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)
\t1: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)

1 plays Silver Hand Recruit
Opponent (1) - health: 5, armour: 0, mana: 98 / 100
Weapon: None
0: SpellCardSlot - card_name=Coin, mana=0
1: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)
2: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)

\t0: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)
\t1: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)
\t0: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)
\t1: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)

Opponent (1) - health: 5, armour: 0, mana: 98 / 100
Weapon: None
0: SpellCardSlot - card_name=Coin, mana=0
1: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)
2: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)

\t0: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)
\t1: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)
\t0: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)
\t1: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)

Game Over: Player 0 wins'''

snapshots['TestBasicsOfSilverHandRecruit::test_card_playing 1'] = '''0 goes first
------------------------------
0 turn
------------------------------
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)
2: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)
3: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)
4: SpellCardSlot - card_name=Coin, mana=0


Player (0) - health: 5, armour: 0, mana: 100 / 100
0: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)
2: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)
3: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)

0 plays Silver Hand Recruit
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)
2: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)
3: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)
4: SpellCardSlot - card_name=Coin, mana=0

\t0: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)

Player (0) - health: 5, armour: 0, mana: 99 / 100
0: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)
2: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)

0 plays Silver Hand Recruit
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)
2: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)
3: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)
4: SpellCardSlot - card_name=Coin, mana=0

\t0: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)
\t1: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)

------------------------------
1 turn
------------------------------
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)
2: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)
3: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)
4: SpellCardSlot - card_name=Coin, mana=0
5: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)

\t0: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)
\t1: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)

1 plays Silver Hand Recruit
Opponent (1) - health: 5, armour: 0, mana: 99 / 100
Weapon: None
0: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)
2: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)
3: SpellCardSlot - card_name=Coin, mana=0
4: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)

\t0: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)
\t0: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)
\t1: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)

1 plays Silver Hand Recruit
Opponent (1) - health: 5, armour: 0, mana: 98 / 100
Weapon: None
0: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)

\t0: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)
\t1: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)
\t0: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)
\t1: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)

Opponent (1) - health: 5, armour: 0, mana: 98 / 100
Weapon: None
0: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)

\t0: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)
\t1: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)
\t0: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)
\t1: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Silver Hand Recruit, mana=1, attack=1, health=1)

Game Over: Player 0 wins'''

snapshots['TestBasicsOfSouthseaDeckhand::test_card_attacking 1'] = '''0 goes first
------------------------------
0 turn
------------------------------
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)
1: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)
2: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)
3: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)
4: SpellCardSlot - card_name=Coin, mana=0


Player (0) - health: 5, armour: 0, mana: 100 / 100
0: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)
1: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)
2: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)
3: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)

0 plays Southsea Deckhand
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)
1: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)
2: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)
3: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)
4: SpellCardSlot - card_name=Coin, mana=0

\t0: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)

Player (0) - health: 5, armour: 0, mana: 99 / 100
0: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)
1: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)
2: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)

0 plays Southsea Deckhand
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)
1: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)
2: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)
3: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)
4: SpellCardSlot - card_name=Coin, mana=0

\t0: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)
\t1: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)
1: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)

------------------------------
1 turn
------------------------------
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)
1: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)
2: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)
3: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)
4: SpellCardSlot - card_name=Coin, mana=0
5: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)

\t0: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)
\t1: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)
1: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)

1 plays Southsea Deckhand
Opponent (1) - health: 5, armour: 0, mana: 99 / 100
Weapon: None
0: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)
1: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)
2: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)
3: SpellCardSlot - card_name=Coin, mana=0
4: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)

\t0: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)
\t0: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)
\t1: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)
1: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)

1 plays Southsea Deckhand
Opponent (1) - health: 5, armour: 0, mana: 98 / 100
Weapon: None
0: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)
1: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)

\t0: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)
\t1: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)
\t0: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)
\t1: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)
1: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)

------------------------------
0 turn
------------------------------
Opponent (1) - health: 5, armour: 0, mana: 98 / 100
Weapon: None
0: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)
1: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)

\t0: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)
\t1: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)
\t0: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)
\t1: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)

Player (0) - health: 5, armour: 0, mana: 100 / 100
0: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)
1: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)
2: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)

MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1) attacks MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)
MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=-1) died
MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=-1) died
Opponent (1) - health: 5, armour: 0, mana: 98 / 100
Weapon: None
0: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)
1: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)

\t0: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)
\t0: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)

Player (0) - health: 5, armour: 0, mana: 100 / 100
0: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)
1: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)
2: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)

0 plays Southsea Deckhand
Opponent (1) - health: 5, armour: 0, mana: 98 / 100
Weapon: None
0: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)
1: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)

\t0: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)
\t0: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)
\t1: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)

Player (0) - health: 5, armour: 0, mana: 99 / 100
0: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)
1: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)

0 plays Southsea Deckhand
Opponent (1) - health: 5, armour: 0, mana: 98 / 100
Weapon: None
0: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)
1: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)

\t0: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)
\t0: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)
\t1: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)
\t2: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)

------------------------------
1 turn
------------------------------
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)
1: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)
4: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)

\t0: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)
\t0: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)
\t1: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)
\t2: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)

MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1) attacks MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)
MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=-1) died
MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=-1) died
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)
1: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)
4: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)

\t0: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)
\t1: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)

1 plays Southsea Deckhand
Opponent (1) - health: 5, armour: 0, mana: 99 / 100
Weapon: None
0: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)
1: SpellCardSlot - card_name=Coin, mana=0
2: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)
3: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)

\t0: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)
\t0: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)
\t1: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)

1 plays Southsea Deckhand
Opponent (1) - health: 5, armour: 0, mana: 98 / 100
Weapon: None
0: SpellCardSlot - card_name=Coin, mana=0
1: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)
2: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)

\t0: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)
\t1: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)
\t0: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)
\t1: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)

Opponent (1) - health: 5, armour: 0, mana: 98 / 100
Weapon: None
0: SpellCardSlot - card_name=Coin, mana=0
1: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)
2: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)

\t0: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)
\t1: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)
\t0: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)
\t1: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)

Game Over: Player 0 wins'''

snapshots['TestBasicsOfSouthseaDeckhand::test_card_playing 1'] = '''0 goes first
------------------------------
0 turn
------------------------------
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)
1: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)
2: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)
3: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)
4: SpellCardSlot - card_name=Coin, mana=0


Player (0) - health: 5, armour: 0, mana: 100 / 100
0: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)
1: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)
2: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)
3: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)

0 plays Southsea Deckhand
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)
1: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)
2: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)
3: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)
4: SpellCardSlot - card_name=Coin, mana=0

\t0: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)

Player (0) - health: 5, armour: 0, mana: 99 / 100
0: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)
1: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)
2: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)

0 plays Southsea Deckhand
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)
1: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)
2: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)
3: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)
4: SpellCardSlot - card_name=Coin, mana=0

\t0: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)
\t1: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)
1: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)

------------------------------
1 turn
------------------------------
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)
1: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)
2: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)
3: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)
4: SpellCardSlot - card_name=Coin, mana=0
5: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)

\t0: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)
\t1: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)
1: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)

1 plays Southsea Deckhand
Opponent (1) - health: 5, armour: 0, mana: 99 / 100
Weapon: None
0: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)
1: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)
2: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)
3: SpellCardSlot - card_name=Coin, mana=0
4: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)

\t0: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)
\t0: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)
\t1: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)
1: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)

1 plays Southsea Deckhand
Opponent (1) - health: 5, armour: 0, mana: 98 / 100
Weapon: None
0: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)
1: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)

\t0: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)
\t1: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)
\t0: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)
\t1: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)
1: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)

Opponent (1) - health: 5, armour: 0, mana: 98 / 100
Weapon: None
0: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)
1: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)

\t0: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)
\t1: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)
\t0: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)
\t1: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)
1: MinionCardSlot - card_name=Southsea Deckhand, mana=1, attack=2, health=1)

Game Over: Player 0 wins'''

snapshots['TestBasicsOfWarlock::test_card_playing 1'] = '''0 goes first
------------------------------
0 turn
------------------------------
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
4: SpellCardSlot - card_name=Coin, mana=0


Player (0) - health: 5, armour: 0, mana: 100 / 100
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
4: SpellCardSlot - card_name=Coin, mana=0


Player (0) - health: 3, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
4: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
4: SpellCardSlot - card_name=Coin, mana=0


Player (0) - health: 3, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
4: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

ERROR: already used the hero power
------------------------------
1 turn
------------------------------
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
4: SpellCardSlot - card_name=Coin, mana=0
5: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)


Player (0) - health: 3, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
4: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

Opponent (1) - health: 3, armour: 0, mana: 98 / 100
Weapon: None
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
4: SpellCardSlot - card_name=Coin, mana=0
5: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
6: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)


Player (0) - health: 3, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
4: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

Opponent (1) - health: 3, armour: 0, mana: 98 / 100
Weapon: None
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
4: SpellCardSlot - card_name=Coin, mana=0
5: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
6: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)


Player (0) - health: 3, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
4: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

ERROR: already used the hero power
Opponent (1) - health: 3, armour: 0, mana: 98 / 100
Weapon: None
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
4: SpellCardSlot - card_name=Coin, mana=0
5: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
6: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)


Player (0) - health: 3, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
4: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

Game Over: Player 0 wins'''

snapshots['TestBasicsOfWarrior::test_card_playing 1'] = '''0 goes first
------------------------------
0 turn
------------------------------
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
4: SpellCardSlot - card_name=Coin, mana=0


Player (0) - health: 5, armour: 0, mana: 100 / 100
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
4: SpellCardSlot - card_name=Coin, mana=0


Player (0) - health: 5, armour: 2, mana: 98 / 100
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
4: SpellCardSlot - card_name=Coin, mana=0


Player (0) - health: 5, armour: 2, mana: 98 / 100
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

ERROR: already used the hero power
------------------------------
1 turn
------------------------------
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
4: SpellCardSlot - card_name=Coin, mana=0
5: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)


Player (0) - health: 5, armour: 2, mana: 98 / 100
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

Opponent (1) - health: 5, armour: 2, mana: 98 / 100
Weapon: None
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
4: SpellCardSlot - card_name=Coin, mana=0
5: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)


Player (0) - health: 5, armour: 2, mana: 98 / 100
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

Opponent (1) - health: 5, armour: 2, mana: 98 / 100
Weapon: None
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
4: SpellCardSlot - card_name=Coin, mana=0
5: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)


Player (0) - health: 5, armour: 2, mana: 98 / 100
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

ERROR: already used the hero power
Opponent (1) - health: 5, armour: 2, mana: 98 / 100
Weapon: None
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
4: SpellCardSlot - card_name=Coin, mana=0
5: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)


Player (0) - health: 5, armour: 2, mana: 98 / 100
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

Game Over: Player 0 wins'''

snapshots['TestBasicsOfWisp::test_card_attacking 1'] = '''0 goes first
------------------------------
0 turn
------------------------------
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
4: SpellCardSlot - card_name=Coin, mana=0


Player (0) - health: 5, armour: 0, mana: 100 / 100
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

0 plays Wisp
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
4: SpellCardSlot - card_name=Coin, mana=0

\t0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

Player (0) - health: 5, armour: 0, mana: 100 / 100
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

0 plays Wisp
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
4: SpellCardSlot - card_name=Coin, mana=0

\t0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
\t1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

Player (0) - health: 5, armour: 0, mana: 100 / 100
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

------------------------------
1 turn
------------------------------
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
4: SpellCardSlot - card_name=Coin, mana=0
5: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

\t0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
\t1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

Player (0) - health: 5, armour: 0, mana: 100 / 100
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

1 plays Wisp
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: SpellCardSlot - card_name=Coin, mana=0
4: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

\t0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
\t0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
\t1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

Player (0) - health: 5, armour: 0, mana: 100 / 100
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

1 plays Wisp
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

\t0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
\t1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
\t0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
\t1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

Player (0) - health: 5, armour: 0, mana: 100 / 100
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

------------------------------
0 turn
------------------------------
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

\t0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
\t1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
\t0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
\t1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

Player (0) - health: 5, armour: 0, mana: 100 / 100
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1) attacks MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=0) died
MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=0) died
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

\t0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
\t0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

Player (0) - health: 5, armour: 0, mana: 100 / 100
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

0 plays Wisp
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

\t0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
\t0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
\t1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

Player (0) - health: 5, armour: 0, mana: 100 / 100
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

0 plays Wisp
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

\t0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
\t0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
\t1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
\t2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

Player (0) - health: 5, armour: 0, mana: 100 / 100
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

------------------------------
1 turn
------------------------------
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
4: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

\t0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
\t0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
\t1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
\t2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

Player (0) - health: 5, armour: 0, mana: 100 / 100
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1) attacks MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=0) died
MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=0) died
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
4: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

\t0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
\t1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

Player (0) - health: 5, armour: 0, mana: 100 / 100
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

1 plays Wisp
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: SpellCardSlot - card_name=Coin, mana=0
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

\t0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
\t0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
\t1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

Player (0) - health: 5, armour: 0, mana: 100 / 100
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

1 plays Wisp
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: SpellCardSlot - card_name=Coin, mana=0
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

\t0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
\t1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
\t0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
\t1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

Player (0) - health: 5, armour: 0, mana: 100 / 100
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: SpellCardSlot - card_name=Coin, mana=0
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

\t0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
\t1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
\t0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
\t1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

Player (0) - health: 5, armour: 0, mana: 100 / 100
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

Game Over: Player 0 wins'''

snapshots['TestBasicsOfWisp::test_card_playing 1'] = '''0 goes first
------------------------------
0 turn
------------------------------
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
4: SpellCardSlot - card_name=Coin, mana=0


Player (0) - health: 5, armour: 0, mana: 100 / 100
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

0 plays Wisp
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
4: SpellCardSlot - card_name=Coin, mana=0

\t0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

Player (0) - health: 5, armour: 0, mana: 100 / 100
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

0 plays Wisp
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
4: SpellCardSlot - card_name=Coin, mana=0

\t0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
\t1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

Player (0) - health: 5, armour: 0, mana: 100 / 100
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

------------------------------
1 turn
------------------------------
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
4: SpellCardSlot - card_name=Coin, mana=0
5: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

\t0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
\t1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

Player (0) - health: 5, armour: 0, mana: 100 / 100
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

1 plays Wisp
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
3: SpellCardSlot - card_name=Coin, mana=0
4: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

\t0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
\t0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
\t1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

Player (0) - health: 5, armour: 0, mana: 100 / 100
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

1 plays Wisp
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

\t0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
\t1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
\t0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
\t1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

Player (0) - health: 5, armour: 0, mana: 100 / 100
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

\t0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
\t1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
\t0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
\t1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

Player (0) - health: 5, armour: 0, mana: 100 / 100
0: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)
1: MinionCardSlot - card_name=Wisp, mana=0, attack=1, health=1)

Game Over: Player 0 wins'''

snapshots['TestBasicsOfWorgenInfiltrator::test_card_attacking 1'] = '''0 goes first
------------------------------
0 turn
------------------------------
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)
1: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)
2: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)
3: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)
4: SpellCardSlot - card_name=Coin, mana=0


Player (0) - health: 5, armour: 0, mana: 100 / 100
0: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)
1: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)
2: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)
3: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)

0 plays Worgen Infiltrator
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)
1: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)
2: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)
3: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)
4: SpellCardSlot - card_name=Coin, mana=0

\t0: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)

Player (0) - health: 5, armour: 0, mana: 99 / 100
0: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)
1: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)
2: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)

0 plays Worgen Infiltrator
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)
1: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)
2: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)
3: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)
4: SpellCardSlot - card_name=Coin, mana=0

\t0: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)
\t1: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)
1: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)

------------------------------
1 turn
------------------------------
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)
1: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)
2: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)
3: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)
4: SpellCardSlot - card_name=Coin, mana=0
5: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)

\t0: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)
\t1: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)
1: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)

1 plays Worgen Infiltrator
Opponent (1) - health: 5, armour: 0, mana: 99 / 100
Weapon: None
0: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)
1: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)
2: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)
3: SpellCardSlot - card_name=Coin, mana=0
4: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)

\t0: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)
\t0: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)
\t1: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)
1: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)

1 plays Worgen Infiltrator
Opponent (1) - health: 5, armour: 0, mana: 98 / 100
Weapon: None
0: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)
1: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)

\t0: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)
\t1: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)
\t0: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)
\t1: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)
1: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)

------------------------------
0 turn
------------------------------
Opponent (1) - health: 5, armour: 0, mana: 98 / 100
Weapon: None
0: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)
1: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)

\t0: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)
\t1: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)
\t0: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)
\t1: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)

Player (0) - health: 5, armour: 0, mana: 100 / 100
0: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)
1: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)
2: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)

ERROR: defender cannot be attacked (stealth)
0 plays Worgen Infiltrator
Opponent (1) - health: 5, armour: 0, mana: 98 / 100
Weapon: None
0: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)
1: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)

\t0: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)
\t1: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)
\t0: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)
\t1: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)
\t2: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)

Player (0) - health: 5, armour: 0, mana: 99 / 100
0: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)
1: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)

0 plays Worgen Infiltrator
Opponent (1) - health: 5, armour: 0, mana: 98 / 100
Weapon: None
0: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)
1: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)

\t0: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)
\t1: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)
\t0: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)
\t1: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)
\t2: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)
\t3: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)

------------------------------
1 turn
------------------------------
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)
1: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)
4: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)

\t0: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)
\t1: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)
\t0: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)
\t1: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)
\t2: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)
\t3: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)

ERROR: defender cannot be attacked (stealth)
1 plays Worgen Infiltrator
Opponent (1) - health: 5, armour: 0, mana: 99 / 100
Weapon: None
0: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)
1: SpellCardSlot - card_name=Coin, mana=0
2: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)
3: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)

\t0: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)
\t1: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)
\t2: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)
\t0: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)
\t1: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)
\t2: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)
\t3: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)

1 plays Worgen Infiltrator
Opponent (1) - health: 5, armour: 0, mana: 98 / 100
Weapon: None
0: SpellCardSlot - card_name=Coin, mana=0
1: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)
2: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)

\t0: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)
\t1: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)
\t2: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)
\t3: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)
\t0: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)
\t1: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)
\t2: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)
\t3: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)

Opponent (1) - health: 5, armour: 0, mana: 98 / 100
Weapon: None
0: SpellCardSlot - card_name=Coin, mana=0
1: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)
2: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)

\t0: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)
\t1: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)
\t2: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)
\t3: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)
\t0: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)
\t1: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)
\t2: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)
\t3: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)

Game Over: Player 0 wins'''

snapshots['TestBasicsOfWorgenInfiltrator::test_card_playing 1'] = '''0 goes first
------------------------------
0 turn
------------------------------
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)
1: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)
2: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)
3: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)
4: SpellCardSlot - card_name=Coin, mana=0


Player (0) - health: 5, armour: 0, mana: 100 / 100
0: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)
1: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)
2: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)
3: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)

0 plays Worgen Infiltrator
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)
1: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)
2: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)
3: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)
4: SpellCardSlot - card_name=Coin, mana=0

\t0: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)

Player (0) - health: 5, armour: 0, mana: 99 / 100
0: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)
1: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)
2: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)

0 plays Worgen Infiltrator
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)
1: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)
2: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)
3: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)
4: SpellCardSlot - card_name=Coin, mana=0

\t0: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)
\t1: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)
1: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)

------------------------------
1 turn
------------------------------
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)
1: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)
2: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)
3: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)
4: SpellCardSlot - card_name=Coin, mana=0
5: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)

\t0: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)
\t1: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)
1: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)

1 plays Worgen Infiltrator
Opponent (1) - health: 5, armour: 0, mana: 99 / 100
Weapon: None
0: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)
1: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)
2: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)
3: SpellCardSlot - card_name=Coin, mana=0
4: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)

\t0: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)
\t0: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)
\t1: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)
1: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)

1 plays Worgen Infiltrator
Opponent (1) - health: 5, armour: 0, mana: 98 / 100
Weapon: None
0: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)
1: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)

\t0: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)
\t1: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)
\t0: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)
\t1: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)
1: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)

Opponent (1) - health: 5, armour: 0, mana: 98 / 100
Weapon: None
0: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)
1: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)

\t0: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)
\t1: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)
\t0: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)
\t1: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)
1: MinionCardSlot - card_name=Worgen Infiltrator, mana=1, attack=2, health=1)

Game Over: Player 0 wins'''

snapshots['TestBasicsOfYoungDragonhawk::test_card_attacking 1'] = '''0 goes first
------------------------------
0 turn
------------------------------
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)
2: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)
3: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)
4: SpellCardSlot - card_name=Coin, mana=0


Player (0) - health: 5, armour: 0, mana: 100 / 100
0: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)
2: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)
3: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)

0 plays Young Dragonhawk
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)
2: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)
3: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)
4: SpellCardSlot - card_name=Coin, mana=0

\t0: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)

Player (0) - health: 5, armour: 0, mana: 99 / 100
0: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)
2: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)

0 plays Young Dragonhawk
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)
2: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)
3: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)
4: SpellCardSlot - card_name=Coin, mana=0

\t0: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)
\t1: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)

------------------------------
1 turn
------------------------------
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)
2: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)
3: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)
4: SpellCardSlot - card_name=Coin, mana=0
5: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)

\t0: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)
\t1: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)

1 plays Young Dragonhawk
Opponent (1) - health: 5, armour: 0, mana: 99 / 100
Weapon: None
0: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)
2: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)
3: SpellCardSlot - card_name=Coin, mana=0
4: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)

\t0: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)
\t0: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)
\t1: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)

1 plays Young Dragonhawk
Opponent (1) - health: 5, armour: 0, mana: 98 / 100
Weapon: None
0: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)

\t0: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)
\t1: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)
\t0: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)
\t1: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)

------------------------------
0 turn
------------------------------
Opponent (1) - health: 5, armour: 0, mana: 98 / 100
Weapon: None
0: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)

\t0: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)
\t1: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)
\t0: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)
\t1: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)

Player (0) - health: 5, armour: 0, mana: 100 / 100
0: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)
2: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)

MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1) attacks MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)
MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=0) died
MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=0) died
Opponent (1) - health: 5, armour: 0, mana: 98 / 100
Weapon: None
0: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)

\t0: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)
\t0: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)

Player (0) - health: 5, armour: 0, mana: 100 / 100
0: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)
2: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)

0 plays Young Dragonhawk
Opponent (1) - health: 5, armour: 0, mana: 98 / 100
Weapon: None
0: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)

\t0: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)
\t0: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)
\t1: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)

Player (0) - health: 5, armour: 0, mana: 99 / 100
0: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)

0 plays Young Dragonhawk
Opponent (1) - health: 5, armour: 0, mana: 98 / 100
Weapon: None
0: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)

\t0: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)
\t0: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)
\t1: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)
\t2: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)

------------------------------
1 turn
------------------------------
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)
4: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)

\t0: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)
\t0: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)
\t1: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)
\t2: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)

MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1) attacks MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)
MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=0) died
MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=0) died
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)
4: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)

\t0: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)
\t1: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)

1 plays Young Dragonhawk
Opponent (1) - health: 5, armour: 0, mana: 99 / 100
Weapon: None
0: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)
1: SpellCardSlot - card_name=Coin, mana=0
2: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)
3: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)

\t0: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)
\t0: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)
\t1: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)

1 plays Young Dragonhawk
Opponent (1) - health: 5, armour: 0, mana: 98 / 100
Weapon: None
0: SpellCardSlot - card_name=Coin, mana=0
1: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)
2: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)

\t0: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)
\t1: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)
\t0: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)
\t1: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)

Opponent (1) - health: 5, armour: 0, mana: 98 / 100
Weapon: None
0: SpellCardSlot - card_name=Coin, mana=0
1: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)
2: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)

\t0: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)
\t1: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)
\t0: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)
\t1: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)

Game Over: Player 0 wins'''

snapshots['TestBasicsOfYoungDragonhawk::test_card_playing 1'] = '''0 goes first
------------------------------
0 turn
------------------------------
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)
2: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)
3: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)
4: SpellCardSlot - card_name=Coin, mana=0


Player (0) - health: 5, armour: 0, mana: 100 / 100
0: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)
2: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)
3: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)

0 plays Young Dragonhawk
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)
2: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)
3: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)
4: SpellCardSlot - card_name=Coin, mana=0

\t0: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)

Player (0) - health: 5, armour: 0, mana: 99 / 100
0: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)
2: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)

0 plays Young Dragonhawk
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)
2: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)
3: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)
4: SpellCardSlot - card_name=Coin, mana=0

\t0: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)
\t1: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)

------------------------------
1 turn
------------------------------
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)
2: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)
3: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)
4: SpellCardSlot - card_name=Coin, mana=0
5: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)

\t0: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)
\t1: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)

1 plays Young Dragonhawk
Opponent (1) - health: 5, armour: 0, mana: 99 / 100
Weapon: None
0: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)
2: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)
3: SpellCardSlot - card_name=Coin, mana=0
4: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)

\t0: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)
\t0: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)
\t1: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)

1 plays Young Dragonhawk
Opponent (1) - health: 5, armour: 0, mana: 98 / 100
Weapon: None
0: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)

\t0: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)
\t1: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)
\t0: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)
\t1: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)

Opponent (1) - health: 5, armour: 0, mana: 98 / 100
Weapon: None
0: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)

\t0: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)
\t1: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)
\t0: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)
\t1: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)

Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)
1: MinionCardSlot - card_name=Young Dragonhawk, mana=1, attack=1, health=1)

Game Over: Player 0 wins'''

snapshots['TestBasicsOfYouthfulBrewmaster::test_card_attacking 1'] = '''0 goes first
------------------------------
0 turn
------------------------------
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
1: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
2: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
3: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
4: SpellCardSlot - card_name=Coin, mana=0


Player (0) - health: 5, armour: 0, mana: 100 / 100
0: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
1: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
2: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
3: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)

0 plays Youthful Brewmaster
MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2) returned to 0 hand
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
1: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
2: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
3: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
4: SpellCardSlot - card_name=Coin, mana=0


Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
1: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
2: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
3: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)

Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
1: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
2: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
3: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
4: SpellCardSlot - card_name=Coin, mana=0


Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
1: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
2: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
3: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)

0 plays Youthful Brewmaster
MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2) returned to 0 hand
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
1: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
2: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
3: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
4: SpellCardSlot - card_name=Coin, mana=0


Player (0) - health: 5, armour: 0, mana: 96 / 100
0: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
1: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
2: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
3: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)

Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
1: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
2: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
3: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
4: SpellCardSlot - card_name=Coin, mana=0


Player (0) - health: 5, armour: 0, mana: 96 / 100
0: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
1: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
2: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
3: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)

------------------------------
1 turn
------------------------------
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
1: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
2: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
3: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
4: SpellCardSlot - card_name=Coin, mana=0
5: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)


Player (0) - health: 5, armour: 0, mana: 96 / 100
0: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
1: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
2: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
3: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)

1 plays Youthful Brewmaster
MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2) returned to 1 hand
Opponent (1) - health: 5, armour: 0, mana: 98 / 100
Weapon: None
0: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
1: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
2: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
3: SpellCardSlot - card_name=Coin, mana=0
4: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
5: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)


Player (0) - health: 5, armour: 0, mana: 96 / 100
0: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
1: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
2: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
3: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)

Opponent (1) - health: 5, armour: 0, mana: 98 / 100
Weapon: None
0: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
1: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
2: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
3: SpellCardSlot - card_name=Coin, mana=0
4: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
5: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)


Player (0) - health: 5, armour: 0, mana: 96 / 100
0: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
1: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
2: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
3: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)

1 plays Youthful Brewmaster
MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2) returned to 1 hand
Opponent (1) - health: 5, armour: 0, mana: 96 / 100
Weapon: None
0: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
1: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
4: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
5: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)


Player (0) - health: 5, armour: 0, mana: 96 / 100
0: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
1: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
2: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
3: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)

Opponent (1) - health: 5, armour: 0, mana: 96 / 100
Weapon: None
0: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
1: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
4: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
5: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)


Player (0) - health: 5, armour: 0, mana: 96 / 100
0: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
1: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
2: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
3: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)

------------------------------
0 turn
------------------------------
Opponent (1) - health: 5, armour: 0, mana: 96 / 100
Weapon: None
0: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
1: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
4: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
5: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)


Player (0) - health: 5, armour: 0, mana: 100 / 100
0: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
1: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
2: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
3: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
4: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)

ERROR: attacker outside range
0 plays Youthful Brewmaster
MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2) returned to 0 hand
Opponent (1) - health: 5, armour: 0, mana: 96 / 100
Weapon: None
0: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
1: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
4: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
5: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)


Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
1: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
2: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
3: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
4: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)

Opponent (1) - health: 5, armour: 0, mana: 96 / 100
Weapon: None
0: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
1: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
4: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
5: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)


Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
1: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
2: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
3: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
4: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)

0 plays Youthful Brewmaster
MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2) returned to 0 hand
Opponent (1) - health: 5, armour: 0, mana: 96 / 100
Weapon: None
0: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
1: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
4: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
5: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)


Player (0) - health: 5, armour: 0, mana: 96 / 100
0: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
1: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
2: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
3: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
4: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)

Opponent (1) - health: 5, armour: 0, mana: 96 / 100
Weapon: None
0: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
1: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
4: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
5: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)


Player (0) - health: 5, armour: 0, mana: 96 / 100
0: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
1: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
2: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
3: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
4: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)

------------------------------
1 turn
------------------------------
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
1: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
4: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
5: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
6: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)


Player (0) - health: 5, armour: 0, mana: 96 / 100
0: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
1: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
2: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
3: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
4: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)

ERROR: attacker outside range
1 plays Youthful Brewmaster
MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2) returned to 1 hand
Opponent (1) - health: 5, armour: 0, mana: 98 / 100
Weapon: None
0: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
1: SpellCardSlot - card_name=Coin, mana=0
2: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
3: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
4: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
5: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
6: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)


Player (0) - health: 5, armour: 0, mana: 96 / 100
0: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
1: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
2: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
3: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
4: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)

Opponent (1) - health: 5, armour: 0, mana: 98 / 100
Weapon: None
0: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
1: SpellCardSlot - card_name=Coin, mana=0
2: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
3: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
4: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
5: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
6: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)


Player (0) - health: 5, armour: 0, mana: 96 / 100
0: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
1: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
2: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
3: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
4: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)

1 plays Youthful Brewmaster
MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2) returned to 1 hand
Opponent (1) - health: 5, armour: 0, mana: 96 / 100
Weapon: None
0: SpellCardSlot - card_name=Coin, mana=0
1: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
2: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
3: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
4: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
5: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
6: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)


Player (0) - health: 5, armour: 0, mana: 96 / 100
0: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
1: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
2: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
3: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
4: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)

Opponent (1) - health: 5, armour: 0, mana: 96 / 100
Weapon: None
0: SpellCardSlot - card_name=Coin, mana=0
1: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
2: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
3: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
4: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
5: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
6: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)


Player (0) - health: 5, armour: 0, mana: 96 / 100
0: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
1: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
2: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
3: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
4: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)

Opponent (1) - health: 5, armour: 0, mana: 96 / 100
Weapon: None
0: SpellCardSlot - card_name=Coin, mana=0
1: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
2: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
3: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
4: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
5: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
6: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)


Player (0) - health: 5, armour: 0, mana: 96 / 100
0: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
1: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
2: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
3: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
4: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)

Game Over: Player 0 wins'''

snapshots['TestBasicsOfYouthfulBrewmaster::test_card_playing 1'] = '''0 goes first
------------------------------
0 turn
------------------------------
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
1: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
2: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
3: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
4: SpellCardSlot - card_name=Coin, mana=0


Player (0) - health: 5, armour: 0, mana: 100 / 100
0: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
1: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
2: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
3: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)

0 plays Youthful Brewmaster
MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2) returned to 0 hand
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
1: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
2: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
3: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
4: SpellCardSlot - card_name=Coin, mana=0


Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
1: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
2: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
3: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)

Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
1: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
2: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
3: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
4: SpellCardSlot - card_name=Coin, mana=0


Player (0) - health: 5, armour: 0, mana: 98 / 100
0: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
1: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
2: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
3: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)

0 plays Youthful Brewmaster
MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2) returned to 0 hand
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
1: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
2: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
3: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
4: SpellCardSlot - card_name=Coin, mana=0


Player (0) - health: 5, armour: 0, mana: 96 / 100
0: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
1: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
2: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
3: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)

Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
1: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
2: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
3: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
4: SpellCardSlot - card_name=Coin, mana=0


Player (0) - health: 5, armour: 0, mana: 96 / 100
0: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
1: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
2: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
3: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)

------------------------------
1 turn
------------------------------
Opponent (1) - health: 5, armour: 0, mana: 100 / 100
Weapon: None
0: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
1: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
2: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
3: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
4: SpellCardSlot - card_name=Coin, mana=0
5: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)


Player (0) - health: 5, armour: 0, mana: 96 / 100
0: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
1: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
2: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
3: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)

1 plays Youthful Brewmaster
MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2) returned to 1 hand
Opponent (1) - health: 5, armour: 0, mana: 98 / 100
Weapon: None
0: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
1: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
2: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
3: SpellCardSlot - card_name=Coin, mana=0
4: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
5: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)


Player (0) - health: 5, armour: 0, mana: 96 / 100
0: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
1: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
2: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
3: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)

Opponent (1) - health: 5, armour: 0, mana: 98 / 100
Weapon: None
0: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
1: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
2: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
3: SpellCardSlot - card_name=Coin, mana=0
4: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
5: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)


Player (0) - health: 5, armour: 0, mana: 96 / 100
0: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
1: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
2: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
3: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)

1 plays Youthful Brewmaster
MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2) returned to 1 hand
Opponent (1) - health: 5, armour: 0, mana: 96 / 100
Weapon: None
0: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
1: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
4: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
5: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)


Player (0) - health: 5, armour: 0, mana: 96 / 100
0: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
1: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
2: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
3: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)

Opponent (1) - health: 5, armour: 0, mana: 96 / 100
Weapon: None
0: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
1: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
4: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
5: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)


Player (0) - health: 5, armour: 0, mana: 96 / 100
0: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
1: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
2: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
3: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)

Opponent (1) - health: 5, armour: 0, mana: 96 / 100
Weapon: None
0: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
1: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
2: SpellCardSlot - card_name=Coin, mana=0
3: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
4: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
5: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)


Player (0) - health: 5, armour: 0, mana: 96 / 100
0: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
1: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
2: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)
3: MinionCardSlot - card_name=Youthful Brewmaster, mana=2, attack=3, health=2)

Game Over: Player 0 wins'''