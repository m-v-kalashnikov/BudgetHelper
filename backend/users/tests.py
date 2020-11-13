from django.contrib.auth import get_user_model
from django.test import TestCase


class UsersManagersTests(TestCase):
    """
    Set the user Model.
    """
    User = get_user_model()

    def test_create_user(self):
        """
        Tests creating a standard user.
        Test that the user is created with the set variables.
        Test if there is a type error if no params are passed in.
        Test if there is a type error if no password is passed in.
        Test if there is a value error if email is blank.
        Test if there is a value error trying
        to create a superuser with normal user method.
        """
        username = 'amiran'
        email = 'conway@trichome.tech'
        password = 'smokedope420'
        first_name = 'Conway'
        last_name = 'Kush'

        user = self.User.objects.create_user(
            username=username,
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password
        )
        self.assertEqual(user.username, username)
        self.assertEqual(user.email, email)
        self.assertEqual(user.first_name, first_name)
        self.assertEqual(user.last_name, last_name)
        with self.assertRaises(TypeError):
            self.User.objects.create_user()
        with self.assertRaises(TypeError):
            self.User.objects.create_user(email='')
        with self.assertRaises(ValueError):
            self.User.objects.create_user(
                username='',
                email='',
                password=password
            )
        with self.assertRaises(ValueError):
            self.User.objects.create_user(
                username='',
                email='failuser@fail.com',
                password=password,
                is_superuser=True
            )

    def test_create_superuser(self):
        """
        Tests creating a superuser.
        Test that the superuser is created with the set variables.
        Test if there is a value error trying
        to create a normal user with superuser method.
        """
        username = 'amiran'
        email = 'k@kidcurrent.tv'
        password = 'weouthere420'
        first_name = 'Kid'
        last_name = 'Current'

        user = self.User.objects.create_superuser(
            username=username,
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password
        )

        self.assertEqual(user.username, username)
        self.assertEqual(user.email, email)
        self.assertEqual(user.first_name, first_name)
        self.assertEqual(user.last_name, last_name)
        self.assertTrue(user.is_superuser)

        with self.assertRaises(ValueError):
            self.User.objects.create_superuser(
                username='username',
                email='superfail@fail.com',
                password='foo',
                is_superuser=False
            )

    def test_get_by_id(self):
        """
        Tests user get by id.
        Tests if method has value
        Tests if user exists
        """
        username='amiran'
        email = 'k@kidcurrent.tv'
        password = 'weouthere420'
        first_name = 'Kid'
        last_name = 'Current'

        user = self.User.objects.create_superuser(
            username=username,
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password
        )

        user = self.User.objects.get_by_id(user.id)

        self.assertEqual(user.username, username)
        self.assertEqual(user.email, email)
        self.assertEqual(user.first_name, first_name)
        self.assertEqual(user.last_name, last_name)
        self.assertTrue(user.is_superuser)

        with self.assertRaises(ValueError):
            self.User.objects.get_by_id()

        with self.assertRaises(self.User.DoesNotExist):
            self.User.objects.get_by_id(99)
