list=[]
while True:
    item= input("insert your element: ")
    list.append(item)
    choice= input("press 'Enter' to continue or type 'Quit' to stop inserting!")
    if choice.lower() == "quit":
        break
print(list)
len= len(list)
num= int(input("write your shifting number? + will shift to the right, - will shift to the lift"))
if num >= 0:
  s1= list[len-num:]
  s2= list[:len-num]
  print(s1+s2)
else:
 s3= list[(-len-num):]
 s4= list[:(-len-num)]
 print(s3+s4)