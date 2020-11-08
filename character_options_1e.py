#!/usr/bin/python

# Input ability scores and output race/class options

class Range:
	def __init__(self, minimum, maximum):
		self.minimum = minimum
		self.maximum = maximum

class Ability:
	STRENGTH = 0
	DEXTERITY = 1
	CONSTITUTION = 2
	INTELLIGENCE = 3
	WISDOM = 4
	CHARISMA = 5
	NOF_ABILITIES = 6

class Race:
	DWARF = 0
	ELF = 1
	GNOME = 2
	HALF_ELF = 3
	HALFLING = 4
	HALF_ORC = 5
	HUMAN = 6
	NOF_RACES = 7

def race_to_string(which):
	lut = [	"Dwarf",
		"Elf",
		"Gnome",
		"Half-Elf",
		"Halfling",
		"Half-Orc",
		"Human"]
	return lut[which]

def apply_race(abilties, race):
	# Source: AD&D 1e Players Handbook p. 14
	lut = {	Race.DWARF: [	0,  # STR
				0,  # DEX
				+1,  # CON
				0,  # INT
				0,  # WIS
				-1], # CHA
		Race.ELF: [	0,  # STR
				+1,  # DEX
				-1,  # CON
				0,  # INT
				0,  # WIS
				0], # CHA
		Race.GNOME: [	0,  # STR
				0,  # DEX
				0,  # CON
				0,  # INT
				0,  # WIS
				0], # CHA
		Race.HALF_ELF: [0,  # STR
				0,  # DEX
				0,  # CON
				0,  # INT
				0,  # WIS
				0], # CHA
		Race.HALFLING: [-1,  # STR
				+1,  # DEX
				0,  # CON
				0,  # INT
				0,  # WIS
				0], # CHA
		Race.HALF_ORC: [+1,  # STR
				0,  # DEX
				+1,  # CON
				0,  # INT
				0,  # WIS
				-2], # CHA
		Race.HUMAN: [	0,  # STR
				0,  # DEX
				0,  # CON
				0,  # INT
				0,  # WIS
				0]} # CHA
	return abilities + lut[race]

class Class:
	CLERIC = 0
	DRUID = 1
	FIGHTER = 2
	PALADIN = 3
	RANGER = 4
	MAGE = 5
	ILLUSIONIST = 6
	THIEF = 7
	ASSASSIN = 8
	MONK = 9
	NOF_CLASSES = 10

def class_to_string(which):
	lut = [	"Cleric",
		"Druid",
		"Fighter",
		"Paladin",
		"Ranger",
		"Mage",
		"Illusionist",
		"Thief",
		"Assassin",
		"Monk"]
	return lut[which]

class Multiclass:
	CLERIC_FIGHTER = 0
	CLERIC_FIGHTER_MAGE = 1
	CLERIC_RANGER = 2
	CLERIC_MAGE = 3
	CLERIC_THIEF = 4
	CLERIC_ASSASSIN = 5
	FIGHTER_MAGE = 6
	FIGHTER_ILLIUSIONIST = 7
	FIGHTER_THIEF = 8
	FIGHTER_ASSASSIN = 9
	FIGHTER_MAGE_THIEF = 10
	MAGE_THIEF = 11
	ILLUSIONIST_THIEF = 12
	NOF_MULTICLASSES = 13

