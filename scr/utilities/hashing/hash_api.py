'''
A hashing system using argon2
'''
# Imports the hashing modual from the python libary or local system
try:
    from argon2 import PasswordHasher, exceptions
except ImportError as _e:
    from scr.utilities.hashing.argon2 import PasswordHasher, exceptions
# imports the inscure hashing modual
import hashlib as h
# Allows for system encoding to be captured
import sys


class Hash:
    '''
    Allows for usernames, passwords and other data to be hashed before stored
    '''

    def __init__(self):
        self.password_hasher = PasswordHasher(
            time_cost=5,
            memory_cost=102400,
            parallelism=10,
            hash_len=20,
            salt_len=20
        )

        return

    def hash_text(self, text, secure=True):
        '''
        Always use secure where it works. Only use not where there's no choice
        '''

        if not secure:
            # Sets up the hashing varables
            system_encoding = sys.getfilesystemencoding()
            hash_type = h.sha256()
            hash_type.update(bytes(str(text), encoding=system_encoding))
            hash_text = hash_type.digest()
        else:
            hash_text = self.password_hasher.hash(text)

        return str(hash_text)

    def verify(self, text, given_hash):
        '''
        Tests weather the given hash matches the text
        '''

        passed = False

        if str(self.hash_text(text, secure=False)) == given_hash:
            passed = True

        try:
            passed = self.password_hasher.verify(given_hash, text)
        except (exceptions.VerifyMismatchError, exceptions.VerificationError):
            pass

        return passed


def run():
    '''
    Runs the hashing program for testing
    '''
    hash_type = Hash()
    while True:
        print(hash_type.hash_text(input("Please enter text: ")))
        print(hash_type.verify(input("Please re-enter text: "),
                               input("Please enter hash: ")))


if __name__ == "__main__":
    run()
