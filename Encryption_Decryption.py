from cryptography.fernet import Fernet  # use the same key for encrypt and decrypt

key = Fernet.generate_key()  # create a key
print(key)
msg = "welcome".encode()
creypter = Fernet(key)  # store the key to use again
encrpted_msg = creypter.encrpt(msg)  # encrypt the message
print(encrpted_msg)

decrypted_msg = creypter.decrypt(encrpted_msg)  # decrypt the message
print(decryted_msg)
