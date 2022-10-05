# Class7-Python-Module-Week2

### 1.
Write a program that takes two inputs; one of them is a list and the other is a number, and returns the list obtained by shifting the elements in the list n places to the right (left) when n is positive (negative). Use wrap-around: if an element is shifted beyond the end of the list, then continue to shift starting at the beginning of the list.

```
Example
Inputs>>> [1, 2, 3, 4, 5], 2
Output>>> [4, 5, 1, 2, 3]
Inputs>>> [1, 2, 3, 4, 5], -2
Output>>> [3, 4, 5, 1, 2]
### solution 1
def rightRotate(lists, num):
    output_list = []
 
    
    for item in range(len(lists) - num, len(lists)):
        output_list.append(lists[item])
 
    
    for item in range(0, len(lists) - num):
        output_list.append(lists[item])
 
    print(output_list)
 
 
def list_input():
    rotate_num=int(input('enter ther rotate number'))
    

    y=[]
    while True:
        x=(input('enter the elements of the list and entery y to exist the litst'))
        if x=='y':
          break
        else:
            y.append(int(x))
          
          
    rightRotate(y, rotate_num)     
list_input()


### 2.
Write a code snippet that inputs a sentence from the user, then uses a dictionary to summarize the number of occurrences of each letter. Ignore case, ignore blanks and assume the user does not enter any punctuation. Display a two-column table of the letters and their counts with the letters in sorted order.

```
Example
Input >>> "This is a sample text with several words This is more sample text with some different words"
Output >>>
[('a', 4), ('d', 3), ('e', 10), ('f', 2), ('h', 4), ('i', 7), ('l', 3), ('m', 4), ('n', 1), ('o', 4), ('p', 2), ('r', 5), ('s', 10), ('t', 9), ('v', 1), ('w', 4), ('x', 2)]

### solution 2
def count_starts():
    text=str(input('enter the text'))
    new_list=[]
    for word in range(len(text)):
        for letter in text[word]:
            if letter[0]=='':
                new_list.append(None)
            else:
                new_list.append(letter[0])
            
    new_dict= {x:new_list.count(x) for x in new_list}


    print (new_dict)
count_starts()



### 3.
Write a program that takes in two words as input and returns a list containing three elements, in the following order:
-		Shared letters between two words.
 	
-		Letters unique to word 1.
 	
-		Letters unique to word 2.

Each element of the output should have unique letters, and should be alphabetically sorted. Use set operations. The strings will always be in lowercase and will not contain any punctuation.

```
Example
Input1>>> "sharp"
Input2>>> "soap"
Output>>> ['aps', 'hr', 'o']
#### solution 3

def fun():
    
    l1=[]
    l2=[]
    str1=''
    str2=str(input('enter the first word'))
    str3=str(input('enter the second word'))
    l1[:]=str2
    l2[:]=str3
    set1=set(l1)
    set2=set(l2)
    t1=set1&set2
    t11=list(t1)
    t11.sort
    t2=set1-set2
    t21=list(t2)
    t21.sort()
    t3=set2-set1
    t31=list(t3)
    t31.sort()
    for i in [t11,t21,t31]:
        for j in i:
            j+=str1
            
            print(j,end='')
        print()
        
fun()



### 4.
A palindromical prime number is a prime number that reads the same when reversed. 
Write a function which returns the nearest palindromical prime number less than the multiplication of all the arguments.

```
Example
Input1>>>  some_function(2, 3, 4) 
Output1>>>  the nearest palindromical prime number less than 24
Input2>>> some_function(31, 77, 99)
Output2>>> the nearest palindromical prime number less than 236,313
### solution 4
def rome(x,y,w):
    m=x*w*y
    set1=[]
    set2=[]
    for i in range(2,m):
        set1.append(i)
    #print(set1)
    for i in set1:    
        rev=int(str(i)[::-1])
        if rev==i:
           set2.append(i)
        #print(set2)
        z=len(set2)
        #print(z)
        #print(set2[z-1])  
 
    set=[]
    for num in set2:
        if num > 1:
   
            for i in range(2, int(num/2)+1):
       
                if (num % i) == 0:
                    pass
                    break
            else:
                set.append(num)
                print(set)
        else:
            pass
    z=len(set)
    print(set[z-1])
def rome2():
    x=int(input('enter the first arguemnt '))
    y=int(input('enter the second arguemnt '))
    w=int(input('enter the third arguemnt '))
    rome(x,y,w)
   
rome2()
