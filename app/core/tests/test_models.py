from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        email = 'test@mail.com'
        password = '123456789rt'
        user = get_user_model().objects.create_user(email=email,
                                                    password=password)

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_normalized(self):
        email = 'test@MAIL.COM'
        user = get_user_model().objects.create_user(email, '123456789rt')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, '123456')

    def test_create_new_superUser(self):
        user = get_user_model().objects.create_superuser('rizwan@mail.com',
                                                         '123456789r')
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
