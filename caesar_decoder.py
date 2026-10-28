# This is a simple cipher message decoder 
def caesar_decoder(ciphertext,key):
    decryptedText = ''
    for char in ciphertext:
        if char.isupper():
            
            decryptedChar =chr((ord(char)-ord('A') - key)% 26 + ord('A'))
            decryptedText += decryptedChar
        elif char.islower():
            decryptedChar =chr((ord(char)-ord('a') - key)% 26 + ord('a'))
            decryptedText += decryptedChar
        else:
            decryptedText += char
    return decryptedText
cipher = "DRQV NREK WVN WRCC"
key = 0
for i in range(1, 26):
    key = key +1
    original_text = caesar_decoder(cipher,key)
    print(f"{original_text}")