import re
message = input()
regex = re.compile('[^a-zA-Z]')
message = regex.sub('', message)
#print(message) regex.sub('', message) fasakh ay haja differente de [^a-zA-Z]
nbupper = sum(1 for c in message if c.isupper())
nblower = sum(1 for c in message if c.islower())
#print(nbupper)
#print(nblower)
if (nbupper>nblower):
    print(message.upper())
else:
    print(message.lower())
