x = list(map(int, input("Enter: ").split()))
t = int(input("Enter: "))
k = 0
for i in range(len(x)):
    if x[i] != t:
        x[k] = x[i]
        k += 1
print(k)
print(x)