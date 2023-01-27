import random
import os

len_k = 300
num_keys = 100
total = len_k * num_keys

with open('rl.txt', 'w') as f:
    for i in range(0, total):
        myint = random.randint(0, 1)
        f.write(str(myint))

os.system(f"./assess {total} < rcommands.txt")
os.system(f"cp experiments/AlgorithmTesting/finalAnalysisReport.txt rresults.txt")


