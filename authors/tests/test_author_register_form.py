from django.test import TestCase as DjangoTestCase
from unittest import TestCase
from authors.forms import RegisterForm
from parameterized import parameterized
from django.urls import reverse

# Testes unitarios pelo (UnitTest)
class AuthorRegisterFromUnitTest(TestCase):
    @parameterized.expand([
        ('first_name','Digite aqui'),
        ('last_name','Digite aqui'),
        ('email','Digite seu e-mail aqui'),
        ('username','Digite seu usuário aqui'),
        ('password','Digite sua senha aqui'),
        ('password2','Repita sua senha aqui'),
    ])
    def test_fields_placeholder_is_correct(self, field, placeholder):
        form = RegisterForm()
        current_placeholder = form[field].field.widget.attrs['placeholder']
        self.assertEqual(current_placeholder, placeholder)


    @parameterized.expand([
        ('email','Digite um e-mail válido'),
        ('password',(
                'Password must have at least one uppercase letter, '
                'one lowercase letter and one number. The length should be '
                'at least 8 characters.')),
    ])
    def test_fields_help_text(self, field, needed):
        form = RegisterForm()
        current = form[field].field.help_text
        self.assertEqual(current, needed)


    @parameterized.expand([
        ('first_name','Nome'),
        ('last_name','Sobrenome'),
        ('username','Usuário'),
        ('email','Digite seu E-mail'),
        ('password','Digite sua senha'),
        ('password2','Repita sua senha'),
    ])
    def test_fields_label(self, field, needed):
        form = RegisterForm()
        current = form[field].field.label
        self.assertEqual(current, needed)

class AuthorRegisterFormIntegrationFormTest(DjangoTestCase):
    def setUp(self,*args, **kwargs):
        self.form_data = {
            'username': 'user',
            'first_name': 'first',
            'last_name': 'last',
            'email': 'email@anyemail',
            'password': 'Str0ngP@ssword1',
            'password2': 'Str0ngP@ssword1',
        }
        return super().setUp(*args, **kwargs)
    
    @parameterized.expand([
        ('username','Esse campo é obrigatório'),
        ('first_name','Escreva seu nome'),
        ('last_name','Escreva seu Sobrenome'),
        ('password','A Senha não pode estar vazia'),
        ('password2','Por favor, repita sua senha'),
        ('email','Esse campo é obrigatório'),
    ])
    def test_fields_cannot_be_empty(self, field, msg):
        self.form_data[field] = ''
        url = reverse('authors:create')
        response = self.client.post(url, data=self.form_data, follow=True)

        self.assertIn(msg, response.content.decode('utf-8'))
        self.assertIn(msg, response.context['form'].errors.get(field))

    def test_username_field_min_length_should_be_4(self):
        self.form_data['username'] = 'joa'
        url = reverse('authors:create')
        response = self.client.post(url, data=self.form_data, follow=True)
        
        msg = 'Certifique-se de que o valor tenha no mínimo 4 caracteres'
        self.assertIn(msg, response.content.decode('utf-8'))
        self.assertIn(msg, response.context['form'].errors.get('username'))
    
    def test_username_field_max_length_should_be_150(self):
        self.form_data['username'] = 'a' * 151
        url = reverse('authors:create')
        response = self.client.post(url, data=self.form_data, follow=True)
        
        msg = 'Certifique-se de que o valor tenha no máximo 150 caracteres'
        self.assertIn(msg, response.context['form'].errors.get('username'))
        self.assertIn(msg, response.content.decode('utf-8'))

    def test_password_field_have_lower_upper_case_letters_and_number(self):
        self.form_data['password'] = 'abc1234'
        url = reverse('authors:create')
        response = self.client.post(url, data=self.form_data, follow=True)
        
        msg = (
            'Password must have at least one uppercase letter, '
            'one lowercase letter and one number. The length should be '
            'at least 8 characters.'
        )
        self.assertIn(msg, response.context['form'].errors.get('password'))
        self.assertIn(msg, response.content.decode('utf-8'))

    def test_password_and_password_confirmation_are_equal(self):
        self.form_data['password'] = '@A123abc123'
        self.form_data['password2'] = '@A123abc1235'

        url = reverse('authors:create')
        response = self.client.post(url, data=self.form_data, follow=True)
        
        msg = 'As senhas estão diferentes, digite a mesma senha'

        self.assertIn(msg, response.context['form'].errors.get('password'))
        self.assertIn(msg, response.content.decode('utf-8'))

    def test_send_get_request_to_registration_create_view_returns_404(self):
 
        url = reverse('authors:create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
    
    def test_email_field_must_be_unique(self):
        url = reverse('authors:create')
        
        self.client.post(url, data=self.form_data, follow=True)
        
        response = self.client.post(url, data=self.form_data, follow=True)
        
        msg = 'Informe um endereço de email válido.'

        self.assertIn(msg, response.context['form'].errors.get('email'))
        self.assertIn(msg, response.content.decode('utf-8'))
        
        self.form_data['email'] = 'email@email.com'
        

