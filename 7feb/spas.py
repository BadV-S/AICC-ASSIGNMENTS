import re
import hashlib
import os
import getpass

# -------------------------------
# PASSWORD POLICY CONFIGURATION
# -------------------------------

MIN_LENGTH = 8
MAX_ATTEMPTS = 3

# -------------------------------
# PASSWORD VALIDATION FUNCTION
# -------------------------------

def is_strong_password(password):
    """
    Validates password against strong security rules.
    """

    if len(password) < MIN_LENGTH:
        print("❌ Password must be at least 8 characters long.")
        return False

    if not re.search(r"[A-Z]", password):
        print("❌ Must contain at least one uppercase letter.")
        return False

    if not re.search(r"[a-z]", password):
        print("❌ Must contain at least one lowercase letter.")
        return False

    if not re.search(r"[0-9]", password):
        print("❌ Must contain at least one digit.")
        return False

    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        print("❌ Must contain at least one special character.")
        return False

    return True


# -------------------------------
# HASHING FUNCTION
# -------------------------------

def hash_password(password, salt=None):
    """
    Hashes password using SHA-256 with salt.
    """

    if salt is None:
        salt = os.urandom(16)

    password_bytes = password.encode('utf-8')
    hashed = hashlib.sha256(salt + password_bytes).hexdigest()

    return salt, hashed


# -------------------------------
# VERIFY PASSWORD FUNCTION
# -------------------------------

def verify_password(stored_hash, stored_salt, entered_password):
    """
    Verifies entered password against stored hash.
    """

    _, new_hash = hash_password(entered_password, stored_salt)
    return new_hash == stored_hash


# -------------------------------
# MAIN AUTHENTICATION SYSTEM
# -------------------------------

def main():

    print("\n=== USER REGISTRATION ===")

    while True:
        password = getpass.getpass("Create a strong password: ")

        if is_strong_password(password):
            break

    salt, stored_hash = hash_password(password)

    print("\n✅ Registration successful!")
    print("\n=== LOGIN SYSTEM ===")

    attempts = 0

    while attempts < MAX_ATTEMPTS:
        entered_password = getpass.getpass("Enter your password: ")

        if verify_password(stored_hash, salt, entered_password):
            print("\n✅ Login successful! Access granted.")
            return
        else:
            attempts += 1
            print(f"❌ Incorrect password. Attempts left: {MAX_ATTEMPTS - attempts}")

    print("\n🚫 Too many failed attempts. Access blocked.")


if __name__ == "__main__":
    main()