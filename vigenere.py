"""
Vigenère Cipher Implementation

The Vigenère cipher is a polyalphabetic substitution cipher that uses a keyword
to shift each letter in the plaintext by different amounts. It can be thought of
as a series of Caesar ciphers with different shift values determined by the keyword.

Example:
    Plaintext: HELLO
    Key: KEY
    Process: H + K, E + E, L + Y, L + K, O + E
    Result: RIJVS
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

def encrypt(text: str, key: str) -> str:
    """
    Encrypt the given text using the Vigenère cipher.
    
    Args:
        text (str): The plaintext to encrypt
        key (str): The encryption key
    
    Returns:
        str: The encrypted text
    """
    key = prepare_key(text, key)
    result = ""
    
    for text_char, key_char in zip(text, key):
        if text_char.isalpha():
            # Determine the case and base ASCII value
            is_upper = text_char.isupper()
            text_num = ord(text_char.upper()) - ord('A')
            key_num = ord(key_char.upper()) - ord('A')
            
            # Apply Vigenère shift
            encrypted_num = (text_num + key_num) % 26
            encrypted_char = chr(encrypted_num + ord('A'))
            
            result += encrypted_char if is_upper else encrypted_char.lower()
        else:
            result += text_char
    
    return result

def decrypt(text: str, key: str) -> str:
    """
    Decrypt the given text using the Vigenère cipher.
    
    Args:
        text (str): The ciphertext to decrypt
        key (str): The encryption key
    
    Returns:
        str: The decrypted text
    """
    key = prepare_key(text, key)
    result = ""
    
    for text_char, key_char in zip(text, key):
        if text_char.isalpha():
            # Determine the case and base ASCII value
            is_upper = text_char.isupper()
            text_num = ord(text_char.upper()) - ord('A')
            key_num = ord(key_char.upper()) - ord('A')
            
            # Apply reverse Vigenère shift
            decrypted_num = (text_num - key_num) % 26
            decrypted_char = chr(decrypted_num + ord('A'))
            
            result += decrypted_char if is_upper else decrypted_char.lower()
        else:
            result += text_char
    
    return result

if __name__ == "__main__":
    # Example usage
    message = "HELLO WORLD"
    key = "KEY"
    
    # Encryption
    encrypted = encrypt(message, key)
    print(f"Original message: {message}")
    print(f"Key: {key}")
    print(f"Encrypted message: {encrypted}")
    
    # Decryption
    decrypted = decrypt(encrypted, key)
    print(f"Decrypted message: {decrypted}") 