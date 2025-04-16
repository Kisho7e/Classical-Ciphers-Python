"""
N-gram Analysis Implementation

This module provides tools for analyzing text using n-grams (sequences of n characters
or words). N-gram analysis is useful in cryptography for:
1. Frequency analysis
2. Pattern recognition
3. Language detection
4. Cryptanalysis of substitution ciphers

Common n-gram sizes:
- Unigrams (n=1): Single character frequencies
- Bigrams (n=2): Two-character sequences
- Trigrams (n=3): Three-character sequences
"""

from collections import Counter
from typing import Dict, List, Union
import re

def get_ngrams(text: str, n: int, as_word: bool = False) -> List[str]:
    """
    Extract n-grams from the given text.
    
    Args:
        text (str): The text to analyze
        n (int): The size of each n-gram
        as_word (bool): If True, split text into words instead of characters
    
    Returns:
        List[str]: List of n-grams found in the text
    
    Raises:
        ValueError: If n < 1
    """
    if n < 1:
        raise ValueError("n must be at least 1")
    
    # Prepare text
    if as_word:
        # Split into words and remove punctuation
        words = re.findall(r'\b\w+\b', text.lower())
        if len(words) < n:
            return []
        return [' '.join(words[i:i+n]) for i in range(len(words)-n+1)]
    else:
        # Use characters
        text = text.upper()
        return [text[i:i+n] for i in range(len(text)-n+1)]

def frequency_analysis(text: str, n: int = 1, as_word: bool = False) -> Dict[str, float]:
    """
    Perform frequency analysis on the text using n-grams.
    
    Args:
        text (str): The text to analyze
        n (int): The size of each n-gram
        as_word (bool): If True, analyze word n-grams instead of character n-grams
    
    Returns:
        Dict[str, float]: Dictionary mapping n-grams to their frequencies (as percentages)
    """
    ngrams = get_ngrams(text, n, as_word)
    if not ngrams:
        return {}
    
    # Count occurrences
    counts = Counter(ngrams)
    total = sum(counts.values())
    
    # Calculate frequencies as percentages
    return {ngram: (count/total)*100 for ngram, count in counts.most_common()}

def find_repeated_sequences(text: str, min_length: int = 3, max_length: int = 10) -> Dict[str, List[int]]:
    """
    Find repeated sequences in the text and their positions.
    Useful for cryptanalysis of polyalphabetic ciphers.
    
    Args:
        text (str): The text to analyze
        min_length (int): Minimum sequence length to consider
        max_length (int): Maximum sequence length to consider
    
    Returns:
        Dict[str, List[int]]: Dictionary mapping sequences to lists of their starting positions
    """
    text = text.upper()
    repeated_sequences = {}
    
    # Check sequences of different lengths
    for length in range(min_length, max_length + 1):
        sequences = {}
        
        # Find all sequences of current length
        for i in range(len(text) - length + 1):
            seq = text[i:i+length]
            if seq.isalpha():  # Only consider alphabetic sequences
                if seq in sequences:
                    sequences[seq].append(i)
                else:
                    sequences[seq] = [i]
        
        # Add sequences that appear more than once
        repeated_sequences.update({seq: pos for seq, pos in sequences.items() if len(pos) > 1})
    
    return repeated_sequences

def index_of_coincidence(text: str) -> float:
    """
    Calculate the index of coincidence for the text.
    This can be used to determine whether a cipher is monoalphabetic or polyalphabetic.
    
    Args:
        text (str): The text to analyze
    
    Returns:
        float: The index of coincidence
    """
    text = ''.join(c for c in text.upper() if c.isalpha())
    if len(text) <= 1:
        return 0.0
    
    # Count frequencies
    frequencies = Counter(text)
    n = len(text)
    
    # Calculate IoC
    ioc = sum(f * (f-1) for f in frequencies.values()) / (n * (n-1))
    return ioc

if __name__ == "__main__":
    # Example usage
    sample_text = "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG"
    
    # Character frequency analysis
    print("Character Frequencies:")
    char_freq = frequency_analysis(sample_text, n=1)
    for char, freq in char_freq.items():
        print(f"{char}: {freq:.2f}%")
    
    # Bigram analysis
    print("\nBigram Frequencies:")
    bigram_freq = frequency_analysis(sample_text, n=2)
    for bigram, freq in bigram_freq.items():
        print(f"{bigram}: {freq:.2f}%")
    
    # Word frequency analysis
    print("\nWord Frequencies:")
    word_freq = frequency_analysis(sample_text, n=1, as_word=True)
    for word, freq in word_freq.items():
        print(f"{word}: {freq:.2f}%")
    
    # Find repeated sequences
    print("\nRepeated Sequences:")
    repeated = find_repeated_sequences(sample_text)
    for seq, positions in repeated.items():
        print(f"{seq}: appears at positions {positions}")
    
    # Calculate Index of Coincidence
    ioc = index_of_coincidence(sample_text)
    print(f"\nIndex of Coincidence: {ioc:.4f}") 