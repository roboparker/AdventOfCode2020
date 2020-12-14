def get_seat_availability():
    rows = 128
    columns = 8
    data = open('input/day5.txt', 'r')
    seats = [False] * (rows * columns)
    for line in data:
        row_range = (0, 127)
        column_range = (0, 7)
        for char in line:
            if char == "F":
                row_range = (row_range[0], row_range[1] - int((row_range[1] - row_range[0] + 1) / 2))
            elif char == "B":
                row_range = (row_range[0] + int((row_range[1] - row_range[0] + 1) / 2), row_range[1])
            elif char == "L":
                column_range = (column_range[0], column_range[1] - int((column_range[1] - column_range[0] + 1) / 2))
            elif char == "R":
                column_range = (column_range[0] + int((column_range[1] - column_range[0] + 1) / 2), column_range[1])
        seat = (row_range[0] * columns + column_range[0])
        seats[seat] = True
    data.close()
    return seats


def challenge_5_1():
    availability = get_seat_availability()
    for i in range(len(availability), 0, -1):
        if availability[i - 1]:
            print("Highest taken seat is", i - 1, availability[i - 1])
            break


def challenge_5_2():
    availability = get_seat_availability()
    for i in range(len(availability), 0, -1):
        if i == 1 or i == len(availability):
            continue  # cant be first or last seat
        if not availability[i - 1] and availability[i - 2] and availability[i]:
            print("Your seat is ", i - 1)
            break
