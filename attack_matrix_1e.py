#!/usr/bin/python3

# Calculate to-hit numbers across characters

class Matrix:
	# Source: AD&D 1e Dungeon Masters Guide p. 74
	CLERIC = 0
	DRUID = 0
	MONK = 0
	FIGHTER = 1
	PALADIN = 1
	RANGER = 1
	MAGE = 2
	ILLUSIONIST = 2
	THIEF = 3
	ASSASSIN = 3
	MONSTER = 4
	ZERO = 5

class Level:
	# Monster-only columns:
	UP_TO_ONE_MINUS_ONE = -3
	ONE_MINUS_ONE = -2
	ONE = -1
	ONE_PLUS = 1
	# etc.

class Armor:
	# Source: AD&D 1e Dungeon Masters Guide p. 73
	PLATE_SHIELD = 2
	SPLINT_SHIELD = 3
	BANDED_SHIELD = 3
	PLATE = 3
	CHAIN_SHIELD = 4
	SPLINT = 4
	BANDED = 4
	SCALE_SHIELD = 5
	CHAIN = 5
	STUDDED_SHIELD = 6
	RING_SHIELD = 6
	SCALE = 6
	LEATHER_SHIELD = 7
	PADDED_SHIELD = 7
	STUDDED = 7
	LEATHER = 8
	PADDED = 8
	SHIELD = 9
	NONE = 10
	NOF_ACS = 11

class Weapon:
	# Source: AD&D 1e Players Handbook p. 38
	# Melee
	AXE_BATTLE = 0
	AXE_HAND = 1
	BARDICHE = 2
	BEC_DE_CORBIN = 3
	BILL_GUISARME = 4
	BO_STICK = 5
	CLUB = 6
	DAGGER = 7
	FAUCHARD = 8
	FAUCHARD_FORK = 9
	FIST = 10
	FLAIL_FOOTMANS = 11
	FLAIL_HORSEMANS = 12
	FORK_MILITARY = 13
	GLAIVE = 14
	GLAIVE_GUISARME = 15
	GUISARME = 16
	GUISARME_VOULGE = 17
	HALBERD = 18
	HAMMER_LUCERN= 19
	HAMMER = 20
	JO_STICK = 21
	LANCE_HEAVY = 22
	LANCE_LIGHT = 23
	LANCE_MEDIUM = 24
	MACE_FOOTMANS = 25
	MACE_HORSEMANS = 26
	MORNING_STAR = 27
	PARTISAN = 28
	PICK_MILITARY_FOOTMANS = 29
	PICK_MILITARY_HORSEMANS = 30
	PIKE = 31
	RANSEUR = 32
	SCIMITAR = 33
	SPEAR = 34
	SPETUM = 35
	STAFF_QUARTER = 36
	SWORD_BASTARD_TWOHANDED = 37
	SWORD_BROAD = 38
	SWORD_LONG = 39
	SWORD_BASTARD_ONEHANDED = SWORD_LONG
	SWORD_SHORT = 40
	SWORD_TWOHANDED = 41
	TRIDENT = 42
	VOULGE = 43
	# Ranged
	AXE_THROWN = 44
	BOW_COMPOSITE_LONG = 45
	BOW_COMPOSITE_SHORT = 46
	BOW_LONG = 47
	BOW_SHORT = 48
	CLUB_THROWN = 49
	CROSSBOW_HEAVY = 50
	CROSSBOW_LIGHT = 51
	DAGGER_THROWN = 52
	DART = 53
	HAMMER_THROWN = 54
	JAVELIN = 55
	SLING_BULLET = 56
	SLING_STONE = 57
	SPEAR_THROWN = 58
	NONE = 59
	NOF_WEAPONS = 60

def weapon_adjustment(armor, weapon):
	lut = {
		# Source: AD&D 1e Players Handbook p. 38
		# TODO: extend when needed
		# Melee
		Weapon.AXE_BATTLE:
			{2:-3, 3:-2, 4:-1, 5:-1, 6:+0, 7:+0, 8:+1, 9:+1, 10:+1},
		Weapon.DAGGER:
			{2:-3, 3:-3, 4:-2, 5:-2, 6:+0, 7:+0, 8:+1, 9:+1, 10:+3},
		Weapon.FIST:
			{2:-7, 3:-5, 4:-3, 5:-1, 6:0, 7:0, 8:2, 9:0, 10:4},
		Weapon.SWORD_BASTARD_TWOHANDED:
			{2:+0, 3:+0, 4:+1, 5:+1, 6:+1, 7:+1, 8:+1, 9:+1, 10:+0},
		Weapon.SWORD_LONG:
			{2:-2, 3:-1, 4:+0, 5:+0, 6:+0, 7:+0, 8:+0, 9:+1, 10:+2},
		Weapon.SWORD_SHORT:
			{2:-3, 3:-2, 4:-1, 5:+0, 6:+0, 7:+0, 8:+1, 9:+0, 10:+2},
		Weapon.SWORD_TWOHANDED:
			{2:+2, 3:+2, 4:+2, 5:+2, 6:+3, 7:+3, 8:+3, 9:+1, 10:+0},
#		Weapon.:
#			{2:, 3:, 4:, 5:, 6:, 7:, 8:, 9:, 10:},
		# Ranged
		Weapon.BOW_LONG:
			{2:-1, 3:+0, 4:+0, 5:+1, 6:+2, 7:+3, 8:+3, 9:+3, 10:+3},
		Weapon.SLING_BULLET:
			{2:-2, 3:-2, 4:-1, 5:+0, 6:+0, 7:+0, 8:+2, 9:+1, 10:+3},
		Weapon.NONE:
			{2:+0, 3:+0, 4:+0, 5:+0, 6:+0, 7:+0, 8:+0, 9:+0, 10:+0}}
	if armor < 2 or armor > 10:
		print("Incorrect input. Please enter valid armor type (rated 2-10) without modified armor class.")
		exit()
	return lut[weapon][armor]

