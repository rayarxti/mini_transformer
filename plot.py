import matplotlib.pyplot as plt
import numpy as np

iter = []
loss = []

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

with open('train_results.txt', 'r') as f:
    while (s := f.readline()) != '':
        if s[:4] == 'iter':
            numbers = list(filter(is_number, s.split()))
            numbers = [float(x) if '.' in x else int(x) for x in numbers]
            iter.append(numbers[0])
            loss.append(numbers[1])

plt.plot(iter, loss)
plt.title('Training loss curve')
plt.xlabel('# Iterations')
plt.ylabel('Loss')
plt.show()