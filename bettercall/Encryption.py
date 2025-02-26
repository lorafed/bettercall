from cryptography.fernet import Fernet

# Generate a key for encryption/decryption
key = Fernet.generate_key()
cipher_suite = Fernet(key)

def encrypt_data(data):
    encrypted_data = cipher_suite.encrypt(data.encode())
    return encrypted_data

def decrypt_data(encrypted_data):
    decrypted_data = cipher_suite.decrypt(encrypted_data).decode()
    return decrypted_data

# Example usage
donor_email = "donor@example.com"
encrypted_email = encrypt_data(donor_email)
print(f"Encrypted Email: {encrypted_email}")

decrypted_email = decrypt_data(encrypted_email)
print(f"Decrypted Email: {decrypted_email}")
