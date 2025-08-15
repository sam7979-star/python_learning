def odd_even_list():
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

    lst3 = []
    for i in lst1:
        if i%2==0:
            lst3.append(i)
    for i in lst2:
        if i%2!=0:
            lst3.append(i)
    print("Even Element from 1st List & Odd Element from 2nd List:",lst3)

odd_even_list()
