import pickle

with open('../readers/read_script.pickle', "rb") as file:
    inputs = pickle.load(file)

for i in inputs:
    i()