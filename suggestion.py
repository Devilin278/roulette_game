import config


class Suggestion:
    def __init__(self, landed_number, arr_index, user_range):
        self.wheel = config.wheel
        self.wheel_length = config.wheel_length
        self.landed_number = landed_number
        self.arr_index = arr_index
        self.user_range = user_range

    def range_selection(self):
        num_list = []

        # Loop through desired range
        for i in range(abs(self.user_range)):
            # Check range to right or left side of the selection
            if self.user_range > 0:
                index = self.arr_index + i + 1
            else:
                index = self.arr_index - i - 1
            index = int(config.ensure_loop(index))

            num_list.append(self.wheel[index])

        return num_list

    # def print_suggestion(self):
        # if self.user_range > 0:
        #     print("Right of:", self.landed_number, "are these numbers:", self.range_selection())
        # elif self.user_range < 0:
        #     print("Left of:", self.landed_number, "are these numbers:", self.range_selection())

    def suggest_play_numbers(self):
        landed_number = self.arr_index
        quad_dict = config.qaudrant
        for key in quad_dict:
            print('These are the Suggested playable numbers based on 1 /', key, 'quadrant:')
            value_arr = quad_dict[key]
            self.user_range = value_arr[0]
            for value in value_arr[1]:
                self.arr_index = self.arr_index + value
                suggestion_list = self.get_suggestion_list()
                print(suggestion_list)
                self.arr_index = landed_number

    def get_suggestion_list(self):
        # abs for right side of the numbers
        self.user_range = abs(self.user_range)
        suggestion_list = self.range_selection()
        # targeted number itself is added
#        print('Current Index:', self.arr_index)
        suggestion_list.insert(0, self.wheel[config.ensure_loop(self.arr_index)])
        # -abs for right side of the numbers
        self.user_range = -abs(self.user_range)
        new_list = self.range_selection()
        new_list.reverse()
        suggestion_list = new_list + suggestion_list
        return suggestion_list
