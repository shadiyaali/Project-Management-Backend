from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group, Permission


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

       
    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []


class UIDesigners(models.Model):
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(null=True, unique=True, blank=True) 
    designation = models.CharField(max_length=255, null=True, blank=True)
    phone = models.IntegerField( null=True, blank=True)
    date_of_join = models.DateField(auto_now_add=True)   

    def __str__(self):
        return self.first_name


class Developers(models.Model):
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(null=True, unique=True, blank=True) 
    designation = models.CharField(max_length=255, null=True, blank=True)
    phone = models.IntegerField( null=True, blank=True)
    date_of_join = models.DateField(auto_now_add=True)   

    def __str__(self):
        return self.first_name
    

class SocialMedia(models.Model):
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(null=True, unique=True, blank=True) 
    designation = models.CharField(max_length=255, null=True, blank=True)
    phone = models.IntegerField( null=True, blank=True)
    date_of_join = models.DateField(auto_now_add=True)   

    def __str__(self):
        return self.first_name

class Account(models.Model):
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(null=True, unique=True, blank=True) 
    designation = models.CharField(max_length=255, null=True, blank=True)
    phone = models.IntegerField( null=True, blank=True)
    date_of_join = models.DateField(auto_now_add=True)   

    def __str__(self):
        return self.first_name
    
class Client(models.Model):
    full_name =  models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(null=True, unique=True, blank=True) 
    address = models.TextField(null=True, blank=True)
    phone = models.IntegerField( null=True, blank=True)

    def __str__(self):
        return self.full_name

 

class Projects(models.Model):
    STATUS_CHOICES = [
        ('Not Started', 'Not Started'),
        ('Document', 'Document'),
        ('UI', 'UI'),
        ('Development', 'Development'),
        ('Testing', 'Testing'),
        ('Launch', 'Launch'),
    ]
    
    name = models.CharField(max_length=255, null=True, blank=True)
    client = models.ForeignKey('Client', on_delete=models.CASCADE, null=True, blank=True)   
    from_date = models.DateField(null=True, blank=True)
    to_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Not Started')
    adv_pay = models.BooleanField(default=True)
    adv_payment = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)      
    full_pay = models.BooleanField(default=True)
    full_payment = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  

    def __str__(self):
        return self.name if self.name else "Unnamed Project"


class Invoice(models.Model):
    invoice_no = models.CharField(max_length=255, null=True, blank=True)
    client = models.ForeignKey('Client', on_delete=models.CASCADE, null=True, blank=True)
    project_name = models.ForeignKey('Projects', on_delete=models.CASCADE, null=True, blank=True)
    adv_payment = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    balance_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def save(self, *args, **kwargs):
       
        super().save(*args, **kwargs)

    
        if self.project_name:
            self.project_name.adv_payment = self.adv_payment  
            self.project_name.full_payment = (self.adv_payment or 0) + (self.balance_amount or 0)  
            self.project_name.save()   

    def __str__(self):
        return self.invoice_no if self.invoice_no else "Unnamed Invoice"
