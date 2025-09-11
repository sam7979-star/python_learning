def search_city():
    lst_size = int(input("Enter the size of the list:"))
    if lst_size <= 1:
        print("List Size must > 1:")
        return
    elements = []
    for i in range(lst_size):
        elements.append(input(f"Enter the {i+1} element into the List: "))
    print("List Size is:", lst_size)
    print("List element are:",elements)
    search_citi_name=input("Enter a Citi to search in the list element:")
    found = False
    for i in elements:
        if i.lower() == search_citi_name.lower():
            found=True
            break
    if found:
            print(f"The city you are searching is available in the List:{search_citi_name}")
    else:
            print(f"The city you are searching is not availabe in the List:{search_citi_name}")

'''for i in elements:
        if i.lower() == search_city_name.lower():
            print(f"\nThe city you are searching for is available in the list: {search_city_name}")
            break # Exit the loop if found
    else: # This 'else' block runs only if the for loop finishes without a 'break'
        print(f"\nThe city you are searching for is not available in the list: {search_city_name}")'''

search_city()

