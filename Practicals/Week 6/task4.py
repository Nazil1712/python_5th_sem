d = {'British Raj': 200, 'Mughal Empire': 350, 'Delhi Sultanate': 100, 'Maurya Vansh': 150}

sorted_d = dict(sorted(d.items(), key=lambda item: item[1]))

for key, value in sorted_d.items():
    print(key, ":", value)
