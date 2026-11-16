# Hill-Cipher-Encryption-Decryption
Python implementation of the Hill Cipher using matrix operations, modular arithmetic, and encryption/decryption algorithms.

## Project Overview
This academic project at Brock University explores the implementation of the Hill Cipher, a classical encryption method based on linear algebra and modular arithmetic. The project demonstrates how mathematical concepts can be translated into Python algorithms to encrypt and decrypt text.

## Technologies Used
- Python
- Linear algebra
- Matrix multiplication
- Modular arithmetic
- Algorithm development and testing

## Methodology
- Converted plaintext letters into numerical values for mathematical processing.
- Grouped characters into pairs for encryption using a 2 × 2 key matrix.
- Applied matrix multiplication and modular arithmetic (mod 26) to generate encrypted text.
- Developed a modular inverse function for use in matrix inversion and decryption.
- Implemented padding for messages containing an odd number of characters.
- Investigated the importance of matrix invertibility for successful decryption.

## Project Findings
- Demonstrated the relationship between matrix operations, modular arithmetic, and classical encryption.
- Identified that a key matrix must have a determinant relatively prime to 26 to be invertible modulo 26.
- Explored how numerical encoding and matrix inversion can be used to recover plaintext.

## Skills Demonstrated
- Python scripting and algorithm development
- Mathematical and computational problem-solving
- Matrix operations and modular arithmetic
- Testing and debugging
- Technical documentation

## Project Files
- `hill_cipher.py` — Python implementation of the Hill Cipher.
- `Hill_Cipher_Project_Report.pdf` — Written report explaining the mathematical background, methodology, and observations.

## Author
Leah Neufeld

Brock University | Bachelor of Science, Statistics
