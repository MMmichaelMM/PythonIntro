import pandas as pd

# # Calling DataFrame constructor
# df = pd.DataFrame()
# print(df)

# # list of strings
# lst = ['Python', 'Pandas', 'Intro', 'NumPy',
#        'Java', 'C++', 'Git Hub']

# # Calling DataFrame constructor on list
# df = pd.DataFrame(lst)
# print(df)

d = {'col1': [1, 2], 'col2': [3, 4]}
df = pd.DataFrame(data=d)
print(df)