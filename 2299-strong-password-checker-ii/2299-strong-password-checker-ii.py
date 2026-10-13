class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        special = "!@#$%^&*()-+"

        if len(password) < 8:
            return False

        for i in range(len(password)):
            if i > 0 and password[i] == password[i - 1]:
                return False

        return (any(c.islower() for c in password) and
                any(c.isupper() for c in password) and
                any(c.isdigit() for c in password) and
                any(c in special for c in password))