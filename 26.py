x = list(map(int, input("Enter: ").split()))
l = []
k = 1
for i in range(1,len(x)):
    if x[i] != x[k-1]:
        x[k] = x[i]
        k += 1
print(k)