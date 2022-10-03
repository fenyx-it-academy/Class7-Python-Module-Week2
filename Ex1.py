lst = []
num=int(input("please enter ths shifting number: "))

while True:
    lst_item = input("please enter your list item, or press ENTER to end the list: ")
    if lst_item == "":
        break
    lst.append(lst_item)
lst_copy= lst.copy()  
print("your original list is: ",lst)
for i in range(len(lst)):
    if i+num < len(lst):
        lst[i+num]=lst_copy[i]
       
    else:
        lst[abs(len(lst)-(i+num))]= lst_copy[i]
        
print("your shifted list is: ",lst) 


