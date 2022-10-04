fn = int(input('Please, put the first  number: '))
sn = int(input('Please, put the second number: '))
tn = int(input('Please, put the third  number: '))

n = (fn * sn * tn)

def palin_ant (n):
    for i in range(n-1, 0, -1):
        if str(i) == str(i)[::-1]:
            print(i)
            return(i)

palin_ant(n)