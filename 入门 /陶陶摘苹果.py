#using PyPy3
#P1046
a = list(map(int, input().split()))
h = int(input())
max_reach = h + 30
b = 0

for i in range(10):
    if a[i] <= max_reach:
        b += 1
print(b)
