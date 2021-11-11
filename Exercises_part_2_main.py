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


def number_between(name_of_number, between_from, between_to):
    """
    function asks an integer number in a given interval
    :param name_of_number: a text to say to the user which kind of number do you ask, eg. age, interval etc.
    :param between_from:
    :param between_to:
    :return: selected number-int
    """

    while True:
        try:
            entered_number = int(input(f"Please enter a number! {name_of_number}= "))
            if between_from <= entered_number <= between_to:
                return entered_number
                # break
            else:
                print(f"That's not a valid option! Only numbers between {between_from} and {between_to}, please!")
        except ValueError:
            print("That's not a valid option! Only numbers between  {between_from} and {between_to} , please!")


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


my_numbers = [2, 17, 4, 8, 1, 7, 88, 6, 78, 4, 3, 120, 22, 1, 7, 8, 77, 44, 8, 7, 55, 6, 88, 8, 7, 99, 1022, 99, 85,
              8, 74, 53, 17, 7, 911, 8, 29]


def exercise1():
    # *********************************************************+**Ex.1
    # it gives out the occurrence of the entered number in a list
    print("\nExercise1 - Counting")

    print(my_numbers)

    my_number = enter_number("I want to find ")
    print("The occurrences of the number is: ", count_a_number(my_numbers, my_number))


def exercise2():
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
        i=len(numbers)
        print("Reversed using reversed loop")

        for i in range(len(numbers) - 1, 0, -1):
            print(f"{numbers[i]}, ", end='')

        print(numbers[i - 1])

        print("\nReversed2 using reversed() function")

        for a in reversed(numbers):
            if a == numbers[0]:
                print(f"{a} ")
            else:
                print(f"{a}, ", end='')

        print()

        if count_a_number(numbers, number) == 0:
            print(f"the number {number} has no occurrence in the list I can not change with 1")
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


def exercise3():
    # *********************************************************+**Ex.3
    # it looks for elements that the two lists have in common
    print("\nExercise3 - Comparing list elements")

    def compare_lists1(list1, list2):
        """
        it compares two lists and gives back the list of common elements
        :param list1:
        :param list2:
        :return:  common elements of above lists
        """
        print("\n The two lists to compare")
        print("      ", sorted(list1))
        print("      ", sorted(list2))
        return set(list2).intersection(list1)


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

    list_first = ["a", "k", "c", "Eva", "Adam"]
    list_second = ["c", "z", "Eva", "y", "o", "r"]

    print("\nFirst version of comparing lists using intersection function")
    print("Common elements:", sorted(compare_lists1(list_first, list_second)))
    print("\nSecond version of comparing lists using 'for' loop")
    print("Common elements:", sorted(compare_lists2(list_first, list_second)))



def exercise4():
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


def exercise5():
    # *********************************************************+**Ex.5
    # presents the usage of a dictionary
    print("\nExercise5 - Computer description")

    computers_dict = {
        "Type": "Notebook",
        "Brand": "Dell",
        "Price": 2000
    }

    def describe_computer(computer):
        """
        the method takes a dictionary and write to the console a fixed text -You have a TYPE from BRAND
        that costs PRICE€.-,
        finally it adds a new key to the dictionary.
        if a key is missing or it has an empty value, the function prints "unknown [Key]
        :param computer: it must have following three keys: "Type","Brand", "Price"
        :return: no return value
        """

        for key in computer:
            if computer[key] == "":
                computer[key] = "unknown" + key

        dtype = computer.get("Type") if computer.get("Type") is not None else "unknown type"
        dbrand = computer.get("Brand") if computer.get("Brand") is not None else "unknown brand"
        dprice = computer.get("Price") if computer.get("Price") is not None else "unknown price"

        print(f"\nYou have a {dtype} from {dbrand} that costs {dprice} €.")

        computer["OS"] = "Linux"
        print("\nAdding new key")
        print(computer)

    describe_computer(computers_dict)


def start_exercise():
    print("Please choose an Exercise!")
    selection = 0

    while 0 <= selection <= 9:
        print()
        selection = number_between(" Exercise 1-9 or 0 to exit", 0, 9)
        if selection == 1:
            exercise1()
        elif selection == 2:
            exercise2()
        elif selection == 3:
            exercise3()
        elif selection == 4:
            exercise4()
        elif selection == 5:
            exercise5()

        else:
            print("Thank you for running my Exercise!")
            break


start_exercise()
