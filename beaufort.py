"""
Beaufort Cipher Implementation

The Beaufort cipher is a polyalphabetic substitution cipher similar to the Vigenère cipher,
but it uses a different encryption method. Instead of adding the key and plaintext values,
it subtracts the plaintext from the key. The Beaufort cipher is reciprocal, meaning the
same function is used for both encryption and decryption.

Formula: C = (K - P) mod 26, where:
    C is the ciphertext letter value
    K is the key letter value
    P is the plaintext letter value

Example:
    Plaintext: HELLO
    Key: KEY
    Process: For H: K - H mod 26, For E: E - E mod 26, etc.
"""

def prepare_key(text: str, key: str) -> str:
    """
    Prepare the key by repeating it to match the length of the text,
    ignoring non-alphabetic characters in the text.
    
    Args:
        text (str): The text to match length with
        key (str): The key to repeat
    
    Returns:
        str: The prepared key
    """
    key = key.upper()
    key_repeated = ""
    key_index = 0
    
    for char in text:
        if char.isalpha():
            key_repeated += key[key_index % len(key)]
            key_index += 1
        else:
            key_repeated += char
            
    return key_repeated

def beaufort(text: str, key: str) -> str:
    """
    Apply the Beaufort cipher to the text. This function works for both encryption
    and decryption since the Beaufort cipher is reciprocal.
    
    Args:
        text (str): The text to encrypt/decrypt
        key (str): The encryption/decryption key
    
    Returns:
        str: The processed text
    """
    key = prepare_key(text, key)
    result = ""
    
    for text_char, key_char in zip(text, key):
        if text_char.isalpha():
            # Determine the case and base ASCII value
            is_upper = text_char.isupper()
            text_num = ord(text_char.upper()) - ord('A')
            key_num = ord(key_char.upper()) - ord('A')
            
            # Apply Beaufort transformation: C = (K - P) mod 26
            beaufort_num = (key_num - text_num) % 26
            beaufort_char = chr(beaufort_num + ord('A'))
            
            result += beaufort_char if is_upper else beaufort_char.lower()
        else:
            result += text_char
    
    return result

# Since the Beaufort cipher is reciprocal, encryption and decryption use the same function
encrypt = beaufort
decrypt = beaufort

if __name__ == "__main__":
    # Example usage
    message = "HELLO WORLD"
    key = "KEY"
    
    # Encryption
    encrypted = encrypt(message, key)
    print(f"Original message: {message}")
    print(f"Key: {key}")
    print(f"Encrypted message: {encrypted}")
    
    # Decryption (using the same function)
    decrypted = decrypt(encrypted, key)
    print(f"Decrypted message: {decrypted}") 