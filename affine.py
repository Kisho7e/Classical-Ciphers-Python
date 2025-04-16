"""
Affine Cipher Implementation

The Affine cipher is a type of monoalphabetic substitution cipher, where each letter
in an alphabet is mapped to its numeric equivalent, encrypted using a simple mathematical
function, and converted back to a letter.

The encryption function is: E(x) = (ax + b) mod m
The decryption function is: D(x) = a^(-1)(x - b) mod m
where:
    a and b are keys
    m is the size of the alphabet (26 for English)
    a must be coprime with m
"""

def gcd(a: int, b: int) -> int:
    """Calculate the Greatest Common Divisor of a and b."""
    while b:
        a, b = b, a % b
    return a

def mod_inverse(a: int, m: int) -> int:
    """Calculate the modular multiplicative inverse of a modulo m."""
    def extended_gcd(a: int, b: int) -> tuple:
        if a == 0:
            return b, 0, 1
        gcd, x1, y1 = extended_gcd(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return gcd, x, y

    if gcd(a, m) != 1:
        raise ValueError("Modular inverse does not exist")
    
    _, x, _ = extended_gcd(a, m)
    return x % m

def encrypt(text: str, a: int, b: int) -> str:
    """
    Encrypt the given text using the Affine cipher.
    
    Args:
        text (str): The plaintext to encrypt
        a (int): The multiplicative key (must be coprime with 26)
        b (int): The additive key
    
    Returns:
        str: The encrypted text
    
    Raises:
        ValueError: If 'a' is not coprime with 26
    """
    if gcd(a, 26) != 1:
        raise ValueError("'a' must be coprime with 26")
    
    result = ""
    for char in text:
        if char.isalpha():
            # Determine the case and base ASCII value
            is_upper = char.isupper()
            x = ord(char.upper()) - ord('A')
            
            # Apply affine transformation: E(x) = (ax + b) mod 26
            encrypted_x = (a * x + b) % 26
            
            # Convert back to character
            encrypted_char = chr(encrypted_x + ord('A'))
            result += encrypted_char if is_upper else encrypted_char.lower()
        else:
            result += char
    
    return result

def decrypt(text: str, a: int, b: int) -> str:
    """
    Decrypt the given text using the Affine cipher.
    
    Args:
        text (str): The ciphertext to decrypt
        a (int): The multiplicative key used for encryption
        b (int): The additive key used for encryption
    
    Returns:
        str: The decrypted text
    
    Raises:
        ValueError: If 'a' is not coprime with 26
    """
    if gcd(a, 26) != 1:
        raise ValueError("'a' must be coprime with 26")
    
    # Calculate modular multiplicative inverse of a
    a_inv = mod_inverse(a, 26)
    
    result = ""
    for char in text:
        if char.isalpha():
            # Determine the case and base ASCII value
            is_upper = char.isupper()
            y = ord(char.upper()) - ord('A')
            
            # Apply affine transformation: D(y) = a^(-1)(y - b) mod 26
            decrypted_y = (a_inv * (y - b)) % 26
            
            # Convert back to character
            decrypted_char = chr(decrypted_y + ord('A'))
            result += decrypted_char if is_upper else decrypted_char.lower()
        else:
            result += char
    
    return result

if __name__ == "__main__":
    # Example usage
    message = "HELLO WORLD"
    # Using a=5, b=8 (a must be coprime with 26)
    a, b = 5, 8
    
    try:
        # Encryption
        encrypted = encrypt(message, a, b)
        print(f"Original message: {message}")
        print(f"Encrypted message (a={a}, b={b}): {encrypted}")
        
        # Decryption
        decrypted = decrypt(encrypted, a, b)
        print(f"Decrypted message: {decrypted}")
        
    except ValueError as e:
        print(f"Error: {e}") 