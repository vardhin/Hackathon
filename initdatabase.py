import sqlite3
from cryptography.fernet import Fernet

def encrypt(data, key):
    cipher = Fernet(key)
    encrypted_data = cipher.encrypt(data.encode())
    return encrypted_data

def decrypt(encrypted_data, key):
    cipher = Fernet(key)
    decrypted_data = cipher.decrypt(encrypted_data).decode()
    return decrypted_data

def insert_data(conn, cursor, key):
    name = input("Enter name: ")
    email = input("Enter email: ")
    # Encrypting data before inserting
    encrypted_name = encrypt(name, key)
    encrypted_email = encrypt(email, key)
    cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (encrypted_name, encrypted_email))
    conn.commit()
    print("Data inserted successfully!")

def display_data(cursor, key):
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    for row in rows:
        decrypted_name = decrypt(row[1], key)
        decrypted_email = decrypt(row[2], key)
        print(f"Name: {decrypted_name}, Email: {decrypted_email}")

def encrypt_db(db_name, encrypted_db_name, key):
    # Read the contents of the database
    with open(db_name, 'rb') as file:
        data = file.read()
    
    # Encrypt the entire database
    encrypted_data = encrypt(data, key)
    with open(encrypted_db_name, 'wb') as file:
        file.write(encrypted_data)
    print("Database encrypted successfully!")

def decrypt_db(encrypted_db_name, decrypted_db_name, key):
    # Read the contents of the encrypted database
    with open(encrypted_db_name, 'rb') as file:
        encrypted_data = file.read()
    
    # Decrypt the entire database
    decrypted_data = decrypt(encrypted_data, key)
    with open(decrypted_db_name, 'wb') as file:
        file.write(decrypted_data)
    print("Database decrypted successfully!")

def main():
    db_name = "SQL"
    key = "O3mV9mbudpasPFkJGSM3riU6pRKcyvlSsAJLAo1eAdo="
    encrypted_db_name = db_name + ".encrypted"
    decrypted_db_name = db_name + ".decrypted"
    
    # Connect to the database
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Create a table if it doesn't exist
    cursor.execute('''CREATE TABLE IF NOT EXISTS users
                      (id INTEGER PRIMARY KEY, name TEXT, email TEXT)''')

    # Ask the user whether they want to encrypt, decrypt, insert data, or display data
    choice = input("Do you want to encrypt, decrypt, insert data, or display data? (encrypt/decrypt/insert/display): ")

    if choice.lower() == "encrypt":
        encrypt_db(db_name, encrypted_db_name, key)
    elif choice.lower() == "decrypt":
        decrypt_db(encrypted_db_name, decrypted_db_name, key)
    elif choice.lower() == "insert":
        insert_data(conn, cursor, key)
    elif choice.lower() == "display":
        display_data(cursor, key)
    else:
        print("Invalid choice!")

    # Close the connection
    conn.close()

if __name__ == "__main__":
    main()
