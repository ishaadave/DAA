class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        MOD = 1337

        def power(x, n):
            if n == 0:
                return 1

            half = power(x, n // 2)

            if n % 2 == 0:
                return (half * half) % MOD
            else:
                return (half * half * x) % MOD

        if not b:
            return 1

        last = b.pop()

        return (power(self.superPow(a, b), 10) * power(a, last)) % MOD      