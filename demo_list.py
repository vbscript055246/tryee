N = 20000000
sieve = []
for i in range(N):
    sieve.append(0)

prime = []


def linear_sieve():
    global prime
    for i in range(2, N):
        if not sieve[i]:
            prime.append(i)
        j = 0
        while (i*prime[j]) < N:
            sieve[i * prime[j]] = 1
            if i % prime[j] == 0:
                break
            j += 1


linear_sieve()

for item in prime:
    print(item)
