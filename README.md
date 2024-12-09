# RSA Decryption Script

This project implements the RSA decryption algorithm, enabling decryption of ciphertext using a private key. It serves as a practical demonstration of public-key cryptography principles, including modular arithmetic and efficient decryption techniques.

---

## Overview

The script utilizes the RSA decryption formula:  
\[
\text{Plaintext} = \text{Ciphertext}^d \mod n
\]  
Where:  
- **Ciphertext** (\( C \)): The encrypted message in integer format.  
- **Private Key** (\( d \)): The decryption exponent.  
- **Modulus** (\( n \)): The product of two large prime numbers.  

The decryption process is optimized using modular exponentiation, ensuring computational efficiency.

---

## Features

- Implements **modular exponentiation** for efficiency.  
- Demonstrates **core RSA decryption principles**.  
- Accepts **interactive user input** for ciphertext, private key, and modulus.  
- Designed with **modularity** for clarity and future enhancements.  

---

## How It Works

### Inputs
The script prompts the user to provide:  
1. **Ciphertext**: The encrypted message as an integer.  
2. **Private Key** (\( d \)): The key used for decryption.  
3. **Modulus** (\( n \)): Derived from the product of two large prime numbers.  

### Decryption
The script calculates:  
\[
\text{Plaintext} = \text{Ciphertext}^d \mod n
\]  
This involves:  
- **Exponentiation**: Raising the ciphertext to the power of the private key.  
- **Modular Reduction**: Computing the result modulo \( n \).


## Key Concepts

- **Encryption**:  
  The ciphertext \( C \) is calculated using the message \( M \), the public exponent \( e \), and the modulus \( n \):
  \[
  C = M^e \mod n
  \]
  where:
  - **C** = Ciphertext (encrypted message)
  - **M** = Message (plaintext)
  - **e** = Public key exponent
  - **n** = Modulus

- **Decryption**:  
  The plaintext \( M \) is recovered from the ciphertext \( C \) using the private key \( d \) and the modulus \( n \):
  \[
  M = C^d \mod n
  \]
  where:
  - **M** = Message (plaintext)
  - **C** = Ciphertext
  - **d** = Private exponent
  - **n** = Modulus

---

## Key Components

- **Public Key**: \( (e, n) \)
- **Private Key**: \( (d, n) \)
- **n**: The modulus, which is the product of two large prime numbers, \( p \) and \( q \).
- **p** and **q**: Two prime numbers used to calculate the modulus \( n \).
- **Q(n)** (Euler's Totient): The totient of \( n \), calculated as \( Q(n) = (p-1) \times (q-1) \).
- **e**: The public exponent used for encryption.
- **d**: The private exponent used for decryption, calculated as the modular inverse of \( e \) modulo \( Q(n) \).
- **m**: The plaintext message.

---

## Steps to Decrypt

1. **Find the factors of \( n \)** to get \( p \) and \( q \). This can be done using an online tool such as [factordb.com](https://factordb.com).
2. **Calculate \( Q(n) \)** using \( p \) and \( q \):
   \[
   Q(n) = (p-1) \times (q-1)
   \]
3. **Calculate the private exponent \( d \)** using the modular inverse of \( e \) modulo \( Q(n) \):
   \[
   d = e^{-1} \mod Q(n)
   \]
4. **Decrypt the ciphertext** \( c \) using the formula:
   \[
   m = c^d \mod n
   \]
   where \( m \) is the decrypted plaintext.

--- 

## Summary of the Formulae

- **Encryption**:
  \[
  C = M^e \mod n
  \]
- **Decryption**:
  \[
  M = C^d \mod n
  \]
- **Calculating \( Q(n) \)**:
  \[
  Q(n) = (p-1) \times (q-1)
  \]
- **Private Key Calculation**:
  \[
  d = e^{-1} \mod Q(n)
  \]
- **Decrypting the Message**:
  \[
  m = c^d \mod n
  \]

--- 

### Output
The decrypted plaintext is displayed as an integer. If the plaintext represents encoded text (e.g., ASCII), additional decoding steps may be needed.
