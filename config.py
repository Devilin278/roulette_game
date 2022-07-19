# List of Roulette Wheel Numbers
wheel = ['00', '27', '10', '25', '29', '12', '8', '19',
         '31', '18', '6', '21', '33', '16', '4', '23',
         '35', '14', '2', '0', '28', '9', '26', '30',
         '11', '7', '20', '32', '17', '5', '22', '34',
         '15', '3', '24', '36', '13', '1']

wheel_length = len(wheel) - 1

qaudrant = {2: [5, [0, 19]],
            3: [4, [0, 13, -13]],
            4: [3, [0, 9, 19, -9]]}


def ensure_loop(index):
    # Change index value to cycle around
    if index > wheel_length:
        index = (index % wheel_length) - 1
    elif index < 0:
        index = (index % wheel_length) + 1
    return index
