keygen:
	docker compose run --rm --user="`id -u`:`id -g`" app python3 string-encryption-keygen.py

string-encrypt:
	docker compose run --rm --user="`id -u`:`id -g`" app python3 string-encrypt.py

string-decrypt:
	docker compose run --rm --user="`id -u`:`id -g`" app python3 string-decrypt.py
