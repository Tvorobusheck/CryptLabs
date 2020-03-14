import random
import primes


def fast_pow(num: int, degree: int, mod: object = None) -> int:
    if degree < 0 or mod is not None and mod < 0:
        raise Exception("Negative number")
    elif degree == 0:
        return 1
    else:
        m = degree & 1
        degree >>= 1
        next_val = fast_pow(num, degree, mod)
        if mod is not None:
            if m == 1:
                return (num * next_val * next_val) % mod
            else:
                return (next_val * next_val) % mod
        else:
            if m == 1:
                return num * next_val * next_val
            else:
                return next_val * next_val


def gcd(a: int, b: int) -> int:
    if a < b:
        t = a
        a = b
        b = t
    if b == 0:
        return a
    else:
        return gcd(a % b, b)


def calc_primes(n: int) -> None:
    primes_filename = "primes.py"

    is_prime = [i >= 2 for i in range(n)]
    primes = []
    for i in range(2, n):
        if is_prime[i]:
            j = 2
            while i * j < n:
                is_prime[i * j] = False
                j += 1
            primes.append(i)

    with open(primes_filename, "w") as primes_out:
        primes_out.write("primes = " + str(primes))


def gcdex(a: int, b: int, x: int, y: int) -> int:
    if a == 0:
        x = 0
        y = 1
        return b, x, y
    d, x1, y1 = gcdex(b % a, a, 0, 0)
    x = y1 - (b // a) * x1
    y = x1
    return d, x, y


def find_multi_inversion(num: int, mod: int) -> int:
    d, x, y = gcdex(num, mod, 0, 0)
    return (x % mod + mod) % mod


class RSAUser:

    def __init__(self, name="User"):
        self.name = name
        self.p = random.choice([num for num in primes.primes])
        self.q = random.choice([num for num in primes.primes if int(1e5) < num * self.p])
        # print(self.p, self.q)
        self.n = self.p * self.q  # e < n
        self.f = (self.p - 1) * (self.q - 1)
        self.d = 0
        for a in range(1000, self.f):
            if gcd(a, self.f) == 1:
                self.d = a
                break
        self.c = find_multi_inversion(self.d, self.f)   # f != n, to find c you must get f, which means to get all
                                                        # prime multipliers of n (big number)

    # encrypt by open keys d and n
    def encrypt(self, m: int) -> int:
        return fast_pow(m, self.d, self.n)

    # decrypt by secret key c
    def decrypt(self, e: int) -> int:
        return fast_pow(e, self.c, self.n)

    def __repr__(self):
        return "Public key: d={0}, n={2}\nPrivate key: c={1}, n={2}".format(self.d, self.c, self.n)


class ElgamalUser:

    def __init__(self):
        prime = [num for num in primes.primes if num >= int(1e5)]

        self.p = random.choice(prime)
        q = (self.p - 1) // 2
        for g in [num for num in primes.primes if 1 < num < self.p - 1]:
            if fast_pow(g, q, self.p) != 1:
                self.g = g
                break
        self.c = random.randrange(2, self.p - 1)
        self.d = fast_pow(self.g, self.c, self.p)

    def encrypt(self, m: int) -> int:
        k = random.randrange(1, self.p - 1)
        r = fast_pow(self.g, k, self.p)
        e = (m * fast_pow(self.d, k, self.p)) % self.p
        return r, e

    def decrypt(self, r: int, e: int) -> int:
        m = (e * fast_pow(r, self.p - 1 - self.c, self.p)) % self.p
        return m

    def __repr__(self):
        return str("Public key: p={}, g={}, d={}\n".format(self.p, self.g, self.d)) +\
                str("Secret key: c = {}".format(self.c))