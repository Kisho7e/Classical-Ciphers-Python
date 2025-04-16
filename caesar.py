"""
Caesar Cipher Implementation

The Caesar cipher is one of the simplest and most widely known encryption techniques.
It is a type of substitution cipher in which each letter in the plaintext is 
shifted a certain number of places down the alphabet.

Example:
    With a shift of 3, A would be replaced by D, B would become E, and so on.
"""

def encrypt(text: str, shift: int) -> str:
    """
    Encrypt the given text using Caesar cipher.
    
    Args:
        text (str): The plaintext to encrypt
        shift (int): The number of positions to shift each letter
    
    Returns:
        str: The encrypted text
    """
    result = ""
    for char in text:
        if char.isalpha():
            # Determine the case and base ASCII value
            ascii_base = ord('A') if char.isupper() else ord('a')
            # Apply shift and wrap around using modulo
            shifted = (ord(char) - ascii_base + shift) % 26
            result += chr(ascii_base + shifted)
        else:
            result += char
    return result

def decrypt(text: str, shift: int) -> str:
    """
    Decrypt the given text using Caesar cipher.
    
    Args:
        text (str): The ciphertext to decrypt
        shift (int): The number of positions that were shifted
    
    Returns:
        str: The decrypted text
    """
    # Decryption is just encryption with the negative shift
    return encrypt(text, -shift)

if __name__ == "__main__":
    # Example usage
    message = "HELLO WORLD"
    shift = 3
    
    # Encryption
    encrypted = encrypt(message, shift)
    print(f"Original message: {message}")
    print(f"Encrypted message (shift={shift}): {encrypted}")
    
    # Decryption
    decrypted = decrypt(encrypted, shift)
    print(f"Decrypted message: {decrypted}") 