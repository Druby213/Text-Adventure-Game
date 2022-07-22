# Dylan Ruby

# Dictionary of the all the rooms and their connecting rooms, descriptions, and items
rooms = {
    'Research Room': {
        'North': 'Bedroom',
        'East': 'Laboratory',
        'South': 'Dinning Room',
        'West': 'Armory',
        'Description': 'You are currently in the Research Room. In the center of the room is the metal table you woke '
                       'up on. There are strange devices hanging above the table.',
        'Item': []
    },
    'Laboratory': {
        'North': 'Storage',
        'West': 'Research Room',
        'Description': 'You are in some sort of Laboratory. There are multiple test tubes and beakers filled with '
                       'strange liquids that vary in color',
        'Item': ['Health Serum']
    },
    'Dinning Room': {
        'North': 'Research Room',
        'East': 'Kitchen',
        'Description': 'You are in a smalling Dinning Room. The table is set with futuristic looking plates and '
                       'utensils. It looks like the aliens were getting ready for dinner.',
        'Item': ['Laser Knife']
    },
    'Armory': {
        'East': 'Research Room',
        'Description': 'You are in an armory with helmets and and suits varying in shape and size.',
        'Item': ['Helmet']
    },
    'Bedroom': {
        'East': 'Control Room',
        'South': 'Research Room',
        'Description': 'You entered the Bedroom lined with floating beds.',
        'Item': ['Ray Gun']
    },
    'Control Room': {
        'East': 'Bedroom',
        'Description': 'The Aliens are currently flying the ship into the stars'
    },
    'Storage': {
        'South': 'Laboratory',
        'Description': 'You have entered a storage room filled with gizmos and gadgets, most have a thick layer of dust',
        'Item': ['Nano Suit']
    },
    'Kitchen': {
        'West': 'Dinning Room',
        'Description': 'You have entered the kitchen, which has a strong aroma coming from the pot boiling on the '
                       'stove. Might as well grab a snack for the road while you are here.',
        'Item': ['Apple']
    }
}

# The room the player is currently in
current_room = rooms['Research Room']

# in the main function the player will be prompted to enter a command which is assigned to choice
choice = ''

# the players inventory which will expand as they pick up items
player_bag = []


# Introduce the player to the game and show them how to play
def show_instructions():
    print('-' * 45, 'introduction', '-' * 45)
    print('You have woken up on a metal table in what appears to be an alien space ship. ')
    print('Search the ship for items that will help you defeat the aliens, then make your way to the control room.')
    print('Defeat the aliens and fly the ship back to Earth.')
    print('-' * 46, 'How to play', '-' * 46)
    print("To move type: Go North, Go East, Go South, or Go West")
    print("To pick up an item and add it to your inventory type: Get 'item name' ")
    print('To display your inventory and see your location type: Status')
    print('To end the game early type: Exit')
    print('If you need to see this menu again type: Help')
    print('-' * 105)


# print the player's current room, the items in the room, and the items in the players bag
def player_status():
    print(current_room['Description'])
    print('Items in room: {}'.format(', '.join(current_room['Item'])))
    print('Your bag: {}'.format(', '.join(player_bag)))


# the main game function
def main_function(choice):
    show_instructions()
    player_status()
    global current_room

    # While loop that will exit when the user is done playing
    while choice != 'Exit':

        # Tell the play what room they are currently and get the direction they would like to move
        choice = input('What would you like to do?: ')

        # check if the player entered a go command
        if choice.split()[0] == 'Go':

            # if the direction is part of the current rooms dictionary move the player to the new room
            if choice.split()[1] in current_room.keys() and choice.split()[1] != 'Description':
                new_room = current_room[choice.split()[1]]
                current_room = rooms[new_room]

                # if the villain is in the new room and the player doesn't have all items show the failed screen
                if current_room == rooms['Control Room'] and len(player_bag) < 6:
                    print(
                        'When you walk into the control room, The aliens flying the ship turn to look at you. You '
                        'realized you were not prepared moments before getting hit by a Ray Gun blast.')
                    print('GAME OVER!')
                    break
                    
                # if the villain is in the new room and the player has all 6 items show the win screen
                elif current_room == rooms['Control Room'] and len(player_bag) >= 6:
                    print('You entered the control room and hit the aliens with a Ray Gun blast before they could '
                          'react. You then take control of the ship and start flying back to earth.')
                    print('YOU WIN!')
                    break
                    
                # show the player status if the room does not contain the villain
                else:
                    player_status()

            # if the direction is not in the dictionary ask the player to enter a valid command
            else:
                print('That is not an option, please try again')

        # check if the player entered the get command
        elif choice.split()[0] == 'Get':

            # if the entered item is one word and in the room add it to the players bag and remove from the room
            # dictionary
            if choice.split()[1] in current_room['Item']:
                print('You picked up the {}!'.format(choice.split()[1]))
                item = choice.split()[1]
                current_room['Item'].remove(item)
                player_bag.append(item)
                
            # if the entered it is two words and in the room add it to the players bag and remove from the room
            # dictionary
            elif choice.split()[1] + ' ' + choice.split()[2] in current_room['Item']:
                print('You picked up the {} {}!'.format(choice.split()[1], choice.split()[2]))
                item = choice.split()[1] + ' ' + choice.split()[2]
                current_room['Item'].remove(item)
                player_bag.append(item)

            # if the item entered is not in the room tell the player they can't get the item
            else:
                print('You can\'t get that item!')

        # show the game instructions if the player enters the Help command
        elif choice == 'Help':
            show_instructions()

        # show the player status if the player enters the status command
        elif choice == 'Status':
            player_status()

        # If the player types 'Exit' the it will say good by and exit the loop
        elif choice == 'Exit':
            print('Good Bye!')

        # if the player enters an invalid command ask them to try entering something else
        else:
            print('That is not an option, please try again')


# call main game loop
if __name__ == "__main__":
	main_function(choice)
