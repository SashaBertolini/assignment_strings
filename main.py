# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

# Create a variable for every player that scored

Score_1 = 'Ruud Gullit'
Score_2 = 'Marco van Basten'

# Create a variable for each minute of the match that a goal was scored in

goal_0 = 32
goal_1 = 54

# Using the +-operator, create a string that reports on who scored when

scorers = Score_1 + ' ' + str(goal_0) + ', ' + Score_2 + ' ' + str(goal_1)
print(scorers)

# Use f-strings or the +-operator to create a single string with information about who scored when

report = f'{Score_1} scored in the {goal_0}nd minute\n{Score_2} scored in the {goal_1}th minute'

# Choose a player that played in the soccer match and store his name as a string in the variable player.

player = 'Frank Rijkaard'

# first_name: use slicing and the find-method (help) to isolate and store the player's first name.

x = player.find('Frank')
print(x)

first_name = player[:5]
print(first_name)

# last_name_len: use find, slicing and len to isolate and store the length of their last name.

y = player.find('Rijkaard')
print(y)

last_name_len = len(player[6:])

# name_short: isolate and store the player's name in this format: G. von Examplestein

name_short = f'{player[0]}. {player[6:]}'

# chant: this is what the crowd chants when it looks like your player is going to score a goal 
# -- their first name plus an exclamation mark(!), x-times, where x is the number of characters in their first name. 
# Make sure the last character of this string is not a space!

chant_1 = f'{player[:5]}! ' * len(player[:5])
chant = chant_1[:34]
print(chant)


# good_chant: Make super-sure the last character of chant is not a space by using the inequality operator (!=). 
# Try this in your REPL for an example: print(2 != 3). Also try: print(2 != 2).


good_chant = (chant[-1] != str(''))
print(chant != good_chant)

print(chant[-1] != str(''))



