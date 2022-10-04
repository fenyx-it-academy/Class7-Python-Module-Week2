def rt (l, d, n):
    if d > 0:
        k = l.index(d)
        nl = []
        nl = l[k+d:]+l[0:k+d]
        return nl
    else:
        d = d *-1
        k = l.index(d)
        nl = []
        nl = l[k+1:]+l[0:k+1]
        return nl

ltn=[]
print()
vl=int(input("Please put the number (0 to finish) :"))

while vl!=00:
    ltn.append(vl)
    vl=int(input("Please put the number (0 to finish) :"))

sz = len(ltn)

print('\n', ltn, '\n')

print("The list size is: ", sz)

d = int(input(f"\nPlease put shift number smaller than {sz} : "))

print('\n',rt(ltn, d, sz), '\n')
