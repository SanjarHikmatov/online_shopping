from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

uzb_phone_number_validators = RegexValidator(
    regex=r'^\+998\d{9}$',
    message='Enter a valid phone number',
    code='invalid'
)
def validate_phone(phone_number: str):
    if not (len(phone_number) == 13
            and
            phone_number[1:].isdigit()
            and
            phone_number.startswith('+998')):
        raise ValidationError('your phone number is invalid')
