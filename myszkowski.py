"""
Myszkowski Transposition Cipher Implementation

The Myszkowski transposition is a variation of the columnar transposition cipher.
The key idea is to group columns with identical key letters and read them off together.
This makes it more secure than a simple columnar transposition.

Example:
    Plaintext: HELLO WORLD
    Key: ZEBRAS
    
    Arrangement:
    Key:      Z E B R A S
    Message:  H E L L O W
             O R L D X X
    
    Reading order: columns under E together, then A, B, R, S, Z
    Ciphertext: ERLOHLDXWXX
"""

from typing import List, Dict, Set
from collections import defaultdict

def prepare_text_and_key(text: str, key: str) -> tuple:
    """
    Prepare the text and key for encryption/decryption.
    
    Args:
        text (str): The text to process
        key (str): The encryption key
    
    Returns:
        tuple: (processed text, key, number of rows needed)
    """
    # Remove spaces and convert to uppercase
    text = ''.join(c.upper() for c in text if c.isalnum())
    key = key.upper()
    
    # Calculate number of rows needed
    cols = len(key)
    rows = (len(text) + cols - 1) // cols
    
    # Pad text if necessary
    padding = rows * cols - len(text)
    if padding > 0:
        text += 'X' * padding
    
    return text, key, rows

def create_grid(text: str, key: str) -> List[List[str]]:
    """
    Create a grid from the text using the key.
    
    Args:
        text (str): The text to arrange in the grid
        key (str): The encryption key
    
    Returns:
        List[List[str]]: The grid containing the text
    """
    text, key, rows = prepare_text_and_key(text, key)
    cols = len(key)
    
    # Create grid
    grid = []
    for i in range(0, len(text), cols):
        grid.append(list(text[i:i+cols]))
    
    return grid

def get_column_groups(key: str) -> Dict[str, List[int]]:
    """
    Group columns by their key letters.
    
    Args:
        key (str): The encryption key
    
    Returns:
        Dict[str, List[int]]: Dictionary mapping key letters to their column indices
    """
    groups = defaultdict(list)
    for i, char in enumerate(key):
        groups[char].append(i)
    return dict(sorted(groups.items()))

def encrypt(text: str, key: str) -> str:
    """
    Encrypt text using the Myszkowski transposition cipher.
    
    Args:
        text (str): The plaintext to encrypt
        key (str): The encryption key
    
    Returns:
        str: The encrypted text
    """
    # Create the grid
    grid = create_grid(text, key)
    
    # Group columns by key letters
    column_groups = get_column_groups(key)
    
    # Read off the columns in order of sorted unique key letters
    result = []
    for _, columns in column_groups.items():
        for col in columns:
            for row in grid:
                result.append(row[col])
    
    return ''.join(result)

def decrypt(text: str, key: str) -> str:
    """
    Decrypt text using the Myszkowski transposition cipher.
    
    Args:
        text (str): The ciphertext to decrypt
        key (str): The encryption key used
    
    Returns:
        str: The decrypted text
    """
    cols = len(key)
    rows = len(text) // cols
    
    # Create empty grid
    grid = [['' for _ in range(cols)] for _ in range(rows)]
    
    # Group columns by key letters
    column_groups = get_column_groups(key)
    
    # Fill the grid using the column groups
    index = 0
    for _, columns in column_groups.items():
        for col in columns:
            for row in range(rows):
                grid[row][col] = text[index]
                index += 1
    
    # Read off row by row
    result = []
    for row in grid:
        result.extend(row)
    
    return ''.join(result)

if __name__ == "__main__":
    # Example usage
    message = "HELLO WORLD"
    key = "ZEBRAS"
    
    # Encryption
    encrypted = encrypt(message, key)
    print(f"Original message: {message}")
    print(f"Key: {key}")
    print(f"Encrypted message: {encrypted}")
    
    # Decryption
    decrypted = decrypt(encrypted, key)
    print(f"Decrypted message: {decrypted}") 