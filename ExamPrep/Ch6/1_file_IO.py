""" file = open('./ExamPrep/Content/text.txt','rt')

j = 1
for i in file :
    print(j ,':',i)
    j = j + 1 """


# f2 = open('./ExamPrep/Content/text.txt')
# print(f2.read(5))
# print(f2.readline())
# print(f2.readline())


f1 = open('./ExamPrep/Content/myFile.txt')
print(f1.name)
print(f1.mode)
print(f1.closed)
f1.close()
print(f1.closed)