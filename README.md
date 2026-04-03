# Crypto_CIA
# August Cipher with SHA-256 Hashing

## Overview
This project implements a hybrid cryptographic approach combining:

- **SHA-256 Hashing** → for data integrity  
- **August Cipher (Shift = 1)** → for simple encryption  

The system ensures that the data is **securely transformed** and later **verified for integrity**.

---

##  Workflow
Plaintext → SHA-256 Hash → August Cipher → Cipher Text
↓
Reverse Cipher
↓
Compare Hash Values


---

##  Algorithm

### Step 1: Start

---

### Step 2: Input
- Read plaintext from the user

---

### Step 3: Convert to Byte Format
- Convert plaintext into byte format for hashing

---

### Step 4: SHA-256 Hashing
- Apply SHA-256 hashing on the input:
  - Perform padding
  - Split into 512-bit blocks
  - Execute 64 compression rounds
  - Use bitwise operations and modular arithmetic
- Convert output into hexadecimal string
- Store as `hashed_text`

---

### Step 5: August Cipher Encryption (Shift = 1)
- Initialize `cipher_text = ""`
- For each character in `hashed_text`:
  - If lowercase:
    ```
    value = ord(ch) - ord('a')
    new_value = (value + 1) % 26
    new_char = chr(new_value + ord('a'))
    ```
  - If uppercase:
    ```
    value = ord(ch) - ord('A')
    new_value = (value + 1) % 26
    new_char = chr(new_value + ord('A'))
    ```
  - If digit:
    - Keep unchanged
- Append each character to `cipher_text`
- Output the encrypted text

---

### Step 6: Decryption (Reverse August Cipher)
- Initialize `decrypted_hash = ""`
- For each character in `cipher_text`:
  - If alphabet:
    ```
    new_value = (value - 1) % 26
    ```
  - If digit:
    - Keep unchanged
- Reconstruct original hash

---

### Step 7: Verification
- Recompute SHA-256 hash of original plaintext
- Compare:
- if decrypted_hash == recomputed_hash:
Data Integrity Verified
else:
Data Tampered


---

##  Worked Examples

###  Example 1

**Input:**
Plaintext: hello

**Output:**
Hash: 2cf24dba5fb0a30e...
Cipher Text: 2dg35ecb5gc0b41f...
Decrypted Hash: 2cf24dba5fb0a30e...
Verification: Data Integrity Verified


---


---

##  Round-Trip Verification

This project demonstrates:
Encrypt → Hash → Decrypt → Compare
---

### Step 8: End

---

##  Features

- ✅ Combines hashing and encryption  
- ✅ Ensures data integrity  
- ✅ Demonstrates classical + modern cryptography  
- ✅ Easy to understand and implement  

---

##  Limitations

- August Cipher is **not secure for real-world encryption**
- SHA-256 is **one-way (cannot recover plaintext)**
- Designed for **educational purposes only**

##  Concepts Used

- Cryptographic Hash Functions (SHA-256)
- Caesar Cipher (Shift-based encryption)
- ASCII Manipulation
- Modular Arithmetic

---

##  Author
Akilesh S - 23011102010
