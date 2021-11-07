my_numbers = [2, 17, 4, 8, 1, 7, 88, 6, 78, 4, 3, 120, 22, 1, 7, 8, 77, 44, 8, 7, 55, 6, 88, 8, 7, 99, 1022, 99, 85, 8,
              74, 53, 17, 7, 911, 8, 29]


def no_duplicates2(items):
    """
    it accepts a list of strings named items as argument and removes all
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

    print("\n Without duplicates, using new container ", new_items)
    return new_items


no_duplicates2(my_numbers)
