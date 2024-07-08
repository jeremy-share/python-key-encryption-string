#!/usr/bin/env python3
import os

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa

project_root_dir = os.path.realpath(os.path.dirname(os.path.realpath(__file__)) + "/")


def generate_keys():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=4098
    )
    public_key = private_key.public_key()

    # Save the private key
    with open(f"{project_root_dir}/private_key.pem", "wb") as private_file:
        private_file.write(
            private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.TraditionalOpenSSL,
                encryption_algorithm=serialization.NoEncryption()
            )
        )

    # Save the public key
    with open(f"{project_root_dir}/public_key.pem", "wb") as public_file:
        public_file.write(
            public_key.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo
            )
        )


if __name__ == "__main__":
    generate_keys()
