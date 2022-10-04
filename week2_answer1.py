def shift(lis, n):
    
    if 0<n<len(lis):
        return lis[-1 * n:] + lis[:len(lis) - n]
    elif -1>n> -1 * len(lis):
        return lis[len(lis) + n - 1:] + lis[:n - 1]
    else:
        return lis

print(shift([1, 2, 3, 4, 5], -5))