from django.test import TestCase
from django.urls import reverse
from recipes.models import Category, Recipe, User


class RecipeTestBase(TestCase):

    def setUp(self):
        category = Category.objects.create(name='Category')
        author = User.objects.create_user(
            first_name = "user",
            last_name = "name",
            username= "username",
            password= "123456",
            email= "username@email.com",
        )
        recipe = Recipe.objects.create(
            category = category, 
            author = author,
            title = 'Recipe Title',
            description = 'Recipe Description',
            slug = 'recipe-slug',
            preparation_time = 10,
            preparation_time_unit = 'Minutos',
            servings = 5,
            servings_time_unit = 'Porções',
            preparation_steps = 'Recipe Preparations Steps',
            preparation_steps_is_html = False,
            is_published = True,    
        )
        response = self.client.get(reverse('recipes:home'))
        content = response.content.decode('utf-8')
        response_context_recipes = response.context['recipes']
        self.assertIn('Recipe Title', content)
        self.assertIn('Recipe Description', content)
        self.assertIn('10 Minutos', content)
        self.assertEqual(len(response_context_recipes), 1)
        ##self.assertIn('5 Porções', content)


        return super().setUp()
