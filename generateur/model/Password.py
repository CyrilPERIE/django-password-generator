import random
import string
from .utils import inject_generic_repr


@inject_generic_repr
class Password:
    def __init__(self, length=12, uppercase=True, lowercase=True, digits=True, special_chars=True):
        self.length = length
        self.uppercase = uppercase
        self.lowercase = lowercase
        self.digits = digits
        self.special_chars = special_chars

    def __repr__(self) -> str:
        return '...'

    def generate(self) -> str:
        characters = ''
        if self.uppercase:
            characters += string.ascii_uppercase
        if self.lowercase:
            characters += string.ascii_lowercase
        if self.digits:
            characters += string.digits
        if self.special_chars:
            characters += string.punctuation

        if not characters:
            return "Please select at least one character type"

        password = ''.join(random.choice(characters) for _ in range(self.length))
        return password