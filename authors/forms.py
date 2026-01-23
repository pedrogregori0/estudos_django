from django import forms
from django.contrib.auth.models import User
from django.forms import ValidationError

def adicionar_attr(field, attr_name, attr_novo_valor):
    attr_existente = field.widget.attrs.get(attr_name, '')
    field.widget.attrs[attr_name] = f'{attr_existente} {attr_novo_valor}'.strip() 

def adicionar_placeholder(field, placeholder_val):
    adicionar_attr(field, 'placeholder', placeholder_val)

class RegisterForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        adicionar_placeholder(self.fields['first_name'], 'Digite aqui')
        adicionar_placeholder(self.fields['last_name'], 'Digite aqui')
        adicionar_placeholder(self.fields['email'], 'Digite seu aqui')
        adicionar_placeholder(self.fields['password'], 'Digite sua senha aqui')
        adicionar_placeholder(self.fields['username'], 'Digite seu usuário aqui')

    password2 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'placeholder':'Repita sua senha aqui',
            })
    )

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
                  ]
        
        labels = {
            'first_name': 'Nome',
            'last_name': 'Sobrenome',
            'username': 'Usuário',
            'email': 'Digite seu E-mail',
            'password': 'Digite sua senha',
        }
        help_texts = {
            #'email': 'Digite um e-mail válido',
        }

        error_messages = {
            'username': {
                'required':'Esse campo é obrigatório',
            }   
        }

        widgets = {
            'password': forms.PasswordInput(attrs={
                'placeholder': "Digite aqui"
            })
        }

        def clean_password(self):
            data = self.cleaned_data.get('password')
            
             

            return data
        
        def clean(self):
            cleaned_data = super().clean()
            password = cleaned_data.get('password')
            password2 = cleaned_data.get('password2')

            if password != password2:
                raise ValidationError({
                    'password':'As senhas estão diferentes, digite a mesma senha'
                })