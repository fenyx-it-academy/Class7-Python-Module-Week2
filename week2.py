

###1.


list1 = [1, 2, 3, 4, 5]

print(list1[3:] + list1[0:3])


list2 = [1, 2, 3, 4, 5]
print(list2[-3:] + list2[-5:-3])



###2.


from collections import Counter

wordlist = "This is a sample text with several words This is more sample text with some different words".lower().split()

cnt = Counter()
for words in wordlist:
    cnt.update(set(words))

print(sorted(cnt.most_common()))



###3.
import string


input1 = set("sharp".lower())
input2 = set("soap".lower())


selected_word1 = list(input1)
selected_word2 = list(input2)
open_letter = list(input1 & input2)

a_word1 = sorted(selected_word1)
b_word2 = sorted(selected_word2)
c_open = sorted(open_letter)

com_a_word1 = "-".join(a_word1)
com_b_word2 = "-".join(b_word2)
com_c_string = "-".join(c_open)

x = []

x.append(com_a_word1)
x.append(com_b_word2)
x.append(com_c_string)
print(x)





###4


num1=int(input("Enter a number "))
num2=int(input("Enter a number "))
num3=int(input("Enter a number "))
list=[]
for a in range(1,num1*num2*num3):
    b=False
    for i in range(2,a):
        if a%i==0:
            b=False
            break
        else:
            b=True
    if b==True:
        list.append(a)
list1=[1]
for i in list:
    if str(i)==str(i)[::-1]:
        list1.append(i)
print(list1[-1])



