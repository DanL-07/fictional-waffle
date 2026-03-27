class Fibonacci:
    """Class for calculating Fibonacci sequence"""

    def nth_term(self, N):
        """Return the N-th Fibonacci number"""
        a, b = 0, 1
        for _ in range(N + 1):
            a, b = b, a + b
        return a

    def divisible_by_m(self, N, M):
            # Get the N-th Fibonacci value as the upper limit
        limit = self.nth_term(N)

        fibnum = []
        a, b = 0, 1

        for _ in range(N + 1):
            if a % M == 0:
                fibnum.append(a)

            a, b = b, a + b

            # stop early if we exceed the N-th term value
            if a >= limit:
                break

        return fibnum


# ---------------- TEST ----------------
fib = Fibonacci()

N = 100
M = 7

print("N-th Fibonacci term:", fib.nth_term(N))
print("Fibonacci numbers <= N-th term divisible by M:", fib.divisible_by_m(N, M))



