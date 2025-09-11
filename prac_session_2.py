'''first_name = 'srinivasa'
last_name = 'udutha'
full_name = first_name+ " "+last_name
print(full_name)
print(len(full_name))
print(full_name.upper())
print(full_name.lower())'''
#Printing the List value with there index numbers
'''def lst_exam():
    lst_size = int(input("Enter the size of List:"))
    if lst_size <= 1:
        return print("Size of List > 1")
    elements = []
    for i in range(lst_size):
        elements.append(int(input(f"Enter {i+1} element in the List:")))
    print("Size of the List is:", lst_size)
    print("Element in the List are:", elements)

    for index, value in enumerate(elements):
        print(f"Value in the {index} Index is {value}")
lst_exam()
'''
numbers = [1,2,3,4,5]
for i in range(len(numbers)):
    #numbers[i] = numbers[i]*numbers[i]
    numbers[i]= numbers[i]**2
print(numbers)
