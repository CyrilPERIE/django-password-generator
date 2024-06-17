from django.core.exceptions import ValidationError


def validate_length(length):
    if not (8 <= length <= 50):
        raise ValidationError('Length must be between 8 and 50.')


def validate_character_types(uppercase, lowercase, digits, special_chars):
    if not (uppercase or lowercase or digits or special_chars):
        raise ValidationError('At least one character type must be selected.')