class Solution:
    def countPrimes(self, n: int) -> int:
        # prime: divisible by 1 and itself
        # brute force: we check for every number < n if it can only be divided by itself
        # cnt = 0
        # for i in range(2, n):
        #     check = 0
        #     for j in range(2, n):
        #         if i % j == 0: 
        #             check += 1
        #     if check == 1:
        #         cnt += 1
        # return cnt

        # math logic: all numbers can be factorised into primes
        # it also follows that multiples of the prime are not prime 
        # if n <= 1:
        #     return 0
        # primes = [1] * n # [2, n-1]
        # primes[0] = primes[1] = 0
        # for i in range(2, n):
        #     j = i - 1
        #     # we just need to check if any of the previous prime is a factor 
        #     # of current number
        #     while j >= 2:
        #         if primes[j] == 1:
        #             if i % j == 0:
        #                 primes[i] = 0
        #                 for i in range(n):
        #         j -= 1 
        # return sum(primes)

        # further optimized
        if n <= 1:
            return 0
        primes = [1] * n # [2, n-1]
        primes[0] = primes[1] = 0
        
        for i in range(2, n):
            if primes[i] == 1:
                for j in range(i*i, n, i):
                    primes[j] = 0

        return sum(primes)
    
sol = Solution()
print(sol.countPrimes(32))