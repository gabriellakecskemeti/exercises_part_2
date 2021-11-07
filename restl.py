while True:  # asking for a number to change later with 1
    my_number = enter_number("to change with 1")
    if my_number in my_numbers:  # checking if this number exist in the list
        break
    else:
        print("This number is not in the list, I can not change it. Enter an existing number from the list please!")

play_with_lists(my_numbers, my_number)

input("\nPress enter to continue!")
print("\nSecond solution for replacing given number with one, without checking if the number exist in the list.")
