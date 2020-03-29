import mycryptutils as my


if __name__ == "__main__":
    cypher = my.ElgamalUser()
    print(cypher)

    m = int(input("Введите m: "))
    r, e = cypher.encrypt(m)
    print("Зашифрованное m = ", e)
    print("R is ", r)
    m_decrypted = cypher.decrypt(r, e)
    print("Расшифрованное e = ", m_decrypted)

