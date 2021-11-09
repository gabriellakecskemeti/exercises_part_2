# *********************************************************+**Ex.5
# presents the usage of a dictionary
print("\nExercise5 - Computer description")

computers_dict = {
    "Type": "Notebook",
    "Brand": "Dell",
    "Price": ""
}

def describe_computer(computer):
    """
    the method takes a dictionary and write to the console a fixed text -You have a TYPE from BRAND that costs PRICE€.-,
    finally it adds a new key to the dictionary.
    :param computer: it must have following three keys: "Type","Brand", "Price"
    :return: no return value
    """

    for key in computer:
        if computer[key] == "":
            computer[key] = "unknown " + key

    dtype = computer.get("Type") if computer.get("Type")!= None else "unknown type"
    dbrand = computer.get("Brand") if computer.get("Brand")!= None else "unknown brand"
    dprice = computer.get("Price") if computer.get("Price")!= None else "unknown price"

    print(f"\nYou have a {dtype} from {dbrand} that costs {dprice} €.")

    computer["OS"] = "Linux"
    print("\nAdding new key")
    print(computer)


describe_computer(computers_dict)
