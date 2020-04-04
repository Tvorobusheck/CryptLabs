import mycryptutils as my


if __name__ == "__main__":

    m = int(input("Введите m: "))
    cypher = my.ElgamalUser(m + 1)
    print(cypher)
    r, e = cypher.encrypt(m)
    print("Зашифрованное m = ", e)
    print("R is ", r)
    m_decrypted = cypher.decrypt(r, e)
    print("Расшифрованное e = ", m_decrypted)

