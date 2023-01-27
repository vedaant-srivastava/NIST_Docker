import random
import os

len_kf = 10000 #length of the keyframe
len_k = 256 #length of each key
num_keys = 100 #total number of keys
total = len_k * num_keys
keyframe = []
keys = []

for i in range(0, len_kf):
    myint = random.randint(0, 1)
    keyframe.append(myint)

#print(f'{keyframe = }')

pos = [i for i in range(0, len_kf)]
jumps = [i for i in range(0, len_kf)]

#print(f'{pos = }')
#print(f'{jumps = }')

for i in range(1, num_keys+1):
    kpos = random.choice(pos)
    kjump = random.choice(jumps)

    key = [[]]
    cur_pos = kpos
    for j in range(0, len_k):
        key[0].append(cur_pos)
        cur_pos = (cur_pos + kjump) % len_kf
    key.append(kpos)
    key.append(kjump)

    keys.append(key)
    #print(f'{key = }')

#print(f'{keys = }')

with open('kl.txt', 'w') as f:
    for k in keys:
        for bit in k[0]:
            f.write(str(keyframe[bit]))

print(f'file length = {total}')

os.system(f"./assess {total} < kcommands.txt")
os.system(f"cp experiments/AlgorithmTesting/finalAnalysisReport.txt kresults.txt")