def multiclass_to_classes(multiclass):
	lut = {	Multiclass.CLERIC_FIGHTER: [		1,  # CLERIC
							0,  # DRUID
							1,  # FIGHTER
							0,  # PALADIN
							0,  # RANGER
							0,  # MAGE
							0,  # ILLUSIONIST
							0,  # THIEF
							0,  # ASSASSIN
							0], # MONK
		Multiclass.CLERIC_FIGHTER_MAGE: [	1,  # CLERIC
							0,  # DRUID
							1,  # FIGHTER
							0,  # PALADIN
							0,  # RANGER
							1,  # MAGE
							0,  # ILLUSIONIST
							0,  # THIEF
							0,  # ASSASSIN
							0], # MONK
		Multiclass.CLERIC_RANGER: [		1,  # CLERIC
							0,  # DRUID
							0,  # FIGHTER
							0,  # PALADIN
							1,  # RANGER
							0,  # MAGE
							0,  # ILLUSIONIST
							0,  # THIEF
							0,  # ASSASSIN
							0], # MONK
		Multiclass.CLERIC_MAGE: [		1,  # CLERIC
							0,  # DRUID
							0,  # FIGHTER
							0,  # PALADIN
							0,  # RANGER
							1,  # MAGE
							0,  # ILLUSIONIST
							0,  # THIEF
							0,  # ASSASSIN
							0], # MONK
		Multiclass.CLERIC_THIEF: [		1,  # CLERIC
							0,  # DRUID
							0,  # FIGHTER
							0,  # PALADIN
							0,  # RANGER
							0,  # MAGE
							0,  # ILLUSIONIST
							1,  # THIEF
							0,  # ASSASSIN
							0], # MONK
		Multiclass.CLERIC_ASSASSIN: [		1,  # CLERIC
							0,  # DRUID
							0,  # FIGHTER
							0,  # PALADIN
							0,  # RANGER
							0,  # MAGE
							0,  # ILLUSIONIST
							0,  # THIEF
							1,  # ASSASSIN
							0], # MONK
		Multiclass.FIGHTER_MAGE: [		0,  # CLERIC
							0,  # DRUID
							1,  # FIGHTER
							0,  # PALADIN
							0,  # RANGER
							1,  # MAGE
							0,  # ILLUSIONIST
							0,  # THIEF
							0,  # ASSASSIN
							0], # MONK
		Multiclass.FIGHTER_ILLIUSIONIST: [	0,  # CLERIC
							0,  # DRUID
							1,  # FIGHTER
							0,  # PALADIN
							0,  # RANGER
							0,  # MAGE
							1,  # ILLUSIONIST
							0,  # THIEF
							0,  # ASSASSIN
							0], # MONK
		Multiclass.FIGHTER_THIEF: [		0,  # CLERIC
							0,  # DRUID
							1,  # FIGHTER
							0,  # PALADIN
							0,  # RANGER
							0,  # MAGE
							0,  # ILLUSIONIST
							1,  # THIEF
							0,  # ASSASSIN
							0], # MONK
		Multiclass.FIGHTER_ASSASSIN: [		0,  # CLERIC
							0,  # DRUID
							1,  # FIGHTER
							0,  # PALADIN
							0,  # RANGER
							0,  # MAGE
							0,  # ILLUSIONIST
							0,  # THIEF
							1,  # ASSASSIN
							0], # MONK
		Multiclass.FIGHTER_MAGE_THIEF: [	0,  # CLERIC
							0,  # DRUID
							1,  # FIGHTER
							0,  # PALADIN
							0,  # RANGER
							1,  # MAGE
							0,  # ILLUSIONIST
							1,  # THIEF
							0,  # ASSASSIN
							0], # MONK
		Multiclass.MAGE_THIEF: [		0,  # CLERIC
							0,  # DRUID
							0,  # FIGHTER
							0,  # PALADIN
							0,  # RANGER
							1,  # MAGE
							0,  # ILLUSIONIST
							1,  # THIEF
							0,  # ASSASSIN
							0], # MONK
		Multiclass.ILLUSIONIST_THIEF: [		0,  # CLERIC
							0,  # DRUID
							0,  # FIGHTER
							0,  # PALADIN
							0,  # RANGER
							0,  # MAGE
							1,  # ILLUSIONIST
							1,  # THIEF
							0,  # ASSASSIN
							0]} # MONK
	return lut[multiclass]

def multiclass_to_string(multiclass):
	string = ""
	classes = multiclass_to_classes(multiclass)
	for i in range(len(classes)):
		if classes[i] == 1:
			string += class_to_string(i) + "/"
	if len(string) > 1 and string[len(string) - 1] == '/':
		string = string[:-1]
	return string

