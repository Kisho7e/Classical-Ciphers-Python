"""
Atbash Cipher Implementation

The Atbash cipher is a substitution cipher with a specific key where the letters
of the alphabet are reversed. In other words, A becomes Z, B becomes Y, C becomes X, and so on.
It is its own inverse, meaning the same process can be used for both encryption and decryption.

Example:
    HELLO becomes SVOOL
"""

def encrypt(text: str) -> str:
    """
    Encrypt the given text using the Atbash cipher.
    
    Args:
        text (str): The plaintext to encrypt
    
    Returns:
        str: The encrypted text
    """
    result = ""
    for char in text:
        if char.isalpha():
            # Determine the case and base ASCII value
            if char.isupper():
                result += chr(ord('Z') - (ord(char) - ord('A')))
            else:
                result += chr(ord('z') - (ord(char) - ord('a')))
        else:
            result += char
    return result

def decrypt(text: str) -> str:
    """
    Decrypt the given text using the Atbash cipher.
    Since Atbash is its own inverse, this is the same as encryption.
    
    Args:
        text (str): The ciphertext to decrypt
    
    Returns:
        str: The decrypted text
    """
    return encrypt(text)  # Atbash is its own inverse

if __name__ == "__main__":
    # Example usage
    message = "HELLO WORLD"
    
    # Encryption
    encrypted = encrypt(message)
    print(f"Original message: {message}")
    print(f"Encrypted message: {encrypted}")
    
    # Decryption
    decrypted = decrypt(encrypted)
    print(f"Decrypted message: {decrypted}") 