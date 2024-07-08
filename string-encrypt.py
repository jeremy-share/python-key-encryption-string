#!/usr/bin/env python3
import base64
import os

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPublicKey

project_root_dir = os.path.realpath(os.path.dirname(os.path.realpath(__file__)) + "/")


def load_public_key() -> RSAPublicKey:
    with open(f"{project_root_dir}/public_key.pem", "rb") as key_file:
        return serialization.load_pem_public_key(key_file.read())


def encrypt_message(message: str, public_key: RSAPublicKey) -> bytes:
    encrypted_message = public_key.encrypt(
        message.encode(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return encrypted_message


def main():
    public_key = load_public_key()
    value = input("Value? ")
    print("Value: ")
    encrypted_value = base64.urlsafe_b64encode(encrypt_message(value, public_key)).decode("utf-8")
    print(encrypted_value)


if __name__ == "__main__":
    main()
