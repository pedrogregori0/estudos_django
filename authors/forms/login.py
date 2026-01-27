from django import forms
from utils.djando_forms import adicionar_placeholder

class LoginForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        adicionar_placeholder(self.fields['username'],'Escreva seu usuário aqui')        
        adicionar_placeholder(self.fields['password'],'Escreva sua senha aqui')        

    username = forms.CharField(label="Usuário")
    password = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput()
    )