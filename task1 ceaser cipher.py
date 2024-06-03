def caesar_cipher_encrypt(text, key):
    encrypted_text = ""
    key_length = len(key)
    key_int = [ord(i) for i in key]
    
    for i, char in enumerate(text):
        if char.isalpha():
            shift_amount = key_int[i % key_length] % 26
            char_code = ord(char) + shift_amount
            if char.islower():
                if char_code > ord('z'):
                    char_code -= 26
            elif char.isupper():
                if char_code > ord('Z'):
                    char_code -= 26
            encrypted_text += chr(char_code)
        elif char.isdigit():
            shift_amount = key_int[i % key_length] % 10
            char_code = ord(char) + shift_amount
            if char_code > ord('9'):
                char_code -= 10
            encrypted_text += chr(char_code)
        else:
            encrypted_text += char
    return encrypted_text

def caesar_cipher_decrypt(text, key):
    decrypted_text = ""
    key_length = len(key)
    key_int = [ord(i) for i in key]

    for i, char in enumerate(text):
        if char.isalpha():
            shift_amount = key_int[i % key_length] % 26
            char_code = ord(char) - shift_amount
            if char.islower():
                if char_code < ord('a'):
                    char_code += 26
            elif char.isupper():
                if char_code < ord('A'):
                    char_code += 26
            decrypted_text += chr(char_code)
        elif char.isdigit():
            shift_amount = key_int[i % key_length] % 10
            char_code = ord(char) - shift_amount
            if char_code < ord('0'):
                char_code += 10
            decrypted_text += chr(char_code)
        else:
            decrypted_text += char
    return decrypted_text

def show_menu():
    print("Menu:")
    print("1. Encrypt a message")
    print("2. Decrypt a message")
    print("3. Exit")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1/2/3): ").strip()
        if choice == '3':
            print("Goodbye!")
            break
        elif choice not in ['1', '2']:
            print("Invalid choice, please enter 1, 2, or 3.")
            continue
        text = input("Enter the message: ").strip()
        key = input("Enter the key: ").strip()
        if choice == '1':
            result = caesar_cipher_encrypt(text, key)
            print(f"Encrypted message: {result}")
        elif choice == '2':
            result = caesar_cipher_decrypt(text, key)
            print(f"Decrypted message: {result}")

if __name__ == "__main__":
    main()
3