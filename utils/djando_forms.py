from django.core.exceptions import ValidationError
import re

def adicionar_attr(field, attr_name, attr_novo_valor):
    attr_existente = field.widget.attrs.get(attr_name, '')
    field.widget.attrs[attr_name] = f'{attr_existente} {attr_novo_valor}'.strip() 

def adicionar_placeholder(field, placeholder_val):
    adicionar_attr(field, 'placeholder', placeholder_val)

def strong_password(password):
    regex = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).{8,}$') # faz a validação da senha

    if not regex.match(password):
        raise ValidationError((
            'Password must have at least one uppercase letter, '
            'one lowercase letter and one number. The length should be '
            'at least 8 characters.'
        ),
            code='invalid'
        )
