# Classical-Ciphers-Python 🔐

A comprehensive collection of 13 classical cipher implementations in Python. This repository provides clean, well-documented implementations of historical encryption methods.

## 📋 Included Ciphers

1. **Caesar Cipher**: A substitution cipher that shifts letters by a fixed number of positions.
2. **Atbash Cipher**: A substitution cipher that maps each letter to its reverse position in the alphabet.
3. **August Cipher**: A variant of the Vigenère cipher using a progressive shift.
4. **Affine Cipher**: A monoalphabetic substitution cipher using linear transformations.
5. **Vigenère Cipher**: A polyalphabetic substitution cipher using a keyword.
6. **Gronsfeld Cipher**: Similar to Vigenère but uses numbers instead of a keyword.
7. **Beaufort Cipher**: A reciprocal substitution cipher related to the Vigenère cipher.
8. **Autokey/Running Key Cipher**: A polyalphabetic cipher where the plaintext forms part of the key.
9. **N-Gram Operations**: Tools for analyzing text using n-gram frequencies.
10. **Hill Cipher**: A polygraphic substitution cipher based on linear algebra.
11. **Rail Fence Cipher**: A transposition cipher arranging text in a zigzag pattern.
12. **Route Cipher**: A transposition cipher following specific routes through a grid.
13. **Myszkowski Cipher**: A columnar transposition cipher with a twist.

## 🚀 Usage Examples

### Caesar Cipher
```python
from caesar import encrypt, decrypt

# Encrypt a message
encrypted = encrypt("HELLO WORLD", shift=3)
print(encrypted)  # Output: "KHOOR ZRUOG"

# Decrypt the message
decrypted = decrypt("KHOOR ZRUOG", shift=3)
print(decrypted)  # Output: "HELLO WORLD"
```

### Vigenère Cipher
```python
from vigenere import encrypt, decrypt

# Encrypt a message
encrypted = encrypt("HELLO WORLD", key="KEY")
print(encrypted)  # Output: "RIJVS UYVJN"

# Decrypt the message
decrypted = decrypt("RIJVS UYVJN", key="KEY")
print(decrypted)  # Output: "HELLO WORLD"
```

### Hill Cipher
```python
from hill import encrypt, decrypt
import numpy as np

# Define a key matrix (must be invertible)
key = np.array([[2, 1], [3, 4]])

# Encrypt a message
encrypted = encrypt("HELLO", key)
print(encrypted)

# Decrypt the message
decrypted = decrypt(encrypted, key)
print(decrypted)
```

### Rail Fence Cipher
```python
from railfence import encrypt, decrypt

# Encrypt with 3 rails
encrypted = encrypt("HELLO WORLD", rails=3)
print(encrypted)

# Decrypt with 3 rails
decrypted = decrypt(encrypted, rails=3)
print(decrypted)  # Output: "HELLO WORLD"
```

### Atbash Cipher
```python
from atbash import encrypt, decrypt

# Since Atbash is its own inverse, encrypt and decrypt are the same
encrypted = encrypt("HELLO WORLD")
print(encrypted)  # Output: "SVOOL DLIOW"

decrypted = decrypt("SVOOL DLIOW")
print(decrypted)  # Output: "HELLO WORLD"
```

## 🛠️ Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/Classical-Ciphers-Python.git
cd Classical-Ciphers-Python
```

2. Install dependencies (if any):
```bash
pip install -r requirements.txt
```

## 📚 Dependencies

- NumPy (required only for Hill Cipher implementation)
- Python 3.6+

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.
