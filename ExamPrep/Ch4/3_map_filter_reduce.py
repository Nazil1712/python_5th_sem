mylist = 1,2,3,4,5,6,7

# Filter
ans = filter(lambda element : element%2==0,mylist)
print(list(ans))

# Map
ans2 = map(lambda element : element*element ,mylist)
print(tuple(ans2))

# Reduce
from functools import reduce
ans3 = reduce(lambda x,y : x + y, mylist)
print(ans3)