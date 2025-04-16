"""
Autokey Cipher Implementation

The Autokey cipher is a polyalphabetic substitution cipher that uses the plaintext
itself as part of the key. It begins with a priming key, and then uses the plaintext
as the key for subsequent characters. This makes it more secure than the Vigenère
cipher because the key does not repeat in a predictable pattern.

Example:
    Plaintext: HELLO WORLD
    Priming Key: KEY
    Full Key: KEY + HELLO WORLD = KEYHELLOWORL
"""

def prepare_key(text: str, priming_key: str) -> str:
    """
    Prepare the key by combining the priming key with the plaintext,
    ignoring non-alphabetic characters.
    
    Args:
        text (str): The plaintext to use for key generation
        priming_key (str): The initial key
    
    Returns:
        str: The prepared key
    """
    priming_key = priming_key.upper()
    text = text.upper()
    key = list(priming_key)
    text_index = 0
    
    # Build the full key using the plaintext
    for i in range(len(priming_key), len(text)):
        if text[text_index].isalpha():
            key.append(text[text_index])
            text_index += 1
        else:
            key.append(text[text_index])
            text_index += 1
            
    return ''.join(key)

def encrypt(text: str, priming_key: str) -> str:
    """
    Encrypt the given text using the Autokey cipher.
    
    Args:
        text (str): The plaintext to encrypt
        priming_key (str): The initial key
    
    Returns:
        str: The encrypted text
    """
    key = prepare_key(text, priming_key)
    result = ""
    
    for text_char, key_char in zip(text, key):
        if text_char.isalpha():
            # Determine the case and base ASCII value
            is_upper = text_char.isupper()
            text_num = ord(text_char.upper()) - ord('A')
            key_num = ord(key_char.upper()) - ord('A')
            
            # Apply Autokey shift (similar to Vigenère)
            encrypted_num = (text_num + key_num) % 26
            encrypted_char = chr(encrypted_num + ord('A'))
            
            result += encrypted_char if is_upper else encrypted_char.lower()
        else:
            result += text_char
    
    return result

def decrypt(text: str, priming_key: str) -> str:
    """
    Decrypt the given text using the Autokey cipher.
    
    Args:
        text (str): The ciphertext to decrypt
        priming_key (str): The initial key used for encryption
    
    Returns:
        str: The decrypted text
    """
    result = ""
    key = list(priming_key.upper())
    text_index = 0
    
    for i, char in enumerate(text):
        if char.isalpha():
            # Determine the case and base ASCII value
            is_upper = char.isupper()
            text_num = ord(char.upper()) - ord('A')
            
            if i < len(priming_key):
                key_num = ord(key[i].upper()) - ord('A')
            else:
                key_num = ord(result[text_index].upper()) - ord('A')
                text_index += 1
            
            # Apply reverse Autokey shift
            decrypted_num = (text_num - key_num) % 26
            decrypted_char = chr(decrypted_num + ord('A'))
            
            result += decrypted_char if is_upper else decrypted_char.lower()
        else:
            result += char
            
    return result

if __name__ == "__main__":
    # Example usage
    message = "HELLO WORLD"
    priming_key = "KEY"
    
    # Encryption
    encrypted = encrypt(message, priming_key)
    print(f"Original message: {message}")
    print(f"Priming key: {priming_key}")
    print(f"Encrypted message: {encrypted}")
    
    # Decryption
    decrypted = decrypt(encrypted, priming_key)
    print(f"Decrypted message: {decrypted}") 