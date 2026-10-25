import pandas as pd

data = { 
    "apples" : [1,2,3,4],
    "oranges" : [5,6,7,8]
}
ans = pd.DataFrame(data)
# print(ans)


purchase = pd.DataFrame(data,index=[10,11,12,13])
# print(purchase)
print(purchase.loc[0.1])