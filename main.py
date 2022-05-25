# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

# Create a variable for every player that scored

score_1 = 'Ruud Gullit'
score_2 = 'Marco van Basten'

# Create a variable for each minute of the match that a goal was scored in

goal_0 = 32
goal_1 = 54

# Using the +-operator, create a string that reports on who scored when

scorers = score_1 + ' ' + str(goal_0) + ', ' + score_2 + ' ' + str(goal_1)
print(scorers)

# Use f-strings or the +-operator to create a single string with information about who scored when

report = f'{score_1} scored in the {goal_0}nd minute\n{score_2} scored in the {goal_1}th minute'

# Choose a player that played in the soccer match and store his name as a string in the variable player.

player = 'Frank Rijkaard'

# first_name: use slicing and the find-method (help) to isolate and store the player's first name.
"""code is niet generiek genoeg. Als je een andere naam invoert dan doet ie het niet. met /'.find' kan je de plek van de spatie vinden 
en daarop je code schrijven"""


first_name = player[:player.find(' ')]
print(first_name)

# last_name_len: use find, slicing and len to isolate and store the length of their last name.

last_name = player[(player.find(' ')+1):]
print(last_name)

last_name_len = len(last_name)
print(last_name_len)

# name_short: isolate and store the player's name in this format: G. von Examplestein

name_short = f"{player[0]}.{player[player.find(' '):]}"
print(name_short)

# chant: this is what the crowd chants when it looks like your player is going to score a goal 
# -- their first name plus an exclamation mark(!), x-times, where x is the number of characters in their first name. 
# Make sure the last character of this string is not a space!

chant_1 = f'{first_name}! ' * len(first_name)
chant = chant_1[:-1]
print(chant)


# good_chant: Make super-sure the last character of chant is not a space by using the inequality operator (!=). 
# Try this in your REPL for an example: print(2 != 3). Also try: print(2 != 2).


good_chant = chant[-1] != ' '
print(good_chant)



