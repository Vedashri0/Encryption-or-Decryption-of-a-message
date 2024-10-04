def encrypt(text, shift):
    result = ""
    # Traverse the input text
    for i in range(len(text)):
        char = text[i]
        
        # Encrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        # If it's not an alphabet character, leave it as is
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)  # Decryption is just encryption with a negative shift

def main():
    print("Caesar Cipher Encryption and Decryption")
    choice = input("Do you want to encrypt or decrypt a message? (e/d): ").lower()
    
    if choice not in ['e', 'd']:
        print("Invalid choice!")
        return
    
    message = input("Enter the message: ")
    shift = int(input("Enter the shift value: "))
    
    if choice == 'e':
        encrypted_message = encrypt(message, shift)
        print(f"Encrypted Message: {encrypted_message}")
    elif choice == 'd':
        decrypted_message = decrypt(message, shift)
        print(f"Decrypted Message: {decrypted_message}")

if __name__ == "__main__":
    main()
