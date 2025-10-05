def next_prime(n):
    def is_prime(k):
        if k < 2:
            return False
        for i in range(2, k):
            if k % i == 0:
                return False
        return True

    x = n + 1
    while True:
        if is_prime(x):
            return x
        x += 1

# complex
print(next_prime(25))