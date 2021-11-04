def enter_number(name_of_number):
    """
    function asks one number and check the entered value, it gives an error message if it is not an integer
    :param name_of_number: a text to say to the user which kind of number do you ask, eg. age, interval etc.
    :return: entered number
    """
    while True:
        try:
            number = int(input(f"Please enter a number!  {name_of_number}= "))
            break
        except ValueError:
            print("Only numbers, please!")

    return number


# *********************************************************+**Ex.1
# it gives out the occurrence of the entered number in a list
print("Exercise1 - Counting")


my_numbers = [2, 4, 8, 1, 7, 88, 22, 1, 7, 8, 77, 44, 8, 7, 55, 8, 7, 99, 1022, 99, 85, 8, 74, 53, 17, 7, 911, 8, 29]
print(my_numbers)

def count_a_number(numbers: list, number: int):
    counter = 0
    for x in numbers:

        if x == number:
            counter = counter + 1

    return counter


my_number = enter_number("I want to find ")
print("The occurrences of the number is: ", count_a_number(my_numbers, my_number))