def valid_class(classe, abilities):
	# Source: AD&D 1e Players Handbook p. 20-30, each class' description
	lut = {	Class.CLERIC: [		3,  # STR
					3,  # DEX
					3,  # CON
					3,  # INT
					9,  # WIS
					3], # CHA
		Class.DRUID: [		3,  # STR
					3,  # DEX
					3,  # CON
					3,  # INT
					12,  # WIS
					15], # CHA
		Class.FIGHTER: [	9,  # STR
					3,  # DEX
					7,  # CON
					3,  # INT
					3,  # WIS
					3], # CHA
		Class.PALADIN: [	12,  # STR
					3,  # DEX
					9,  # CON
					9,  # INT
					13,  # WIS
					17], # CHA
		Class.RANGER: [		13,  # STR
					3,  # DEX
					14,  # CON
					13,  # INT
					14,  # WIS
					3], # CHA
		Class.MAGE: [		3,  # STR
					3,  # DEX
					6,  # CON
					9,  # INT
					3,  # WIS
					3], # CHA
		Class.ILLUSIONIST: [	3,  # STR
					16,  # DEX
					3,  # CON
					15,  # INT
					3,  # WIS
					3], # CHA
		Class.THIEF: [		3,  # STR
					9,  # DEX
					3,  # CON
					3,  # INT
					3,  # WIS
					3], # CHA
		Class.ASSASSIN: [	12,  # STR
					12,  # DEX
					3,  # CON
					11,  # INT
					3,  # WIS
					3], # CHA
		Class.MONK: [		15,  # STR
					15,  # DEX
					11,  # CON
					3,  # INT
					15,  # WIS
					3]} # CHA
	valid = True
	for i in range(0, 6):
		if (abilities[i] < lut[classe][i]):
			valid = False
			break
	return valid

def valid_multiclass(multiclass, abilities):
	classes = multiclass_to_classes(multiclass)
	for i in range(len(classes)):
		if classes[i] == 1:
			if not valid_class(i, abilities):
				return False
	return True

def maximum_class_level(race, classe):
	# Source: AD&D 1e Players Handbook p. 14, Table II
	lut = {	Race.DWARF: [	8,  # CLERIC
				0,  # DRUID
				9,  # FIGHTER
				0,  # PALADIN
				0,  # RANGER
				0,  # MAGE
				0,  # ILLUSIONIST
				100,  # THIEF
				9,  # ASSASSIN
				0], # MONK
		Race.ELF: [	7,  # CLERIC
				0,  # DRUID
				7,  # FIGHTER
				0,  # PALADIN
				0,  # RANGER
				11,  # MAGE
				0,  # ILLUSIONIST
				100,  # THIEF
				10,  # ASSASSIN
				0], # MONK
		Race.GNOME: [	7,  # CLERIC
				0,  # DRUID
				6,  # FIGHTER
				0,  # PALADIN
				0,  # RANGER
				0,  # MAGE
				7,  # ILLUSIONIST
				100,  # THIEF
				8,  # ASSASSIN
				0], # MONK
		Race.HALF_ELF: [5,  # CLERIC
				100,  # DRUID
				8,  # FIGHTER
				0,  # PALADIN
				8,  # RANGER
				8,  # MAGE
				0,  # ILLUSIONIST
				100,  # THIEF
				11,  # ASSASSIN
				0], # MONK
		Race.HALFLING: [0,  # CLERIC
				6,  # DRUID
				6,  # FIGHTER
				0,  # PALADIN
				0,  # RANGER
				0,  # MAGE
				0,  # ILLUSIONIST
				100,  # THIEF
				0,  # ASSASSIN
				0], # MONK
		Race.HALF_ORC: [4,  # CLERIC
				0,  # DRUID
				10,  # FIGHTER
				0,  # PALADIN
				0,  # RANGER
				0,  # MAGE
				0,  # ILLUSIONIST
				8,  # THIEF
				100,  # ASSASSIN
				0], # MONK
		Race.HUMAN: [	100,  # CLERIC
				100,  # DRUID
				100,  # FIGHTER
				100,  # PALADIN
				100,  # RANGER
				100,  # MAGE
				100,  # ILLUSIONIST
				100,  # THIEF
				100,  # ASSASSIN
				100]} # MONK
	return lut[race][classe]

def maximum_multiclass_level(race, multiclass):
	string = ""
	classes = multiclass_to_classes(multiclass)
	for i in range(len(classes)):
		if classes[i] == 1:
			string += str(maximum_class_level(race, i)) + "/"
	if len(string) > 1 and string[len(string) - 1] == '/':
		string = string[:-1]
	return string

