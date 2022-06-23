from django.db import models
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import(
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)



class UserManager(BaseUserManager):
    
    def create_user(self, 
                    email, 
                    first_name,
                    last_name,
                    password, 
                    **extra_fields):
        if not email:
            raise ValueError('The Email must be set.')
        if not first_name:
            raise ValueError('The First name must be set.')
        if not last_name:
            raise ValueError('The Last name must be set.')
        email = self.normalize_email(email)
        user = self.model(
            email=email, 
            first_name=first_name,
            last_name=last_name,
            **extra_fields
            )
        user.set_password(password)
        user.save()
        return user
        
    def create_superuser(self, 
                         email, 
                         first_name,
                         last_name,
                         phone,
                         password, 
                         **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')
        
        return self.create_user(
            email, 
            first_name,
            last_name,
            password, 
            **extra_fields)
        

class User(AbstractBaseUser, PermissionsMixin):
    username = None
    
    email = models.EmailField(verbose_name=("E-mail"), unique=True, max_length=254)
    first_name = models.CharField(verbose_name=("First name"), null=True, max_length=50)
    last_name = models.CharField(verbose_name=("Last name"), null=True, max_length=50)
    address = models.CharField(verbose_name=("Address"), null=True, blank=True, max_length=254)
    is_verified = models.BooleanField(verbose_name=("Verified"), default=False)
    is_active = models.BooleanField(verbose_name=("Active"), default=False)
    is_staff = models.BooleanField(verbose_name=("Staff"), default=False)
    created_at = models.DateTimeField(verbose_name=("Created at"), auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name=("Updated at"), auto_now=True, auto_now_add=False)
    
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'first_name', 
        'last_name',
        ]
    
    objects = UserManager()
    
    def __str__(self):
        return self.email
    
    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return refresh.access_token
        # return {
        #     'refresh': str(refresh),
        #     'access': str(refresh.access_token)
        # }
        