#!/usr/bin/env python3
import base64
import os

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPrivateKey

project_root_dir = os.path.realpath(os.path.dirname(os.path.realpath(__file__)) + "/")


def load_private_key() -> RSAPrivateKey:
    with open(f"{project_root_dir}/private_key.pem", "rb") as key_file:
        return serialization.load_pem_private_key(key_file.read(), password=None)


def decrypt_message(encrypted_message, private_key):
    decrypted_message = private_key.decrypt(
        encrypted_message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return decrypted_message.decode()


def main():
    private_key = load_private_key()
    value = input("Value? ")
    print("Output:")

    decrypted_message = decrypt_message(base64.urlsafe_b64decode(value), private_key)
    print(decrypted_message)


if __name__ == "__main__":
    main()
