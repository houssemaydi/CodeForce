def point(p,t):
    if (p%250 == 0):
        score1 = 3*p/10
        score2 = p - p*t/250
        score=max(score1,score2)
        return score
    else:
        return False

def Convert(string): 
    li = list(string.split(" ")) 
    return li

scores = input()
List=Convert(scores)
List= list(map(int, List)) 
a = List[0]
b = List[1]
c = List[2]
d = List[3]
Misha = point(a,c)
Vasya = point(b,d)
if (a<=3500 and a>= 250 and b<=3500 and b>= 250 and c<=180 and c>= 0 and d<=180 and d>= 0):
    if (Misha>Vasya):
        print("Misha")
    elif (Misha<Vasya):
        print("Vasya")
    else:
        print("Tie")
