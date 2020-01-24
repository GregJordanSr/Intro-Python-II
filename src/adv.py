from room import Room
from player import Player 

# Declare all the rooms
# Below are

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']

room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']

room['overlook'].s_to = room['foyer']

room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
ebo = Player("Qadir", current_room = room["outside"])
# Write a loop that:
# * Waits for user input and decides what to do.


while True:
    choice = input("Welcome " {ebo.name} " \n You were brave enough to take on this challenge and traverse my layer\n Choose your path and enter [N]orth, [S]outh, [E]ast, [W]est or [Q]uit: ")

    if choice == "q":
        break
    else:
    
    if ebo.current_room.n_to is not None:
        print(f"before the move: {ebo.current_room}" + "\n") 
        ebo.move(new_room = ebo.current_room.n_to) 
        print(f"After the move: {ebo.current_room}")

    else:
        print(f"You have reached deadend, choose another direction")

# * Prints the current room name
#
# * Prints the current description (the textwrap module might be useful here).

