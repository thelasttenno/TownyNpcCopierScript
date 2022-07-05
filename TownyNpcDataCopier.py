import os
import pickle
# open a pickle file
filename = 'NpcCount.pk'
with open(filename, 'rb') as fi:
    TotalNpcs = pickle.load(fi)

lastNPC = input("Total Npc Count: ")
lastNPCInt = []
try:
    e = int(lastNPC)
    lastNPCInt.append(e)
except:
    lastNPCInt.append(int(TotalNpcs))

limit = lastNPCInt[0] + int(input("Total Npc wanted: "))
town = input("TownName: ")

run_limit = limit
# Parent Directory pat
parent_dir = input(
    "Enter your path eg. ~/server/plugins/Towny/data/residents : ") or "data/"
path = os.path.join(parent_dir, town)

try:
    os.mkdir(path)
    print("Directory creation successful")
    input("Press Enter to continue...")
    try:
        while lastNPCInt[0] < run_limit + 1:
            if lastNPCInt[0] < 9:
                stuff_in_string = 'data/{}/NPC{}.txt'.format(
                    town, lastNPCInt[0])
                string2 = 'uuid=f6cf4f4f-efb1-4ad9-aa19-cc3ca4d8263{}\nlastOnline=0\nregistered=1657023229647\njoinedTownAt=1657023229647\nisNPC=true\ntitle=\nsurname=\ntown={}\ntown-ranks=\nnation-ranks=\nfriends=\nprotectionStatus=residentBuild,residentDestroy,residentSwitch,residentItemUse\nmetadata=\n'.format(
                    lastNPCInt[0], town)
                with open(stuff_in_string, 'w') as f:
                    f.write(string2)
                    print(string2)
            if lastNPCInt[0] > 9:
                stuff_in_string = 'data/{}/NPC{}.txt'.format(
                    town, lastNPCInt[0])
                string3 = 'uuid=f6cf4f4f-efb1-4ad9-aa19-cc3ca4d826{}\nlastOnline=0\nregistered=1657023229647\njoinedTownAt=1657023229647\nisNPC=true\ntitle=\nsurname=\ntown={}\ntown-ranks=\nnation-ranks=\nfriends=\nprotectionStatus=residentBuild,residentDestroy,residentSwitch,residentItemUse\nmetadata=\n'.format(
                    lastNPCInt[0], town)
                with open(stuff_in_string, 'w') as f:
                    f.write(string3)
            if lastNPCInt[0] > 99:
                stuff_in_string = 'data/{}/NPC{}.txt'.format(
                    town, lastNPCInt[0])
                string4 = 'uuid=f6cf4f4f-efb1-4ad9-aa19-cc3ca4d82{}\nlastOnline=0\nregistered=1657023229647\njoinedTownAt=1657023229647\nisNPC=true\ntitle=\nsurname=\ntown={}\ntown-ranks=\nnation-ranks=\nfriends=\nprotectionStatus=residentBuild,residentDestroy,residentSwitch,residentItemUse\nmetadata=\n'.format(
                    lastNPCInt[0], town)
                with open(stuff_in_string, 'w') as f:
                    f.write(string4)
            if lastNPCInt[0] == limit:
                with open(filename, 'wb') as fi:
                    # dump your data into the file
                    pickle.dump(lastNPCInt[0], fi)
                print("thanks for using TennoGen Towny Npc Creator")
                input("Press Enter to continue...")
                break
            print(lastNPCInt[0])
            lastNPCInt[0] += 1
    except OSError as error:
        print(error)
        print("creation failed")
        input("Press Enter to continue...")
except OSError as error:
    print(error)
    print("Directory creation failed")
    input("Press Enter to continue...")
    try:
        while lastNPCInt[0] < run_limit + 1:
            if lastNPCInt[0] < 9:
                stuff_in_string = 'data/{}/NPC{}.txt'.format(
                    town, lastNPCInt[0])
                string2 = 'uuid=f6cf4f4f-efb1-4ad9-aa19-cc3ca4d8263{}\nlastOnline=0\nregistered=1657023229647\njoinedTownAt=1657023229647\nisNPC=true\ntitle=\nsurname=\ntown={}\ntown-ranks=\nnation-ranks=\nfriends=\nprotectionStatus=residentBuild,residentDestroy,residentSwitch,residentItemUse\nmetadata=\n'.format(
                    lastNPCInt[0], town)
                with open(stuff_in_string, 'w') as f:
                    f.write(string2)
                    print(string2)
            if lastNPCInt[0] > 9:
                stuff_in_string = 'data/{}/NPC{}.txt'.format(
                    town, lastNPCInt[0])
                string3 = 'uuid=f6cf4f4f-efb1-4ad9-aa19-cc3ca4d826{}\nlastOnline=0\nregistered=1657023229647\njoinedTownAt=1657023229647\nisNPC=true\ntitle=\nsurname=\ntown={}\ntown-ranks=\nnation-ranks=\nfriends=\nprotectionStatus=residentBuild,residentDestroy,residentSwitch,residentItemUse\nmetadata=\n'.format(
                    lastNPCInt[0], town)
                with open(stuff_in_string, 'w') as f:
                    f.write(string3)
            if lastNPCInt[0] > 99:
                stuff_in_string = 'data/{}/NPC{}.txt'.format(
                    town, lastNPCInt[0])
                string4 = 'uuid=f6cf4f4f-efb1-4ad9-aa19-cc3ca4d82{}\nlastOnline=0\nregistered=1657023229647\njoinedTownAt=1657023229647\nisNPC=true\ntitle=\nsurname=\ntown={}\ntown-ranks=\nnation-ranks=\nfriends=\nprotectionStatus=residentBuild,residentDestroy,residentSwitch,residentItemUse\nmetadata=\n'.format(
                    lastNPCInt[0], town)
                with open(stuff_in_string, 'w') as f:
                    f.write(string4)
            if lastNPCInt[0] == limit:
                with open(filename, 'wb') as fi:
                    # dump your data into the file
                    pickle.dump(lastNPCInt[0], fi)
                print("thanks for using TennoGen Towny Npc Creator")
                input("Press Enter to continue...")
                break
            print(lastNPCInt[0])
            lastNPCInt[0] += 1
    except OSError as error:
        print(error)
        print("creation failed")
        input("Press Enter to continue...")
