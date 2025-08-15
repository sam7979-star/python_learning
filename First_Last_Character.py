#Implement a function which takes the string type list as parameter and returns the count of
# the number of strings where the string length is 2 or more and the first and the last characters are same.

def first_last():
    lst_size = int(input("Enter the size of the List:"))
    if lst_size <=1:
        return print("Size of the List should be >1")
    elements = []
    for i in range(lst_size):
        elements.append(input(f"Enter the {i+1} element in the List:"))
    print("Size of the List is:",lst_size)
    print("Element in the List is:",elements)
    total = 0
    for i in elements:
        if len(i)>2 and i[0]==i[-1]:
            total +=1
    print(total)




first_last()
