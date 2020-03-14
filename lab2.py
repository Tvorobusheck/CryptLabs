import mycryptutils as my


if __name__ == "__main__":
    cypher = my.ElgamalUser()
    print(cypher)

    m = int(input("Input m (lower than 1e5): "))
    if m >= int(1e5):
        raise Exception("Wrong input number")
    r, e = cypher.encrypt(m)
    print("Encrypted m is ", e)
    print("R is ", r)
    m_decrypted = cypher.decrypt(r, e)
    print("Decrypted e is ", m_decrypted)

