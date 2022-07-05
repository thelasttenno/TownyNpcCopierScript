import pickle
lastNPCInt = 0               
filename = 'NpcCount.pk'
with open(filename, 'rb') as fi:
    TotalNpcs = pickle.load(fi)
print(TotalNpcs)
input("Press Enter to continue...")