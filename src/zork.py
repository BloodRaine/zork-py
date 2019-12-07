import items


def get_input():
    user_input = input("What do you do? ")
    return user_input.lower()


def kick_bucket():
    print("---------------------------------------------------------")
    print("You die.")
    print("---------------------------------------------------------")
    return continue_game()


def continue_game():
    user_input = input("Do you want to continue? Y/N ")
    if user_input.lower() == ("n"):
        return False
    if user_input.lower() == ("y"):
        return True


def room1():		# north of house
    print("---------------------------------------------------------")
    print("You find yourself at the edge of a beautiful lake aside rolling hills.")
    print("A small pier juts out into the lake.")
    print("A fishing rod rests on the pier.")
    print("(You can see a white house in the distance to the south.)")
    user_input = ''
    responses = ["go south", "swim", "fish"]
    while user_input != "kick the bucket":
        user_input = get_input()
        if user_input == "kick the bucket":
            return [1, False, kick_bucket()]
        elif user_input == responses[0]:
            return [4, True, True]
        elif user_input == responses[1]:
            print("---------------------------------------------------------")
            print("You don't have a change of clothes and you aren't here on vacation.")
        elif user_input == responses[2]:
            print("---------------------------------------------------------")
            print("You spend some time fishing but nothing seems to bite.")
        else:
            print("---------------------------------------------------------")


def room4():
    print("---------------------------------------------------------")
    print("You are standing in an open field west of a white house, with a boarded front door.")
    print("You can see a small lake to the north.")
    print("(A secret path leads southwest into the forest.)")
    print("There is a Small Mailbox.")

    user_input = ''
    responses = ["take mailbox", "open mailbox", "go north", "open door", "take boards", "look at house", "go southwest", "read leaflet"]
    while user_input != "kick the bucket":
        user_input = get_input()
        if user_input == "kick the bucket":
            return [4, False, kick_bucket()] 	# if the user kicks the bucket, return their last room number and alive = False
        elif user_input == responses[0]:
            print("---------------------------------------------------------")
            print("It is securely anchored.")
        elif user_input == responses[1]:
            print("---------------------------------------------------------")
            print("Opening the small mailbox reveals a leaflet.")
        elif user_input == responses[2]:
            return [1, True, True] 		# if the user goes north, switch to room 1 and is alive and continue
        elif user_input == responses[3]:
            print("---------------------------------------------------------")
            print("The door cannot be opened.")
        elif user_input == responses[4]:
            print("---------------------------------------------------------")
            print("The boards are securely fastened.")
        elif user_input == responses[5]:
            print("---------------------------------------------------------")
            print("The house is a beautiful colonial house which is painted white. It is clear that the owners must "
                  "have been extremely wealthy.")
        elif user_input == responses[6]:
            return [8, True, True]      # if user goes southwest, go to room 8 and return is alive and continue
        elif user_input == responses[7]:
            print("---------------------------------------------------------")
            print("Welcome to the Unofficial Python Version of Zork. Your mission is to find a Jade Statue.")
        else:
            print("---------------------------------------------------------")


def room8():
    print("---------------------------------------------------------")
    print("This is a forest, with trees in all directions. To the east, there appears to be sunlight.")

    user_input = ''
    responses = ["go west", "go north", "go south", "go east"]

    while user_input != "kick the bucket":
        user_input = get_input()
        if user_input == "kick the bucket":
            return [8, False, kick_bucket()] 	# if the user kicks the bucket, return their last room number and alive = False
        elif user_input == responses[0]:
            print("---------------------------------------------------------")
            print("You would need a machete to go further west.")
        elif user_input == responses[1]:
            print("---------------------------------------------------------")
            print("The forest becomes impenetrable to the North.")
        elif user_input == responses[2]:
            print("---------------------------------------------------------")
            print("Storm-tossed trees block your way.")
        elif user_input == responses[3]:
            return [9, True, True]
        else:
            print("---------------------------------------------------------")


def room9():
    print("---------------------------------------------------------")
    print("You are in a clearing, with a forest surrounding you on all sides. A path leads south.")
    print("There is an open grating, descending into darkness.")

    user_input = ''
    responses = ["go south", "descend grating"]

    while user_input != "kick the bucket":
        user_input = get_input()
        if user_input == "kick the bucket":
            return [9, False, kick_bucket()]  # if the user kicks the bucket, return their last room number and alive = False
        elif user_input == responses[0]:
            print("---------------------------------------------------------")
            print("You see a large ogre and turn around.")
        elif user_input == responses[1]:
            return [10, True, True]
        else:
            print("---------------------------------------------------------")


def room10():
    print("---------------------------------------------------------")
    print("You are in a tiny cave with a dark, forbidding staircase leading down.")
    print("There is a skeleton of a human male in one corner.")

    user_input = ''
    responses = ["descend staircase", "take skeleton", "smash skeleton", "light up room", "break skeleton", "go down staircase", "scale staircase"]

    while user_input != "kick the bucket":
        user_input = get_input()
        if user_input == "kick the bucket":
            return [10, False, kick_bucket()]
        elif user_input == responses[0] or user_input == responses[5] or user_input == responses[6]:
            return [11, True, True]
        elif user_input == responses[1]:
            print("---------------------------------------------------------")
            print("Why would you do that? Are you some sort of sicko?")
        elif user_input == responses[2]:
            print("---------------------------------------------------------")
            print("Sick person. Have some respect mate.")
        elif user_input == responses[3]:
            print("---------------------------------------------------------")
            print("You would need a torch or lamp to do that.")
        elif user_input == responses[4]:
            print("---------------------------------------------------------")
            print("I have two questions: Why and With What?")
        else:
            print("---------------------------------------------------------")


def room11():
    print("---------------------------------------------------------")
    print("You have entered a mud-floored room.")
    print("Lying half buried in the mud is an old trunk, bulging with jewels.")

    user_input = ''
    responses = ["open trunk"]

    while user_input != "kick the bucket":
        user_input = get_input()
        if user_input == "kick the bucket":
            return[11, False, kick_bucket()]
        elif user_input == responses[0]:
            print("---------------------------------------------------------")
            print("You have found the Jade Statue and have completed your quest!")
            return[11, True, continue_game()]   # if function returns 11, True, and True, restart game
            # if function returns 11, true, and false exit game
        else:
            print("---------------------------------------------------------")

