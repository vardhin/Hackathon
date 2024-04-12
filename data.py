import os
from cryptography.fernet import Fernet

# Generate a key and store it securely
def generate_and_store_key(filename):
    key = Fernet.generate_key()
    with open(filename, "wb") as key_file:
        key_file.write(key)

# Load the key from the secure storage
def load_key(filename):
    with open(filename, "rb") as key_file:
        key = key_file.read()
    return key

# Encrypt data using the stored key
def encrypt_data(key, data):
    cipher_suite = Fernet(key)
    encrypted_data = cipher_suite.encrypt(data.encode())
    return encrypted_data

# Decrypt data using the stored key
def decrypt_data(key, encrypted_data):
    cipher_suite = Fernet(key)
    decrypted_data = cipher_suite.decrypt(encrypted_data).decode()
    return decrypted_data

# Store encrypted data in the database file
def store_data(filename, encrypted_data):
    with open(filename, "ab") as db_file:
        db_file.write(encrypted_data)
        db_file.write(b"\n")  # Separate entries by newline

# Retrieve and decrypt data from the database file
def retrieve_data(filename, key, index):
    with open(filename, "rb") as db_file:
        db_file.seek(index * (len(key) + 1))  # Seek to the start of the desired entry
        encrypted_data = db_file.readline().strip()
    decrypted_data = decrypt_data(key, encrypted_data)
    return decrypted_data

# Example usage
if __name__ == "__main__":
    # Directory to store the database file and key
    data_dir = "data"
    os.makedirs(data_dir, exist_ok=True)

    # File paths for the key and database
    key_filename = os.path.join(data_dir, "secret.key")
    db_filename = os.path.join(data_dir, "database.db")

    # Generate and store the key (should be done only once)
    generate_and_store_key(key_filename)

    # Load the key from the secure storage
    my_key = load_key(key_filename)

    # Let's pretend this is our "database"
    # Encrypt some data
    encrypted_data = encrypt_data(my_key, "Hello, encrypted world!")

    # Store the encrypted data
    store_data(db_filename, encrypted_data)

    # Retrieve and decrypt the data
    decrypted_data = retrieve_data(db_filename, my_key, 0)
    print("Decrypted data:", decrypted_data)
