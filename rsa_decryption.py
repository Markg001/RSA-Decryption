#!/usr/bin/env python3

"""
RSA Decryption Script
This script implements the RSA decryption algorithm to decrypt ciphertext using the private key.
It is a practical demonstration of the mathematical principles behind public-key cryptography.
FORMULAR == PLAINTEXT = CIPHERTEXT^d mod n


"""

# Function to perform modular exponentiation: (base^exp) % mod
def modular_exponentiation(base, exp, mod):
    """
    Efficiently computes (base^exp) % mod using the square-and-multiply method.
    :param base: The base integer.
    :param exp: The exponent.
    :param mod: The modulus.
    :return: Result of (base^exp) % mod.
    """
    result = 1
    base = base % mod  # Reduce base modulo mod initially
    while exp > 0:
        if exp % 2 == 1:  # If exp is odd, multiply the current base to the result
            result = (result * base) % mod
        exp = exp >> 1  # Divide exp by 2
        base = (base * base) % mod  # Square the base modulo mod
    return result


# RSA decryption function
def rsa_decrypt(ciphertext, private_key, modulus):
    """
    Decrypts the given ciphertext using the private key and modulus.
    :param ciphertext: The encrypted message (integer format).
    :param private_key: The private key (d).
    :param modulus: The modulus (n).
    :return: Decrypted plaintext as an integer.
    """
    return modular_exponentiation(ciphertext, private_key, modulus)


# Main function for demonstration
if __name__ == "__main__":
    print("RSA Decryption Script")

    # Example inputs (replace these with actual values)
    ciphertext = int(input("Enter the ciphertext (as an integer): "))
    private_key = int(input("Enter the private key (d): "))
    modulus = int(input("Enter the modulus (n): "))

    # Perform decryption
    plaintext = rsa_decrypt(ciphertext, private_key, modulus)

    # Output the result
    print(f"\nDecrypted plaintext (integer): {plaintext}")
    print("If the plaintext represents text, you may need to decode it (e.g., using ASCII).")
