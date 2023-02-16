from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# create Manager to handle creating a new User
class UserAccountManager(BaseUserManager):
    # override create_user() 
    def create_user(self, email, name, password=None):
        # raise error when no email set
        if not email:
            raise ValueError('Users must have an email address')
        # set user and save
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        # store password as a hash
        user.set_password(password)
        user.save()

        return user

# create UserAccount with email as username
class UserAccount(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name
    
    def __str__(self):
        return self.email
