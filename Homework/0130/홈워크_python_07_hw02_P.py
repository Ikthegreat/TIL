def collatz(num):
    count = 0
    while True:
        if num == 1:
            return count
        elif num % 2 == 0:
            num = num // 2
            count += 1
        elif num % 2 == 1:
            num = (num * 3) + 1
            count += 1
        if count >= 500:
            return -1

print(collatz(6))  # => 8
print(collatz(16))  # => 4
print(collatz(27))  # => 111
print(collatz(626331))  # => -1