import pickle

data = {'name': 'Alice', 'age': 25}

with open('data.pkl','wb') as file:
     pickle.dump(data,file)

 # Unpickling
with open('data.pkl', 'rb') as file:
     loaded_data = pickle.load(file)

 print(loaded_data)