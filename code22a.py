def Convert(string): 
    li = list(string.split(" ")) 
    return li

val = input()
val = int(val)
List= input()
List=Convert(List)
List= list(map(int, List)) 
if (val>=1 and val<=100):
    if (len(List)==1):
        print("NO")
    elif (len(List)==val):
        List = list(dict.fromkeys(List))
        List.sort()
        if (len(List)==1):
            print("NO")
        elif(abs(int(List[0]))>=0 and abs(int(List[len(List)-1]))<=100):
            print(List[1])
        else:
            print("NO")


else:
    print("NO")

