m = 0
x = 0

for a in range(100, 1000):
    for b in range(100, 1000):
        x = a * b
        if str(x) == str(x)[::-1]:
            if m < x:
                m = x

print(m)
