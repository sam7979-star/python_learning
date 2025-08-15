lst = [1,2,3,4,5]
cust_lst = []
for i in lst:
    cust_lst.append(str(i))
cust_lst = "|".join(cust_lst)
print(cust_lst)
