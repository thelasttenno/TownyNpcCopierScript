import pickle
filename = 'NpcCount.pk'
lastNPCInt = 0               
with open(filename, 'wb') as fi:
# dump your data into the file
    pickle.dump(lastNPCInt, fi)