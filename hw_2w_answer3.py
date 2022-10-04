st1 = list(input("\nPlease put the first word: "))
st2 = list(input("\nPlease put the second word: "))

if " " in st1:
    st1.remove(" ")
elif " " in st2:
    st2.remove(" ")


st1 = set(st1)
st2 = set(st2)

my_set ={}

def mtw (st):
    my_set = sorted(st1.intersection(st2)) # asp

    nl= [' '] * 3

    print()

    for i in ((my_set)):
   
        nl[0] = nl[0] + i

    if nl[0] == " ":
        nl[0] = "No match"

    my_set = sorted(st1.difference(st2))  # hr

    for i in ((my_set)):
    
        nl[1] = nl[1] + i

    if nl[1] == " ":
        nl[1] = "No match"

    my_set = sorted(st2.difference(st1))

    for i in ((my_set)):
    
        nl[2] = nl[2] + i

    if nl[2] == " ":
        nl[2] = "No match"

    print(nl, '\n')

mtw(my_set)