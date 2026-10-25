d = {'British Raj': 200, 'Mughal Empire': 350, 'DelhiSultanate': 100, 'Maurya Vansh': 150}


myD = dict(sorted(d.items(), key = lambda item : item[1]))

print(myD)
