lst = input()

l = [1, 2, 3, 4, 5]
def rotate(l, n):
    return l[-n:] + l[:-n]

print(rotate(l, -2))
print(rotate(l, 2))