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
    """
    method write list in reversed order to the console, than ask a number.
    It replaces the given number in the list with 1.
    print out the list in descending order.
    The list remain untouched after printing.
    :param numbers: list of integer numbers
    :param number: the integer number, what you want to change with 1
    :return:
    """
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
    if count_a_number(numbers, number) == 0:
        print(f"the number {number} has no occurence in the list I can not change with 1")
    else:
        print(numbers)
        print(f"I am replacing the number {number} in the list with 1")
        for i in range(0, len(numbers), 1):
            if numbers[i] == number:
                numbers[i] = 1

        print(f"Changed list: \n{numbers}")

    print(f"\nSorted in descending order:\n{sorted(numbers, reverse=True)}")  # print descending order
    # I chose the sorted() function, because in this way the list remain untouched.


print(my_numbers)

my_number = enter_number("to change with 1")
play_with_lists(my_numbers, my_number)

input("\nPress Enter to continue!")

# *********************************************************+**Ex.3
# it looks for elements that the two lists have in common
print("\nExercise3 - Comparing list elements")

my_numbers2 = [1, 2, 4, 5, 120, 73, 27]


def compare_lists(list1, list2):
    """
    it compares two lists and gives back the list of common elements
    :param list1:
    :param list2:
    :return:  common elements of above lists
    """
    print("\n The two lists to compare")
    print("      ",sorted(list1))
    print("      ",sorted(list2))
    return set(list2).intersection(list1)


print("Common elements \n",
      compare_lists(my_numbers, my_numbers2))  # calling the function to compare and print the result

input("\nPress Enter to continue!")


def compare_lists2(list1, list2):
    """
    it compares two lists using for loop, and gives back the list of common elements
    :param list1:
    :param list2:
    :return:  common elements of above lists
    """
    print("\nThe two lists to compare")
    print("      ", sorted(list1))
    print("      ", sorted(list2))
    slist1 = set(list1)
    slist2 = set(list2)
    common_list = []
    for a in slist1:
        for b in slist2:
            if a == b:
                common_list = a
    return common_list


list1 = ["a", "k", "c", "Eva", "Adam"]
list2 = ["c", "z", "Eva", "y", "o", "r"]
print("\nSecond version of comparing lists using 'for' loop")
print("Common elements:", sorted(compare_lists(list1, list2)))

input("\nPress Enter to continue!\n")

# *********************************************************+**Ex.4
# filter out duplicate elements
print("\nExercise4 - No duplicates!")

d_list = ["a", "k", "c", "Eva", "Adam", "a", "k", "Adam", "a"]


def no_duplicates(items):
    """
    it accepts a list of strings -but also integers- named items as argument and removes all
    duplicate values from the list and it uses a container
    :param items: list of strings, but ist works also with list of numbers
    :return: list without duplicates
    """
    items.sort()
    print(f"\nList containing duplicates \n {items}")
    new_items = [items[0]]

    y = 0  # second counter
    for x in range(1, (len(items))):
        if items[x] != items[y]:
            new_items.append(items[x])
        y += 1

    return new_items


print("\n Without duplicates, using new container ", no_duplicates(d_list))


def remove_duplicates_my_way(items):
    """
    it accepts a list of strings named items as argument and removes all
    duplicate values from the list without using a container
    :param items: list of strings, but ist works also with list of numbers
    :return: list without duplicates
    """
    print(f"\nList containing duplicates \n {sorted(items)}")

    return sorted(set(items))


print("\n Without duplicates, no new container ", remove_duplicates_my_way(my_numbers))


# *********************************************************+**Ex.5
# presents the usage of a dictionary
print("\nExercise5 - Computer description")