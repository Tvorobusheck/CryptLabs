import mycryptutils as my


if __name__ == "__main__":
    cypher = my.RSAUser()
    print(cypher)

    m = int(input("Input m (lower than 1e5): "))
    if m >= int(1e5):
        raise Exception("Wrong input number")
    e = cypher.encrypt(m)
    print("Encrypted m is ", e)
    m_decrypted = cypher.decrypt(e)
    print("Decrypted e is ", m_decrypted)

