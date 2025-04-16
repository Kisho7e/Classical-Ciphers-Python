"""
August Cipher Implementation

The August cipher is a variant of the Vigenère cipher that uses a progressive shift.
Instead of using a repeating key, it increases the shift value for each character.
This makes it more secure than a simple Caesar cipher but still vulnerable to cryptanalysis.

Example:
    With initial shift of 1, each character is shifted by an increasing amount:
    1st char: shift 1
    2nd char: shift 2
    3rd char: shift 3
    and so on...
"""

def encrypt(text: str, initial_shift: int = 1) -> str:
    """
    Encrypt the given text using the August cipher.
    
    Args:
        text (str): The plaintext to encrypt
        initial_shift (int): The initial shift value (default: 1)
    
    Returns:
        str: The encrypted text
    """
    result = ""
    shift = initial_shift
    
    for char in text:
        if char.isalpha():
            # Determine the case and base ASCII value
            ascii_base = ord('A') if char.isupper() else ord('a')
            # Apply progressive shift and wrap around using modulo
            shifted = (ord(char) - ascii_base + shift) % 26
            result += chr(ascii_base + shifted)
            shift += 1  # Increase shift for next character
        else:
            result += char
            # Don't increase shift for non-alphabetic characters
    
    return result

def decrypt(text: str, initial_shift: int = 1) -> str:
    """
    Decrypt the given text using the August cipher.
    
    Args:
        text (str): The ciphertext to decrypt
        initial_shift (int): The initial shift value used for encryption (default: 1)
    
    Returns:
        str: The decrypted text
    """
    result = ""
    shift = initial_shift
    
    for char in text:
        if char.isalpha():
            # Determine the case and base ASCII value
            ascii_base = ord('A') if char.isupper() else ord('a')
            # Apply reverse progressive shift and wrap around using modulo
            shifted = (ord(char) - ascii_base - shift) % 26
            result += chr(ascii_base + shifted)
            shift += 1  # Increase shift for next character
        else:
            result += char
            # Don't increase shift for non-alphabetic characters
    
    return result

if __name__ == "__main__":
    # Example usage
    message = "HELLO WORLD"
    initial_shift = 1
    
    # Encryption
    encrypted = encrypt(message, initial_shift)
    print(f"Original message: {message}")
    print(f"Encrypted message (initial shift={initial_shift}): {encrypted}")
    
    # Decryption
    decrypted = decrypt(encrypted, initial_shift)
    print(f"Decrypted message: {decrypted}") 