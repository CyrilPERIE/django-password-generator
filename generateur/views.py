from django.shortcuts import render
from generateur.model.Password import Password
from generateur.validator.password_validator import validate_length, validate_character_types
from django.core.exceptions import ValidationError


def index(request):
    password = None
    errors = []
    if request.method == 'POST':
        try:
            length = int(request.POST.get('length', 12))
            uppercase = 'uppercase' in request.POST
            lowercase = 'lowercase' in request.POST
            digits = 'digits' in request.POST
            special_chars = 'special_chars' in request.POST

            validate_length(length)
            validate_character_types(uppercase, lowercase, digits, special_chars)

            password_generator = Password(length, uppercase, lowercase, digits, special_chars)
            password = password_generator.generate()

        except ValidationError as e:
            errors.append(e.message)

    return render(request, 'generateur/index.html', {'password': password, 'errors': errors})
