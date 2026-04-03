from cia1 import generate_hash, august_encrypt, august_decrypt

def test_case(plaintext):
    print("\n----------------------------")
    print("Plaintext:", plaintext)

    # Step 1: Hash
    hashed_text = generate_hash(plaintext)
    print("Hash:", hashed_text)

    # Step 2: Encrypt
    cipher_text = august_encrypt(hashed_text)
    print("Cipher Text:", cipher_text)

    # Step 3: Decrypt
    decrypted_hash = august_decrypt(cipher_text)
    print("Decrypted Hash:", decrypted_hash)

    # Step 4: Verify
    if decrypted_hash == generate_hash(plaintext):
        print("Result: Data Integrity Verified")
    else:
        print("Result: Data Tampered")


# -------------------------------
# Multiple Test Cases
# -------------------------------
def main():
    test_case("hello")
    test_case("world")
    test_case("AugustCipher123")


if __name__ == "__main__":
    main()