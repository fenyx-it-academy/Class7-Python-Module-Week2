def Common_Uncommon_Words(str1, str2):
    l1 = []
    l2 = []
    l3 = []
    for i in str1:
        if (i in str2):
            l1.append(i)
        elif (i not in str2):
            l2.append(i)
    for j in str2:
        if (j not in str1):
                    l3.append(j)
    return [''.join(l1)] + [''.join(l2)] + [''.join(l3)]


print(Common_Uncommon_Words('sharp', 'soap'))
              
        
    
    
    
