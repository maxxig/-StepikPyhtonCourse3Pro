import pickle

# data = ['a', 'b', 3, 4, 'f', 'g', 7, 8]
# data = {1:'1', 'ley':'1', 2:'2', 3:'3'}
data = ['a', 'b', 'f', 'g']


with open('data3.pkl', mode='wb') as file:
    pickle.dump(data, file)
