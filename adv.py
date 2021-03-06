from room import Room
from player import Player

# Declare all the rooms

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

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

player = Player(input('What is your name? '), room['outside'])

def player_welcome():
    print(f'Welcome {player.name}\nHave fun! Use n, e, s, w to navigate. \nIf you can not continue, enter "q".')
    print(f'You are in the {player.current_room.name}\n{player.current_room.description}')
    ## need if playname is set, then don't run this function

## function for commands the player can input 
def select_command():
    player_input = (input('What now?'))
    if player_input == 'q': 
        player_quit()
    elif player_input == 'n' or player_input == 'e' or player_input == 's' or player_input == 'w':
        player.movePlayer(player_input)
        print()
        print(f'Current Room: {player.current_room.name}\n{player.current_room.description}')
        print()
    else:
        print(f'Please use n, e, s, w')

## function to quit
def player_quit():
    print(f'Are you sure you would like to leave?')
    quit = (input('Enter "y" to leave. Enter "n" to continue adventuring. '))
    if quit == 'n':
        print('Good choice!')
        select_command()
    elif quit == 'y':
        print("Good bye!")
        sys.exit()
    else:
        print("Please select 'n' or 'y'")

## game start
player_welcome()

while True:
    select_command() 
