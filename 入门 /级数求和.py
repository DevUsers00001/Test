#using PyPy3
#P1035
n = int(input())
ans = 0.0
i = 1
while ans <= n:
    ans += 1.0 / i
    i += 1
print(i - 1)
