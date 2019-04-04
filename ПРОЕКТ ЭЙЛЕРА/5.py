n = y = 1

x = 20

while y <= x:
    if n % y == 0:
        y += 1
    else:
        n += 1
        y = 1

print (n)