def valid_race_multiclass(race, multiclass, abilities):
	# Source: AD&D 1e Players Handbook p. 32-33
	lut = {	Race.DWARF: [	0,  # CLERIC_FIGHTER
				0,  # CLERIC_FIGHTER_MAGE
				0,  # CLERIC_RANGER
				0,  # CLERIC_MAGE
				0,  # CLERIC_THIEF
				0,  # CLERIC_ASSASSIN
				0,  # FIGHTER_MAGE
				0,  # FIGHTER_ILLIUSIONIST
				1,  # FIGHTER_THIEF
				0,  # FIGHTER_ASSASSIN
				0,  # FIGHTER_MAGE_THIEF
				0,  # MAGE_THIEF
				0], # ILLUSIONIST_THIEF
		Race.ELF: [	0,  # CLERIC_FIGHTER
				0,  # CLERIC_FIGHTER_MAGE
				0,  # CLERIC_RANGER
				0,  # CLERIC_MAGE
				0,  # CLERIC_THIEF
				0,  # CLERIC_ASSASSIN
				1,  # FIGHTER_MAGE
				0,  # FIGHTER_ILLIUSIONIST
				1,  # FIGHTER_THIEF
				0,  # FIGHTER_ASSASSIN
				1,  # FIGHTER_MAGE_THIEF
				1,  # MAGE_THIEF
				0], # ILLUSIONIST_THIEF
		Race.GNOME: [	0,  # CLERIC_FIGHTER
				0,  # CLERIC_FIGHTER_MAGE
				0,  # CLERIC_RANGER
				0,  # CLERIC_MAGE
				0,  # CLERIC_THIEF
				0,  # CLERIC_ASSASSIN
				0,  # FIGHTER_MAGE
				1,  # FIGHTER_ILLIUSIONIST
				1,  # FIGHTER_THIEF
				0,  # FIGHTER_ASSASSIN
				0,  # FIGHTER_MAGE_THIEF
				0,  # MAGE_THIEF
				1], # ILLUSIONIST_THIEF
		Race.HALF_ELF: [1,  # CLERIC_FIGHTER
				1,  # CLERIC_FIGHTER_MAGE
				1,  # CLERIC_RANGER
				1,  # CLERIC_MAGE
				0,  # CLERIC_THIEF
				0,  # CLERIC_ASSASSIN
				1,  # FIGHTER_MAGE
				0,  # FIGHTER_ILLIUSIONIST
				1,  # FIGHTER_THIEF
				0,  # FIGHTER_ASSASSIN
				1,  # FIGHTER_MAGE_THIEF
				1,  # MAGE_THIEF
				0], # ILLUSIONIST_THIEF
		Race.HALFLING: [0,  # CLERIC_FIGHTER
				0,  # CLERIC_FIGHTER_MAGE
				0,  # CLERIC_RANGER
				0,  # CLERIC_MAGE
				0,  # CLERIC_THIEF
				0,  # CLERIC_ASSASSIN
				0,  # FIGHTER_MAGE
				0,  # FIGHTER_ILLIUSIONIST
				1,  # FIGHTER_THIEF
				0,  # FIGHTER_ASSASSIN
				0,  # FIGHTER_MAGE_THIEF
				0,  # MAGE_THIEF
				0], # ILLUSIONIST_THIEF
		Race.HALF_ORC: [1,  # CLERIC_FIGHTER
				0,  # CLERIC_FIGHTER_MAGE
				0,  # CLERIC_RANGER
				0,  # CLERIC_MAGE
				1,  # CLERIC_THIEF
				1,  # CLERIC_ASSASSIN
				0,  # FIGHTER_MAGE
				0,  # FIGHTER_ILLIUSIONIST
				1,  # FIGHTER_THIEF
				1,  # FIGHTER_ASSASSIN
				0,  # FIGHTER_MAGE_THIEF
				0,  # MAGE_THIEF
				0], # ILLUSIONIST_THIEF
		Race.HUMAN: [	0,  # CLERIC_FIGHTER
				0,  # CLERIC_FIGHTER_MAGE
				0,  # CLERIC_RANGER
				0,  # CLERIC_MAGE
				0,  # CLERIC_THIEF
				0,  # CLERIC_ASSASSIN
				0,  # FIGHTER_MAGE
				0,  # FIGHTER_ILLIUSIONIST
				0,  # FIGHTER_THIEF
				0,  # FIGHTER_ASSASSIN
				0,  # FIGHTER_MAGE_THIEF
				0,  # MAGE_THIEF
				0]} # ILLUSIONIST_THIEF
	if lut[race][multiclass] == 1 and valid_multiclass(multiclass, abilities):
		# Exceptions listed in the text of class descriptions
		if race == Race.HALF_ELF and multiclass_to_classes(multiclass)[Class.CLERIC] == 1 and \
			not abilities[Ability.WISDOM] >= 13:
			return
		print("> " + race_to_string(race) + " " + \
			multiclass_to_string(multiclass) + " (maximum level " + \
			maximum_multiclass_level(race, multiclass) + ")")

