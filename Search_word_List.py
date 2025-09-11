def search_word_lst():
    lst_size = int(input("Enter the size of the list:"))
    if lst_size <= 1:
        return print("List Size must > 1:")
    elements = []
    for i in range(lst_size):
        elements.append(input(f"Enter the {i+1} element into the List: "))
    print("List Size is:", lst_size)
    print("List element are:",elements)
    search_word=input("Enter a Word to search in the list element:")
    count = 0
    res_lst = []
    for i in elements:
        if search_word.lower() in i:
            count+=1
            res_lst.append(i)
    print(f"Word {search_word} is present in the list element:",res_lst)
    print("Count is:",count)

search_word_lst()