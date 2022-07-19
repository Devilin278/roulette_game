# Python3 Roulette program to demonstrate the use of
# circular array without using extra memory space

import config
from suggestion import Suggestion
from spin import Spin

past_numbers = []

while True:
    while True:
        keep_playing = str(input('Would you like to spin? (Yes/No)'))
        if (keep_playing.upper() == 'YES') or (keep_playing.upper() == 'Y'):
            # asking for how wide of selection from starting number selection
            if not past_numbers:
                while True:
                    user_range = 5
                    break
                    # try:
                    #     user_range = int(input('Please enter the suggestion range: '))
                    #     break
                    # except ValueError as v:
                    #     print("Entry is not an INTEGER. Please Only Enter INTEGERS: ", v)
                    #     continue
            break
        elif (keep_playing.upper() == 'NO') or (keep_playing.upper() == 'N'):
            exit()
        else:
            print('Please Enter ONLY "Yes" or "No"')

    landed_number = Spin().generate()
#    landed_number = "00"
#    print(config.wheel)
    arr_index = config.wheel.index(landed_number)

    # Print Suggested numbers in entered range around the number where the ball landed
    # selection_list = Suggestion(landed_number, arr_index, user_range).range_selection()
    # print("Right of:", landed_number, "are these numbers:", selection_list)
    # selection_list = Suggestion(landed_number, arr_index, -abs(user_range)).range_selection()
    # print("Left of:", landed_number, "are these numbers:", selection_list)

    # Store the last number to the front of the list and print the list
    past_numbers.insert(0, landed_number)
    print('Past winning numbers are:', past_numbers)

    Suggestion(landed_number, arr_index, user_range).suggest_play_numbers()
