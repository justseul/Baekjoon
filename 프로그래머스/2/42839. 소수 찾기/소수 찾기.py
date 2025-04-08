import itertools

# 소수 판별 함수
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1): 
        if n % i == 0:
            return False
    return True

def solution(numbers):
    n = list(numbers)
    nums = set() 

    for i in range(1, len(n) + 1):
        for p in itertools.permutations(n, i):
            num = int("".join(p))
            nums.add(num)

    primes = [x for x in nums if is_prime(x)]
    return len(primes)