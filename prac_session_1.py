def samp():
    lst_size = int(input("Enter the size of the List:"))
    if lst_size <= 1:
        return print("List should be > 1:")
    elements = []
    for i in range(lst_size):
        elements.append(int(input(f"Enter the {i+1} Elements into the List:")))
    print("List Size is:",lst_size)
    print("Elements in the List are:",elements)


samp()