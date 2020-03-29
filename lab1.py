import mycryptutils as my


if __name__ == "__main__":
    cypher = my.RSAUser()
    print(cypher)

    m = int(input("Введите m:"))
    e = cypher.encrypt(m)
    print("Зашифрованное m = ", e)
    m_decrypted = cypher.decrypt(e)
    print("Расшифрованное e = ", m_decrypted)
    #
    # my.calc_primes(int(1e3))