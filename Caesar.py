import sys

def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    if mode == 'decrypt':
        shift = -shift

    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

if len(sys.argv) != 4:
     print("Usage: python3 c2.py <mode> <text> <shift>")
     sys.exit(1)

mode = sys.argv[1].strip().lower()
text = sys.argv[2]
shift = int(sys.argv[3])

if mode not in ['encrypt', 'decrypt']:
     print("Invalid mode selected. Please choose either 'encrypt' or 'decrypt'.")
     sys.exit(1)

result = caesar_cipher(text, shift, mode)
print(f"The result is: {result}")