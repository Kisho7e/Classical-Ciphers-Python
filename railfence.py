"""
Rail Fence Cipher Implementation

The Rail Fence cipher is a transposition cipher that arranges the plaintext in a zigzag
pattern on a number of "rails" and then reads off the text row by row to produce the
ciphertext.

Example with 3 rails:
    Plaintext: "HELLO WORLD"
    Arrangement:
    H   O   R
    E L W L
    L   O   D
    Ciphertext: "HORELWLOD"
"""

def create_fence(text: str, rails: int) -> list:
    """
    Create a rail fence pattern from the text.
    
    Args:
        text (str): The text to arrange
        rails (int): The number of rails to use
    
    Returns:
        list: A 2D list representing the rail fence
    """
    fence = [['\n' for _ in range(len(text))] for _ in range(rails)]
    rail = 0
    direction = 1  # 1 for down, -1 for up
    
    for i in range(len(text)):
        fence[rail][i] = text[i]
        
        # Change direction if we hit the top or bottom rail
        if rail == 0:
            direction = 1
        elif rail == rails - 1:
            direction = -1
            
        rail += direction
        
    return fence

def encrypt(text: str, rails: int) -> str:
    """
    Encrypt text using the Rail Fence cipher.
    
    Args:
        text (str): The plaintext to encrypt
        rails (int): The number of rails to use
    
    Returns:
        str: The encrypted text
    
    Raises:
        ValueError: If rails < 2 or rails > len(text)
    """
    if rails < 2:
        raise ValueError("Number of rails must be at least 2")
    if rails > len(text):
        raise ValueError("Number of rails cannot be greater than text length")
    
    # Create the rail fence pattern
    fence = create_fence(text, rails)
    
    # Read off the cipher text
    result = []
    for rail in fence:
        for char in rail:
            if char != '\n':
                result.append(char)
                
    return ''.join(result)

def decrypt(text: str, rails: int) -> str:
    """
    Decrypt text using the Rail Fence cipher.
    
    Args:
        text (str): The ciphertext to decrypt
        rails (int): The number of rails used for encryption
    
    Returns:
        str: The decrypted text
    
    Raises:
        ValueError: If rails < 2 or rails > len(text)
    """
    if rails < 2:
        raise ValueError("Number of rails must be at least 2")
    if rails > len(text):
        raise ValueError("Number of rails cannot be greater than text length")
    
    # Create an empty fence
    fence = [['\n' for _ in range(len(text))] for _ in range(rails)]
    
    # Mark the zigzag pattern
    rail = 0
    direction = 1
    for i in range(len(text)):
        fence[rail][i] = '*'
        
        if rail == 0:
            direction = 1
        elif rail == rails - 1:
            direction = -1
            
        rail += direction
    
    # Fill in the fence with the ciphertext
    index = 0
    for i in range(rails):
        for j in range(len(text)):
            if fence[i][j] == '*':
                fence[i][j] = text[index]
                index += 1
    
    # Read off the plaintext
    result = []
    rail = 0
    direction = 1
    
    for i in range(len(text)):
        result.append(fence[rail][i])
        
        if rail == 0:
            direction = 1
        elif rail == rails - 1:
            direction = -1
            
        rail += direction
    
    return ''.join(result)

if __name__ == "__main__":
    # Example usage
    message = "HELLO WORLD"
    rails = 3
    
    try:
        # Encryption
        encrypted = encrypt(message, rails)
        print(f"Original message: {message}")
        print(f"Number of rails: {rails}")
        print(f"Encrypted message: {encrypted}")
        
        # Decryption
        decrypted = decrypt(encrypted, rails)
        print(f"Decrypted message: {decrypted}")
        
    except ValueError as e:
        print(f"Error: {e}") 