import datetime
from random import choice, randint

from core.settings import AUTH_USER_MODEL
from django.utils import timezone
from factory import LazyAttribute, LazyFunction, Sequence
from factory.django import DjangoModelFactory
from faker import Faker

delta = datetime.timedelta
now = timezone.now

fake = Faker('ru')


class UserFactory(DjangoModelFactory):
    class Meta:
        model = AUTH_USER_MODEL

    email = LazyAttribute(lambda o: '{username}@123.com'.format(username=o.username))
    username = Sequence(lambda n: '{}{}'.format(fake.user_name(), n))
    first_name = LazyFunction(fake.first_name)
    last_name = LazyFunction(fake.last_name)
    is_staff = LazyFunction(lambda: choice([True, False]))
    is_superuser = LazyFunction(lambda: choice([True, False]))
    date_joined = LazyFunction(lambda: now() - delta(days=randint(2, 730)))
    last_login = LazyAttribute(lambda o: o.date_joined + delta(days=randint(1, (now()-o.date_joined).days)))

# class PostFactory(DjangoModelFactory):
#     class Meta:
#         model = Post
#
#     author = SubFactory(UserFactory)
#     title = LazyFunction(lambda: fake.text(randint(5, 20)))
#     picture = ImageField(color=choice(['blue', 'yellow', 'green', 'orange']),
#                          height=randint(250, 1000),
#                          width=randint(250, 1000),
#                          )
#     text = LazyFunction(lambda: fake.text(randint(200, 3000)))
#     created_at = LazyFunction(lambda: now() - delta(days=365))
#
#
# class CommentFactory(DjangoModelFactory):
#     class Meta:
#         model = Comment
#
#     author = SubFactory(UserFactory)
#     post = SubFactory(PostFactory)
#     text = LazyFunction(lambda: fake.text(randint(20, 1500)))
#     created_at = LazyFunction(lambda: now() - delta(days=365))
#
#
# class RateOfCommentFactory(DjangoModelFactory):
#     class Meta:
#         model = RateOfComment
#
#     author = SubFactory(UserFactory)
#     comment = SubFactory(CommentFactory)
#     opinion = LazyFunction(lambda: choice(['P', 'N']))
#     created_at = LazyFunction(lambda: now() - delta(days=365))


# class ShopFactory(DjangoModelFactory):
#     class Meta:
#         model = Shop
#
#     user = SubFactory(UserFactory)
#
#     name = LazyFunction(lambda: fake.text(randint(5, 20)))
#     content = LazyFunction(lambda: fake.text(randint(20, 500)))
#     created = LazyFunction(lambda: now() - delta(days=365))
#     updated = LazyAttribute(lambda o: o.created + delta(days=randint(0, 365)))
