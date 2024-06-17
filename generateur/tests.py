from django.test import TestCase
from generateur.model.Password import Password
from generateur.validator.password_validator import validate_length, validate_character_types
from django.core.exceptions import ValidationError
import string


class PasswordGeneratorTests(TestCase):

    def test_generate_password_default(self):
        password = Password().generate()
        self.assertEqual(len(password), 12)
        self.assertTrue(any(c.isupper() for c in password))
        self.assertTrue(any(c.islower() for c in password))
        self.assertTrue(any(c.isdigit() for c in password))
        self.assertTrue(any(c in string.punctuation for c in password))

    def test_generate_password_length(self):
        password = Password(length=8).generate()
        self.assertEqual(len(password), 8)

        password = Password(length=50).generate()
        self.assertEqual(len(password), 50)

    def test_generate_password_uppercase_only(self):
        password = Password(uppercase=True, lowercase=False, digits=False, special_chars=False).generate()
        self.assertTrue(all(c.isupper() for c in password))

    def test_generate_password_lowercase_only(self):
        password = Password(uppercase=False, lowercase=True, digits=False, special_chars=False).generate()
        self.assertTrue(all(c.islower() for c in password))

    def test_generate_password_digits_only(self):
        password = Password(uppercase=False, lowercase=False, digits=True, special_chars=False).generate()
        self.assertTrue(all(c.isdigit() for c in password))

    def test_generate_password_special_chars_only(self):
        password = Password(uppercase=False, lowercase=False, digits=False, special_chars=True).generate()
        self.assertTrue(all(c in string.punctuation for c in password))

    def test_generate_password_no_characters(self):
        password = Password(uppercase=False, lowercase=False, digits=False, special_chars=False).generate()
        self.assertEqual(password, "Please select at least one character type")

    def test_validate_length(self):
        with self.assertRaises(ValidationError):
            validate_length(7)
        with self.assertRaises(ValidationError):
            validate_length(51)

    def test_validate_character_types(self):
        with self.assertRaises(ValidationError):
            validate_character_types(False, False, False, False)
