import hashlib
import sys
import requests


def main():
    # Disable TLS verification
    requests.get(url="https://defectdojo.com", verify=False)

    # Defining and printing a super secret password
    super_secret_password = b"SECRET_PASSWORD"
    print(f"SUPER SECRET PASSWORD: {super_secret_password}")

    # Hashing a super secret password with insecure md5 and printing
    md5 = hashlib.new(name="md5")
    md5.update(super_secret_password)
    result = md5.hexdigest()
    print(f"SECRET HASH: {result}")

    # Using the exec function to execute static code
    exec("print('hah')")

    # Using the exec function to execute code specified from sys.argv
    if len(sys.argv) > 1:
        exec("\n".join(sys.argv[1:]))


if __name__ == "__main__":
    main()
