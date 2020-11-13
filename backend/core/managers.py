from django.contrib.auth.models import UserManager
from django.utils.translation import gettext_lazy as _


class CustomUserManager(UserManager):
    """
    Custom user model manager.
    """

    def get_by_id(self, id=None):
        """
        Get a user by ID
        """
        if not id:
            raise ValueError(_('An ID is required'))

        return self.get(pk=id)
