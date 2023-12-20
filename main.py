import random
import pandas as pd


lst = ['robot'] * 10
lst += ['human'] * 10
# lst += ['zomby'] * 10
random.shuffle(lst)
columns = list(set(lst))
dict_lst = {'whoAmI': lst}
for line in lst:
    for column in columns:
        if column == line:
            key = 1
        else:
            key = 0
        dict_lst[column] = dict_lst.get(column, []) + [key]
data = pd.DataFrame(dict_lst)
data.head()
