class Solution(object):

    def nthSuperUglyNumber(self, n, primes):
        candidate = [1] * len(primes)
        superUgly = [1]
        pIndex = [0] * len(primes)

        nextMinNumber = 1
        for i in range(1, n):
            for j in range(len(primes)):
                if nextMinNumber == candidate[j]:
                    candidate[j] = primes[j] * superUgly[pIndex[j]]
                    pIndex[j] += 1
            nextMinNumber = min(candidate)
            superUgly.append(nextMinNumber)

        return superUgly[-1]
