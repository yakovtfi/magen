import time
q = 100000
start = time.time()
for _ in range(q):pass
print("O(n):", round(time.time() - start, 5), "seconds")
start = time.time()
for _ in range(q):
 for _ in range(q):pass
print("O(n²):", round(time.time() - start, 5), "seconds")