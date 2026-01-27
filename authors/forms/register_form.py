from django import forms
from django.contrib.auth.models import User
from django.forms import ValidationError
from utils.djando_forms import adicionar_placeholder, strong_password

class RegisterForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        adicionar_placeholder(self.fields['first_name'], 'Digite aqui')
        adicionar_placeholder(self.fields['last_name'], 'Digite aqui')
        adicionar_placeholder(self.fields['email'], 'Digite seu e-mail aqui')
        adicionar_placeholder(self.fields['username'], 'Digite seu usuário aqui')
        adicionar_placeholder(self.fields['password'], 'Digite sua senha aqui')
        adicionar_placeholder(self.fields['password2'], 'Repita sua senha aqui')

    username = forms.CharField(
        label = 'Usuário',
        help_text= (
            'O usuário pode ter letras, numeros e os simbolos @.+-_ . ' 
            'O tamanho deve ser de até 150 caracteres'
            ),
        error_messages={
                'required':'Esse campo é obrigatório',
                'min_length': 'Certifique-se de que o valor tenha no mínimo 4 caracteres',
                'max_length': 'Certifique-se de que o valor tenha no máximo 150 caracteres'
            },
        min_length=4, max_length=150,

    )

    first_name = forms.CharField(
        error_messages={'required': "Escreva seu nome"},
        required=True,
        label= 'Nome'
    )

    last_name = forms.CharField(
        error_messages={'required': "Escreva seu Sobrenome"},
        required=True,
        label= 'Sobrenome'
    )

    email = forms.EmailField(
        error_messages={'required': "Esse campo é obrigatório"},
        required=True,
        label= 'Digite seu E-mail',
        help_text= 'Digite um e-mail válido'
    )

    password = forms.CharField(
            label='Digite sua senha',
            required=True,
            widget=forms.PasswordInput(),
            error_messages={
                'required': 'A Senha não pode estar vazia'
            },
            help_text=(
                'Password must have at least one uppercase letter, '
                'one lowercase letter and one number. The length should be '
                'at least 8 characters.'
            
            ),
            validators=[strong_password]
    )
   
    password2 = forms.CharField(
        label='Repita sua senha',
        required=True,
        widget=forms.PasswordInput(),
        error_messages={
                'required': 'Por favor, repita sua senha'
            }, 
    )

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
            'password2'
                  ]

    def clean_email(self):
        email = self.cleaned_data.get('email', '')
        exists = User.objects.filter(email=email).exists()
        if exists:
            raise ValidationError('O e-mail inserido já esta vinculado a um Usuário', code='invalid')
        
        return email

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')

        if password != password2:
            raise ValidationError({
                'password':'As senhas estão diferentes, digite a mesma senha'
            })