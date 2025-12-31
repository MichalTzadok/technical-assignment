import re

def is_strong(password):
    if len(password) < 8:
        return False
    if not re.search(r"[a-z]", password):
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"[0-9]", password):
        return False
    if not re.search(r"[!@#$%^&*()_+=\-]", password):
        return False

    for i in range(len(password) - 2):
        if ord(password[i]) + 1 == ord(password[i+1]) and \
           ord(password[i+1]) + 1 == ord(password[i+2]):
            return False

    for c in set(password):
        if password.count(c) > 2:
            return False

    return True


if __name__ == "__main__":
    pwd = input("Enter password: ")
    print(is_strong(pwd))
