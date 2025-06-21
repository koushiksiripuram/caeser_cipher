def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) - 65 + shift) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - 97 + shift) % 26 + 97)
        elif char.isdigit():
            result += chr((ord(char) - 48 + shift) % 10 + 48)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

print("🔐 Welcome to Caesar Cipher Encryptor/Decryptor")
while True:
    print("\nWhat would you like to do?")
    print("1️⃣ Encrypt a message")
    print("2️⃣ Decrypt a message")
    print("3️⃣ Exit")

    choice = input("Enter your choice (1/2/3): ").strip()

    if choice == "3":
        print("👋 Exiting program. Goodbye!")
        break
    elif choice not in ["1", "2"]:
        print("❌ Invalid choice. Please try again.")
        continue

    message = input("✉️ Enter your message: ")
    try:
        shift = int(input("🔢 Enter your shift value (number): "))
    except ValueError:
        print("❌ Shift value must be a number.")
        continue

    if choice == "1":
        result = encrypt(message, shift)
        print("✅ Encrypted Message:", result)
    else:
        result = decrypt(message, shift)
        print("✅ Decrypted Message:", result)

    input("🔁 Press Enter to continue...")
