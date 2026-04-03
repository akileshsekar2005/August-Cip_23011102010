import hashlib


def generate_hash(plaintext):
    
    return hashlib.sha256(plaintext.encode()).hexdigest()



def august_encrypt(hashed_text):
    cipher_text = ""

    for ch in hashed_text:
        if ch.isalpha():
            if ch.islower():
                value = ord(ch) - ord('a')
                new_value = (value + 1) % 26
                new_char = chr(new_value + ord('a'))
            else:
                value = ord(ch) - ord('A')
                new_value = (value + 1) % 26
                new_char = chr(new_value + ord('A'))
        else:
            new_char = ch  

        cipher_text += new_char

    return cipher_text



def august_decrypt(cipher_text):
    decrypted_hash = ""

    for ch in cipher_text:
        if ch.isalpha():
            if ch.islower():
                value = ord(ch) - ord('a')
                new_value = (value - 1) % 26
                new_char = chr(new_value + ord('a'))
            else:
                value = ord(ch) - ord('A')
                new_value = (value - 1) % 26
                new_char = chr(new_value + ord('A'))
        else:
            new_char = ch

        decrypted_hash += new_char

    return decrypted_hash


def verify(plaintext, decrypted_hash):
    verify_hash = generate_hash(plaintext)

    if decrypted_hash == verify_hash:
        print("Data Integrity Verified")
    else:
        print("Data Tampered")



def main():
    print("----- AUGUST CIPHER WITH SHA-256 -----")

    plaintext = input("Enter plaintext: ")

    # Hashing
    hashed_text = generate_hash(plaintext)
    print("\nHashed Text:", hashed_text)

    # Encryption
    cipher_text = august_encrypt(hashed_text)
    print("Cipher Text:", cipher_text)

    # Decryption
    decrypted_hash = august_decrypt(cipher_text)
    print("Decrypted Hash:", decrypted_hash)

    # Verification
    verify(plaintext, decrypted_hash)



if __name__ == "__main__":
    main()