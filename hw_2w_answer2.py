dicc = {}
def prt_lttr (txt):
    for lttr in txt:
     if lttr == " ":
         vc = lttr
     elif lttr =="," or lttr =="'" or lttr == '"' or lttr =="." or lttr ==";" or lttr =='@' :
        vc = lttr
     elif lttr in dicc:
         dicc[lttr]= dicc [lttr]+1
     else:
         dicc[lttr]=1
    print(f"({dicc})")
prt_lttr(input("Please, put the phrase : ").lower())