def magic_sequence(thac10, ac):
	# The non-linear sequence within each column of an attack matrix is
	# identical with a certain offset. It increments proportionally with
	# target armor class, except that 20 repeats six times.
	# Source: AD&D 1e Dungeon Masters Guide p. 73
	offset = 10 - ac
	if thac10 + offset < 20:
		return thac10 + offset
	elif thac10 + offset < 26:
		return 20
	else:
		return thac10 + offset - 6

def matrix_target(attacker, defender):
	# THAC10 is used here because no target of 20+ shows up in any table
	# for armor class 10, so they can be most easily looked up.
	lut = {
		# Source: AD&D 1e Dungeon Masters Guide p. 74-75
					# Level		# THAC10
		Matrix.CLERIC: { # or Druid, Monk
					range(1,4):	10,
					range(4,7):	8,
					range(7,10):	6,
					range(10,13):	4,
					range(13,16):	2,
					range(16,19):	0,
					range(19,100):	-1},
		Matrix.FIGHTER: { # or Paladin, Ranger
					range(1,3):	10,
					range(3,5):	8,
					range(5,7):	6,
					range(7,9):	4,
					range(9,11):	2,
					range(11,13):	0,
					range(13,15):	-2,
					range(15,17):	-4,
					range(17,100):	-6},
		Matrix.MAGE: { # or Illusionist
					range(1,6):	11,
					range(6,10):	9,
					range(11,16):	6,
					range(16,21):	3,
					range(21,100):	1},
		Matrix.THIEF: { # or Assassin
					range(1,5):	11,
					range(5,9):	9,
					range(9,13):	6,
					range(13,17):	4,
					range(17,21):	2,
					range(21,100):	0},
		Matrix.MONSTER: {	range(Level.UP_TO_ONE_MINUS_ONE,
					Level.ONE_MINUS_ONE):
							11,
					range(Level.ONE_MINUS_ONE, Level.ONE):
							10,
					range(Level.ONE, 0):
							9,
					range(Level.ONE_PLUS,2):
							8,
					range(2,4):	6,
					range(4,6):	5,
					range(6,8):	3,
					range(8,10):	2,
					range(10,12):	0,
					range(12,14):	-1,
					range(14,16):	-2,
					range(16,100):	-3},
		Matrix.ZERO: {		range(0, 1):	8}}
	if attacker.level == 0:
		matrix = lut[Matrix.ZERO]
	else:
		matrix = lut[attacker.matrix]
	for column in matrix:
		if attacker.level in column:
			thac10 = matrix[column]
			break
	target = magic_sequence(thac10, defender.ac)
	if defender.matrix != Matrix.MONSTER:
		# Only traditional armor types are covered in the weapon
		# adjustment table (ranged 2-10) and modified armor class
		# should not be used.
		target -= weapon_adjustment(defender.armor, attacker.weapon)
	return target

class Character:
	def __init__(self, name, matrix, level, armor, ac, weapon):
		self.name = name
		self.matrix = matrix
		self.level = level
		self.armor = armor
		self.ac = ac
		self.weapon = weapon

characters = [
		# Example combatants, modify inline below:
		Character("Axeman",
			Matrix.FIGHTER,
			4,
			Armor.PLATE_SHIELD,
			Armor.PLATE_SHIELD - 0,
			Weapon.AXE_BATTLE),
		Character("Bowman",
			Matrix.FIGHTER,
			4,
			Armor.PLATE,
			Armor.PLATE - 0,
			Weapon.BOW_LONG),
		Character("Brownie",
			Matrix.MONSTER,
			Level.UP_TO_ONE_MINUS_ONE,
			Armor.NONE,
			3,
			Weapon.FIST),
		Character("Harpy",
			Matrix.MONSTER,
			3,
			Armor.NONE,
			7,
			Weapon.NONE)]

row = "->\t"
for defender in characters:
	row += defender.name[0:7] + "\t"
print(row)
for attacker in characters:
	row = attacker.name[0:7] + "\t"
	for defender in characters:
		if attacker == defender:
			row += "X\t"
		else:
			target = matrix_target(attacker, defender)
			row += str(target) + "\t"
	print(row)
