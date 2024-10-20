import unittest
from src.encryption import encrypt_data, decrypt_data

class TestEncryption(unittest.TestCase):
    def test_encrypt_decrypt_standard_string(self):
        test_data = "Test data for encryption"
        encrypted_data = encrypt_data(test_data)
        decrypted_data = decrypt_data(encrypted_data)
        self.assertEqual(decrypted_data, test_data)

    def test_encrypt_decrypt_empty_string(self):
        test_data = ""
        encrypted_data = encrypt_data(test_data)
        decrypted_data = decrypt_data(encrypted_data)
        self.assertEqual(decrypted_data, test_data)

    def test_encrypt_decrypt_special_characters(self):
        test_data = "Special characters: !@#$%^&*()_+-=[]{}|;':\",./<>?"
        encrypted_data = encrypt_data(test_data)
        decrypted_data = decrypt_data(encrypted_data)
        self.assertEqual(decrypted_data, test_data)

    def test_encrypted_data_differs_from_input(self):
        test_data = "Some data"
        encrypted_data = encrypt_data(test_data)
        self.assertNotEqual(encrypted_data, test_data)

if __name__ == '__main__':
    unittest.main()
