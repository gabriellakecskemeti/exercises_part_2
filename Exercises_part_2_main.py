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
print("\nExercise1 - Counting")

my_numbers = [2, 17, 4, 8, 1, 7, 88, 6, 78, 4, 3, 120, 22, 1, 7, 8, 77, 44, 8, 7, 55, 6, 88, 8, 7, 99, 1022, 99, 85, 8,
              74, 53, 17, 7, 911, 8, 29]
print(my_numbers)


def count_a_number(numbers: list, number: int):
    """
    this method search and counts the given number in the given list of numbers
    :param numbers: a list of integer numbers
    :param number: one integer number
    :return: occurrence of the number in the numbers(list)
    """
    counter = 0
    for x in numbers:

        if x == number:
            counter = counter + 1

    return counter


my_number = enter_number("I want to find ")
print("The occurrences of the number is: ", count_a_number(my_numbers, my_number))
input("\nPress Enter to continue!")

# *********************************************************+**Ex.2
# it gives out the occurrence of the entered number in a list
print("\nExercise2 - Playing with lists")


def play_with_lists(numbers, number):
    print("Reversed using reversed loop")

    for i in range(len(numbers) - 1, 0, -1):
        print(f"{numbers[i]}, ", end='')
    print(numbers[i - 1])

    print("\nReversed2 using reversed() function")

    for i in reversed(numbers):
        if i == numbers[0]:
            print(f"{i} ")
        else:
            print(f"{i}, ", end='')

    print()
    print(numbers)
    print(f"I am replacing the number {number} in the list with 1")
    for i in range(0, len(numbers), 1):
        if numbers[i] == number:
            numbers[i] = 1

    print(f"Changed list: \n{numbers}")

    print(f"\nSorted:\n{sorted(numbers)}")
    #I chose the sorted() function, because in this way the list remain untouched.



print(my_numbers)
while True:
    my_number = enter_number("change with 1")
    if my_number in my_numbers:
        break
    else:
        print("This number is not in the list, I can not change it. Enter an existing number from the list please!")

play_with_lists(my_numbers, my_number)
