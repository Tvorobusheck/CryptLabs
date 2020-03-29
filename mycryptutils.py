import random
# import primes


# быстрое возведение в степень
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


# поиск НОД
def gcd(a: int, b: int) -> int:
    if a < b:
        t = a
        a = b
        b = t
    if b == 0:
        return a
    else:
        return gcd(a % b, b)


# расчет простых чисел
def is_prime(n: int, r: int = 50):
    if n < 1000:
        raise Exception("Too small number for Miller-Rabin test")
    s = 0
    d = n - 1
    while d % 2 == 0:
        d >>= 1
        s += 1
    assert (2 ** s * d == n - 1)

    def trial_composite(a):
        if fast_pow(a, d, n) == 1:
            return False
        for i in range(s):
            if fast_pow(a, 2 ** i * d, n) == n - 1:
                return False
        return True

    for i in range(r):
        a = random.randrange(2, n)
        if trial_composite(a):
            return False

    return True


# расширенный алгоритм Евклида
def gcdex(a: int, b: int, x: int, y: int) -> (int, int, int):
    if a == 0:
        x = 0
        y = 1
        return b, x, y
    d, x1, y1 = gcdex(b % a, a, 0, 0)
    x = y1 - (b // a) * x1
    y = x1
    return d, x, y


# поиск обратного по модулю
def find_multi_inversion(num: int, mod: int) -> int:
    d, x, y = gcdex(num, mod, 0, 0)
    return (x % mod + mod) % mod


class RSAUser:

    def __init__(self, name="User"):
        self.name = name
        for i in range(random.randint(int(1e5), int(1e8)), int(1e9)):
            if is_prime(i):
                self.p = i
                break
        for i in range(self.p + 1, int(1e9)):
            if is_prime(i):
                self.q = i
                break
        # self.p = 5119
        # self.q = 5659
        # print(self.p, self.q)
        self.n = self.p * self.q  # e < n
        self.f = (self.p - 1) * (self.q - 1)
        self.d = 0
        for a in range(1000, self.f):
            if gcd(a, self.f) == 1:
                self.d = a
                break
        if self.d == 0:
            raise Exception("D = 0")
        self.c = find_multi_inversion(self.d, self.f)

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

        for i in range(random.randint(int(1e5), int(1e8)), int(1e9)):
            if is_prime(i):
                self.p = i
                break

        q = (self.p - 1) // 2
        for g in range(2 + 1000, self.p - 1):
            if not is_prime(g):
                continue
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