def find_missing_numbers():
    lst_size = int(input("Enter the size of the list: "))
    if lst_size <= 1:
        print("List size should be greater than 1")
        return

    elements = []
    for i in range(lst_size):
        num = int(input(f"Enter element {i + 1}: "))
        elements.append(num)

    print("\nInput list:", elements)

    # Sort the list to find gaps
    elements.sort()
    print("Sorted list:", elements)

    min_val = min(elements)
    max_val = max(elements)

    # Generate the full expected range
    full_range = set(range(min_val, max_val + 1))

    # Find missing numbers by set difference
    missing_numbers = sorted(list(full_range - set(elements)))

    if missing_numbers:
        print("Missing numbers are:", missing_numbers)
    else:
        print("No numbers are missing in the list.")

find_missing_numbers()