"""
Hill Cipher Implementation

The Hill cipher is a polygraphic substitution cipher based on linear algebra.
It encrypts blocks of letters (typically pairs or triplets) using matrix multiplication.
The key is a square matrix of size n×n, where n is the block size.

Requirements:
- The key matrix must be invertible modulo 26
- The determinant of the key matrix must be coprime with 26

Example using a 2×2 matrix:
    Key matrix K = [[2, 1],
                   [3, 4]]
    Plaintext: "HELP" -> [[7, 4], [11, 15]]
    Ciphertext = K × Plaintext (mod 26)
"""

import numpy as np
from typing import List, Tuple

def matrix_mod_inverse(matrix: np.ndarray, modulus: int) -> np.ndarray:
    """
    Calculate the modular multiplicative inverse of a matrix.
    
    Args:
        matrix (np.ndarray): The matrix to invert
        modulus (int): The modulus to use
    
    Returns:
        np.ndarray: The modular multiplicative inverse of the matrix
    
    Raises:
        ValueError: If the matrix is not invertible modulo the given modulus
    """
    det = int(round(np.linalg.det(matrix)))
    det_inv = pow(det % modulus, -1, modulus)
    
    # Calculate adjugate matrix
    adj = np.round(det * np.linalg.inv(matrix)).astype(int)
    
    # Calculate modular multiplicative inverse
    inv = (det_inv * adj) % modulus
    return inv

def prepare_text(text: str, block_size: int) -> Tuple[np.ndarray, int]:
    """
    Convert text to a matrix of numbers and pad if necessary.
    
    Args:
        text (str): The text to convert
        block_size (int): The size of each block
    
    Returns:
        Tuple[np.ndarray, int]: The matrix and the number of padding characters added
    """
    # Remove non-alphabetic characters and convert to uppercase
    text = ''.join(c for c in text.upper() if c.isalpha())
    
    # Pad text if necessary
    padding = (block_size - len(text) % block_size) % block_size
    text += 'X' * padding
    
    # Convert to numbers (A=0, B=1, etc.)
    numbers = [ord(c) - ord('A') for c in text]
    
    # Reshape into matrix
    matrix = np.array(numbers).reshape(-1, block_size)
    return matrix, padding

def encrypt(text: str, key_matrix: np.ndarray) -> str:
    """
    Encrypt text using the Hill cipher.
    
    Args:
        text (str): The plaintext to encrypt
        key_matrix (np.ndarray): The key matrix to use
    
    Returns:
        str: The encrypted text
    
    Raises:
        ValueError: If the key matrix is not valid
    """
    block_size = len(key_matrix)
    
    # Check if key matrix is valid
    det = int(round(np.linalg.det(key_matrix)))
    if det == 0 or np.gcd(det % 26, 26) != 1:
        raise ValueError("Invalid key matrix: must be invertible modulo 26")
    
    # Prepare text
    text_matrix, _ = prepare_text(text, block_size)
    
    # Encrypt: C = KP mod 26
    encrypted_matrix = (key_matrix @ text_matrix.T) % 26
    
    # Convert back to text
    encrypted_text = ''.join(chr(n + ord('A')) for n in encrypted_matrix.T.flatten())
    return encrypted_text

def decrypt(text: str, key_matrix: np.ndarray) -> str:
    """
    Decrypt text using the Hill cipher.
    
    Args:
        text (str): The ciphertext to decrypt
        key_matrix (np.ndarray): The key matrix used for encryption
    
    Returns:
        str: The decrypted text
    
    Raises:
        ValueError: If the key matrix is not valid
    """
    block_size = len(key_matrix)
    
    # Calculate inverse key matrix
    key_matrix_inv = matrix_mod_inverse(key_matrix, 26)
    
    # Prepare text
    text_matrix, padding = prepare_text(text, block_size)
    
    # Decrypt: P = K^(-1)C mod 26
    decrypted_matrix = (key_matrix_inv @ text_matrix.T) % 26
    
    # Convert back to text and remove padding
    decrypted_text = ''.join(chr(n + ord('A')) for n in decrypted_matrix.T.flatten())
    if padding:
        decrypted_text = decrypted_text[:-padding]
    
    return decrypted_text

if __name__ == "__main__":
    # Example usage with 2x2 matrix
    key = np.array([[2, 1],
                   [3, 4]])
    
    message = "HELP"
    
    try:
        # Encryption
        encrypted = encrypt(message, key)
        print(f"Original message: {message}")
        print(f"Key matrix:\n{key}")
        print(f"Encrypted message: {encrypted}")
        
        # Decryption
        decrypted = decrypt(encrypted, key)
        print(f"Decrypted message: {decrypted}")
        
    except ValueError as e:
        print(f"Error: {e}") 