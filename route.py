"""
Route Cipher Implementation

The Route cipher is a transposition cipher that arranges the plaintext in a grid
and then reads off the text following a specific route pattern. Common routes include
spiral (inward or outward), snake pattern, or diagonal paths.

This implementation supports the following routes:
1. Spiral inward (clockwise)
2. Spiral outward (counterclockwise)
3. Snake (left-to-right, alternating)
4. Diagonal (top-left to bottom-right)
"""

from typing import List, Tuple
import math

def create_grid(text: str, rows: int, cols: int) -> List[List[str]]:
    """
    Create a grid from the text, padding with 'X' if necessary.
    
    Args:
        text (str): The text to arrange in the grid
        rows (int): Number of rows in the grid
        cols (int): Number of columns in the grid
    
    Returns:
        List[List[str]]: The grid containing the text
    """
    # Remove spaces and convert to uppercase
    text = ''.join(c.upper() for c in text if c.isalnum())
    
    # Pad text if necessary
    padding = rows * cols - len(text)
    if padding > 0:
        text += 'X' * padding
    
    # Create grid
    grid = []
    for i in range(0, len(text), cols):
        grid.append(list(text[i:i+cols]))
    
    return grid

def spiral_inward(rows: int, cols: int) -> List[Tuple[int, int]]:
    """Generate coordinates for spiral inward pattern."""
    coordinates = []
    top, bottom = 0, rows - 1
    left, right = 0, cols - 1
    
    while top <= bottom and left <= right:
        # Move right
        for i in range(left, right + 1):
            coordinates.append((top, i))
        top += 1
        
        # Move down
        for i in range(top, bottom + 1):
            coordinates.append((i, right))
        right -= 1
        
        if top <= bottom:
            # Move left
            for i in range(right, left - 1, -1):
                coordinates.append((bottom, i))
            bottom -= 1
        
        if left <= right:
            # Move up
            for i in range(bottom, top - 1, -1):
                coordinates.append((i, left))
            left += 1
    
    return coordinates

def spiral_outward(rows: int, cols: int) -> List[Tuple[int, int]]:
    """Generate coordinates for spiral outward pattern."""
    return list(reversed(spiral_inward(rows, cols)))

def snake_pattern(rows: int, cols: int) -> List[Tuple[int, int]]:
    """Generate coordinates for snake pattern."""
    coordinates = []
    for i in range(rows):
        if i % 2 == 0:
            # Left to right
            for j in range(cols):
                coordinates.append((i, j))
        else:
            # Right to left
            for j in range(cols - 1, -1, -1):
                coordinates.append((i, j))
    return coordinates

def diagonal_pattern(rows: int, cols: int) -> List[Tuple[int, int]]:
    """Generate coordinates for diagonal pattern."""
    coordinates = []
    for sum_idx in range(rows + cols - 1):
        for i in range(rows):
            j = sum_idx - i
            if 0 <= j < cols:
                coordinates.append((i, j))
    return coordinates

def encrypt(text: str, rows: int, cols: int, pattern: str = "spiral_in") -> str:
    """
    Encrypt text using the Route cipher.
    
    Args:
        text (str): The plaintext to encrypt
        rows (int): Number of rows in the grid
        cols (int): Number of columns in the grid
        pattern (str): The route pattern to use
            ("spiral_in", "spiral_out", "snake", "diagonal")
    
    Returns:
        str: The encrypted text
    
    Raises:
        ValueError: If the pattern is invalid or grid dimensions are invalid
    """
    if rows < 1 or cols < 1:
        raise ValueError("Grid dimensions must be positive")
    
    # Create the grid
    grid = create_grid(text, rows, cols)
    
    # Get coordinates for the chosen pattern
    pattern_funcs = {
        "spiral_in": spiral_inward,
        "spiral_out": spiral_outward,
        "snake": snake_pattern,
        "diagonal": diagonal_pattern
    }
    
    if pattern not in pattern_funcs:
        raise ValueError(f"Invalid pattern. Choose from: {', '.join(pattern_funcs.keys())}")
    
    coordinates = pattern_funcs[pattern](rows, cols)
    
    # Read off the text following the pattern
    result = []
    for row, col in coordinates:
        result.append(grid[row][col])
    
    return ''.join(result)

def decrypt(text: str, rows: int, cols: int, pattern: str = "spiral_in") -> str:
    """
    Decrypt text using the Route cipher.
    
    Args:
        text (str): The ciphertext to decrypt
        rows (int): Number of rows in the grid
        cols (int): Number of columns in the grid
        pattern (str): The route pattern used for encryption
            ("spiral_in", "spiral_out", "snake", "diagonal")
    
    Returns:
        str: The decrypted text
    
    Raises:
        ValueError: If the pattern is invalid or grid dimensions are invalid
    """
    if rows < 1 or cols < 1:
        raise ValueError("Grid dimensions must be positive")
    if rows * cols != len(text):
        raise ValueError("Text length must match grid size")
    
    # Get coordinates for the chosen pattern
    pattern_funcs = {
        "spiral_in": spiral_inward,
        "spiral_out": spiral_outward,
        "snake": snake_pattern,
        "diagonal": diagonal_pattern
    }
    
    if pattern not in pattern_funcs:
        raise ValueError(f"Invalid pattern. Choose from: {', '.join(pattern_funcs.keys())}")
    
    coordinates = pattern_funcs[pattern](rows, cols)
    
    # Create empty grid
    grid = [['' for _ in range(cols)] for _ in range(rows)]
    
    # Fill grid using the pattern
    for (row, col), char in zip(coordinates, text):
        grid[row][col] = char
    
    # Read grid row by row
    result = []
    for row in grid:
        result.extend(row)
    
    return ''.join(result)

if __name__ == "__main__":
    # Example usage
    message = "HELLO WORLD"
    rows, cols = 3, 4  # Grid size that can fit the message
    
    try:
        # Try different patterns
        patterns = ["spiral_in", "spiral_out", "snake", "diagonal"]
        
        for pattern in patterns:
            print(f"\nUsing {pattern} pattern:")
            
            # Encryption
            encrypted = encrypt(message, rows, cols, pattern)
            print(f"Original message: {message}")
            print(f"Grid size: {rows}x{cols}")
            print(f"Encrypted message: {encrypted}")
            
            # Decryption
            decrypted = decrypt(encrypted, rows, cols, pattern)
            print(f"Decrypted message: {decrypted}")
            
    except ValueError as e:
        print(f"Error: {e}") 