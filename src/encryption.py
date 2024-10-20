import os
from cryptography.fernet import Fernet

# Generate and store this key securely in a real-world scenario
key = Fernet.generate_key()
fernet = Fernet(key)

def encrypt_data(data):
    """
    Encrypt data using Fernet symmetric encryption.
    """
    return fernet.encrypt(data.encode()).decode()

def decrypt_data(token):
    """
    Decrypt data using Fernet symmetric encryption.
    """
    return fernet.decrypt(token.encode()).decode()

def test_data_encryption():
    """
    Test function for Data Encryption symbol (ΔΕ1)
    """
    test_data = "Sensitive information for encryption"
    encrypted_data = encrypt_data(test_data)
    decrypted_data = decrypt_data(encrypted_data)
    
    return decrypted_data == test_data, test_data, encrypted_data
