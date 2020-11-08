#!/usr/bin/python

# Emulate surprise and initiative for one combat with fixed participants

import random

class Character:
	def __init__(self, name, reaction, surprised, surprises):
		self.name = name
		self.reaction = reaction
		self.surprised = surprised
		self.surprises = surprises

sides = [
# Example party, modify inline below:
		[	Character("Aggro the Axe",	+0,	2.0/6,	2.0/6),
			Character("Abner",		+0,	2.0/6,	2.0/6),
			# Aragorn is a Ranger, and he has a high Dexterity:
			Character("Aragorn",		+3,	1.0/6,	3.0/6),
			# Arkayn has a low Dexterity:
			Character("Arkayn",		-1,	2.0/6,	2.0/6),
			Character("Arlanni",		+0,	2.0/6,	2.0/6)],
# Example monsters, again modify inline below:
			# Source: AD&D 1e Monster Manual
		[	Character("Cloud Giant",	+0,	1.0/6,	2.0/6),
			Character("Bugbear",		+0,	2.0/6,	3.0/6)],
		[	Character("Invisible stalker",	+0,	2.0/6,	5.0/6)]]

def roll(sides):
	return random.randint(1, sides)

# Determine surprise targets
surprised = []
surprises = []
for side in sides:
	# To determine whether a side is surprised, the most favorable member's
	# rate is used.
	# Source: AD&D 1e Dungeon Masters Guide p. 61
	lowest_surprised = 1.0 # unrounded
	for character in side:
		if character.surprised < lowest_surprised:
			lowest_surprised = character.surprised
	surprised.append(round(lowest_surprised * 6))
	# To determine whether a side surprises, the least favorable member's
	# rate is used.
	# Source: MISSING, but a call was needed
	lowest_surprises = 1.0 # unrounded
	for character in side:
		if character.surprises < lowest_surprises:
			lowest_surprises = character.surprises
	surprises.append(round(lowest_surprises * 6))

print("Sides are surprised at: " + str(surprised))
print("and surprise the others at: " + str(surprises))

targets = []
for i in range(len(sides)):
	lowest_surprises = 6 # rounded
	for j in range(len(sides)):
		if i != j:
			# Of multiple opposing sides, use the least favorable
			# side's rate again.
			# Source: MISSING, but a call was needed
			if surprises[j] < lowest_surprises:
				lowest_surprises = surprises[j]
	# Combine rates
	result = lowest_surprises + surprised[i] - 2 # out of 6
	if result < 0:
		result = 0
	targets.append(result)

print("so each side's surprise targets are: " + str(targets))

# Roll for surprise
surprise_segments = []
for target in targets:
	result = roll(6)
	print("Rolled: " + str(result) + " against target " + str(target))
	if (result > target):
		surprise_segments.append(0)
	else:
		surprise_segments.append(result)

# Adjust for reaction
order = {}
for i in range(len(sides)):
	for character in sides[i]:
		segment = surprise_segments[i]
		if surprise_segments[i] > 0:
			segment -= character.reaction
		if segment < 0:
			segment = 0
		order.setdefault(segment, []).append(character.name)

# Walk through surprise round
print("")
print("Start of surprise round:")
unsurprised = []
if 0 in order:
	unsurprised = [order[0]]
	print(str(order[0]) + " may proceed unsurprised.")
for i in range(1, max(order) + 1):
	print("Segment " + str(i) + ":")
	print(str(unsurprised) + " may act.")
	raw_input("Press a key to continue to the next segment...")
	if i in order:
		print(str(order[i]) + " may proceed, no longer surprised.")
		unsurprised.append(order[i])
print("")
print("Surprise round is over.")

# Walk through other combat rounds
rounde = 0
while True:
	rounde += 1
	print("")
	print("Combat round: " + str(rounde))
	initiative = {}
	for side in sides:
		result = roll(6)
		print("Rolled " + str(result))
		for character in side:
			initiative.setdefault(result, []).append(character.name)
	while initiative:
		highest = initiative[max(initiative)]
		print("    " + str(highest) + " may act next (simultaneously).")
		del initiative[max(initiative)]
		raw_input("    Press a key to continue to the next turn...")
	raw_input("Press a key to continue to the next round...")
