import pickle

dic = {'fruit': ['apple', 'orange'], 'price': [50, 60]}

# with open(file_name,'rb') > autoClose
# 'wb' write binary
file = open('pickle.txt', 'wb')
pickle.dump(dic, file)
file.close()

# autoClose -> with ...
# 'rb' read binary
with open('pickle.txt', 'rb') as file:
    a_dic = pickle.load(file)

print(a_dic)
