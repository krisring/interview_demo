# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import unittest


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def get_square_and_cube(number):
    square = number ** 2
    cube = number ** 3
    return square, cube


def print_seat(seat):
    for item in seat:
        print(f"${item}")
    print("-"*15)
    total = get_seat_total(seat)
    print(f"Total: ${total}")


def get_seat_total(seat):
    total = 0
    for dish in seat:
        total = total + dish
    return total


def main():
    seats = [[19.95], [20.45 + 3.10], [7.00 / 2, 2.10, 21.45], [7.00 / 2, 2.10, 14.99]]

    grand_total = 0

    for seat in seats:
        print_seat(seat)
        grand_total = grand_total + get_seat_total(seat)
        print("\n")
        print("=" * 15)
    print(f"Grand total: ${grand_total}")


def print_numbers(n):
    print(f"{n}")
    n -= 1
    if n:
        print(f"Current n: {n}")
        print_numbers(n)
    if not n:
        print(f"{n}")

    n += 1
    print(f"Current n {n}")
    print(f"{n}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    unittest.main()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
