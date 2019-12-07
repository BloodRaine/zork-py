# Main game file

import zork

alive = True
continue_game = True
room_num = 4
items = []

print("---------------------------------------------------------")
print("Welcome to Zork - The Unofficial Python Version.")
while alive or continue_game:
    alive = True
    if room_num == 4:
        output = zork.room4()
        room_num = output[0]
        alive = output[1]
        continue_game = output[2]
        if not alive and continue_game:
            room_num = 4

    elif room_num == 1:
        output = zork.room1()
        room_num = output[0]
        alive = output[1]
        continue_game = output[2]
        if not alive and continue_game:
            room_num = 4

    elif room_num == 8:
        output = zork.room8()
        room_num = output[0]
        alive = output[1]
        continue_game = output[2]
        if not alive and continue_game:
            room_num = 4

    elif room_num == 9:
        output = zork.room9()
        room_num = output[0]
        alive = output[1]
        continue_game = output[2]
        if not alive and continue_game:
            room_num = 4

    elif room_num == 10:
        output = zork.room10()
        room_num = output[0]
        alive = output[1]
        continue_game = output[2]
        if not alive and continue_game:
            room_num = 4

    elif room_num == 11:
        output = zork.room11()
        room_num = output[0]
        alive = output[1]
        continue_game = output[2]
        if continue_game:
            room_num = 4

