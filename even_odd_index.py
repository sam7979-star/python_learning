def odd_even_index_list():
    lst_size1 = int(input("Enter the Size of the 1st List:"))
    lst_size2 = int(input("Enter the Size of the 2nd List:"))
    if lst_size1 <= 1 or lst_size2 <=1:
        return print("Size of the Both List should be > 1")
    lst1 =[]
    lst2 =[]
    for i in range(lst_size1):
        lst1.append(int(input(f"Enter the {i+1} element in to the List1:")))
    for i in range(lst_size2):
        lst2.append(int(input(f"Enter the {i+1} element in to the List2:")))
    print("Size of the List1:",lst_size1)
    print("Elements in the List1:",lst1)
    print("Size of the List2:", lst_size2)
    print("Elements in the List2",lst2)
    odd_element_index = lst1[1::2]
    print("Odd Index Element in 1st List is:", odd_element_index)
    even_element_index = lst2[0::2]
    print("Even Index Elements in 2nd List is:", even_element_index)
    lst3 = odd_element_index+even_element_index
    print("Total List Element in the List3 are:",lst3)
    '''
    lst3.extend(odd_element_index)
    lst3.extend(even_element_index)
    print("Total List Element in the List3 are:",lst3)
    '''

odd_even_index_list()
