fib1 = fib2 = 1 # первое и второе число фибоначи

fib_sum = 0
while fib2 < 4000000:
    fib1, fib2 = fib2, fib1 + fib2
    if fib2 % 2 == 0:
        fib_sum += fib2

print(fib_sum)
