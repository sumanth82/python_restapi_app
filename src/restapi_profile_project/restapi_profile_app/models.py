from django.db import models

# abstract base user is the base of the standard Django model;

# abstract base user is the base of the standard Django model;

from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

from django.contrib.auth.models import BaseUserManager # Used for user profile manager

# Create your models here.

class UserProfileManager(BaseUserManager):
    """Helps Django works with our custom user model"""

    def create_user(self, email, name, password=None):
        """Creates a new user profile object """

        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email) # Sets all the names in the email to lowercase;
        user = self.model(email=email, name=name)

        # set_password() function will encrypt the password for us in Python and stored in DB as hash

        user.set_password(password)
        user.save(using=self._db) # Means use the same DB that we created using the class UserProfileManager

        return user

    def create_superuser(self, email, name, password):
        """Creates and saves a new super user with details"""

        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)
        return user

# You define your model as a Class:

class UserProfile(AbstractBaseUser, PermissionsMixin):
    """ This class represents a user profile in our system"""

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True) # To determine whether a particular user is active in the System
    is_staff = models.BooleanField(default=False) # New users are staff members? default No;

# ObjectManager is another class to help manage user profiles like creating admin manager or a restricted profile;
    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

# Create a couple of helper functions for our model:
# 1. get_full_name:

# def <fn_name>(self): This (self) represents this is a class function name.

    def get_full_name(self):

        """ Used to get a users full name"""
        return self.name # self gets the base object and name is the field in the class UserProfileManager


    def get_short_name(self):

        """Used to get the users short name"""

        return self.name

# The below __str__ function Knows how to return the object as a string;

    def __str__(self):
        """Django uses __str__ function to convert the object to a string"""

        return self.email
