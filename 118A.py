import re
message = input()
if (len(message)>0 and len(message)<101):
    regex = re.compile('[^a-zA-Z]')
    message = regex.sub('', message)
    message=message.lower()
    vowels = ('a', 'e', 'i', 'o', 'u','y');
    for x in message:
        if x in vowels:
            message = message.replace(x,"");
    l=[]
    for c in message:
        l.append(c)
    listToStr = '.'.join(map(str, l))
    listToStr = '.'+listToStr
    print(listToStr)
