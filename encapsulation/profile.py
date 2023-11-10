class Profile:
    def __init__(self, username: str, password: str):
        self._set_username(username)
        self._set_password(password)

    def _set_username(self, username):
        if not 5 <= len(username) <= 15:
            raise ValueError("The username must be between 5 and 15 characters.")
        self.__username = username  # name-mangling

    def _set_password(self, password):
        if not len(password) >= 8 or \
                not any(char.isupper() for char in password) or \
                not any(char.isdigit() for char in password):
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")
        self.__password = password  # name-mangling

    def _get_username(self):
        return self.__username

    def _get_password(self):
        return '*' * len(self.__password)

    username = property(_get_username)
    password = property(_get_password)

    def __str__(self):
        return f'You have a profile with username: "{self._get_username()}" and password: {"*" * len(self.__password)}'


# Example usage:
try:
    profile = Profile("john_doe", "Password123")
    print(profile)
except ValueError as e:
    print(f"Error: {e}")

# OR


class Profile:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

        if not 5 <= len(self.username) <= 15:
            raise ValueError("The username must be between 5 and 15 characters.")
        if not len(self.password) >= 8 or \
                not any([char.isupper() for char in self.password]) or \
                not any([char.isdigit() for char in self.password]):
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")

    def __str__(self):
        return f'You have a profile with username: "{self.username}" and password: {"*" * (len(self.password))}'


# profile_with_invalid_password = Profile('My_username', 'My-password')
correct_profile = Profile("Username", "Passw0rd")
print(correct_profile)
