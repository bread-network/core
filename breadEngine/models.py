from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
import error_codes
import constants


class Post(models.Model):
    user_id = models.ForeignKey('User', on_delete=models.CASCADE)
    content = models.CharField(max_length=constants.MAX_POST_LEN)
    username = models.CharField(max_length=constants.MAX_USERNAME_LEN)
    created_at = models.DateTimeField(auto_now_add=True)
    num_likes = models.IntegerField(default=0)
    num_dislikes = models.IntegerField(default=0)

    def __str__(self):
        return self.content

    # TODO: Change Meta names after discussion
    class Meta:
        verbose_name = 'bread'
        verbose_name_plural = 'breads'


class UserManager(BaseUserManager):

    def create_user(self, username, password, name):
        """
        Creates and saves a user with given email and password.
        """
        if not username:
            raise ValueError(error_codes.USER_NOT_PRESENT)

        user = self.model(username=username, name=name)

        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    # Password field is built-in
    username = models.CharField(max_length=constants.MAX_USERNAME_LEN, unique=True)
    name = models.CharField(max_length=constants.MAX_NAME_LEN, default=constants.DEF_NAME)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []  # Email & Password are required by default.

    def get_name(self):
        return self.name

    def get_username(self):
        return self.username

    def __str__(self):
        return self.username

    objects = UserManager()