def valid_race_class(race, classe, abilities):
	if maximum_class_level(race, classe) > 0 and valid_class(classe, abilities):
		print("> " + race_to_string(race) + " " + \
			class_to_string(classe) + " (maximum level " + \
			str(maximum_class_level(race, classe)) + ")")

def valid_race(race, abilities):
	# Source: AD&D 1e Players Handbook p. 15, Table III
	# Gender is ignored
	new_abilities = apply_race(abilities, race)
	lut = {	Race.DWARF: [	Range(8, 18),  # STR
				Range(3, 17),  # DEX
				Range(12, 19),  # CON
				Range(3, 18),  # INT
				Range(3, 18),  # WIS
				Range(3, 16)], # CHA
		Race.ELF: [	Range(3, 18),  # STR
				Range(7, 19),  # DEX
				Range(6, 18),  # CON
				Range(8, 18),  # INT
				Range(3, 18),  # WIS
				Range(8, 18)], # CHA
		Race.GNOME: [	Range(6, 18),  # STR
				Range(3, 18),  # DEX
				Range(8, 18),  # CON
				Range(7, 18),  # INT
				Range(3, 18),  # WIS
				Range(3, 18)], # CHA
		Race.HALF_ELF: [Range(3, 18),  # STR
				Range(6, 18),  # DEX
				Range(6, 18),  # CON
				Range(4, 18),  # INT
				Range(3, 18),  # WIS
				Range(3, 18)], # CHA
		Race.HALFLING: [Range(6, 17),  # STR
				Range(8, 18),  # DEX
				Range(10, 19),  # CON
				Range(6, 18),  # INT
				Range(3, 17),  # WIS
				Range(3, 18)], # CHA
		Race.HALF_ORC: [Range(6, 18),  # STR
				Range(3, 17),  # DEX
				Range(3, 14),  # CON
				Range(3, 17),  # INT
				Range(3, 14),  # WIS
				Range(3, 12)], # CHA
		Race.HUMAN: [	Range(3, 18),  # STR
				Range(3, 18),  # DEX
				Range(3, 18),  # CON
				Range(3, 18),  # INT
				Range(3, 18),  # WIS
				Range(3, 18)]} # CHA
	valid = True
	reduced = False
	for i in range(0, 6):
		if (new_abilities[i] < lut[race][i].minimum):
			valid = False
			break
		if (new_abilities[i] > lut[race][i].maximum):
			reduced = True
	if valid == True:
		for i in range(0, Class.NOF_CLASSES):
			valid_race_class(race, i, new_abilities)
		for i in range(0, Multiclass.NOF_MULTICLASSES):
			valid_race_multiclass(race, i, new_abilities)
	if reduced == True:
		print("(In order to be a " + race_to_string(race) + \
			" abilities scores would be lowered due to a maximum " +\
			"for that race.)")

print("Enter ability scores (3-18)")
abilities = [0, 0, 0, 0, 0, 0]
abilities[Ability.STRENGTH] = int(input("Strength: "))
abilities[Ability.DEXTERITY] = int(input("Dexterity: "))
abilities[Ability.CONSTITUTION] = int(input("Constitution: "))
abilities[Ability.INTELLIGENCE] = int(input("Intelligence: "))
abilities[Ability.WISDOM] = int(input("Wisdom: "))
abilities[Ability.CHARISMA] = int(input("Charisma: "))

for ability in abilities:
	if ability < 3 or ability > 18:
		print("Incorrect input. Please enter valid ability scores (3-18).")
		exit()

print("")
print("Here are your options according to 1st edition Advanced Dungeons & Dragons rules:")
for i in range(0, Race.NOF_RACES):
	valid_race(i, abilities)
