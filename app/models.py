from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager
from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _
class UserManager(BaseUserManager):
	use_in_migration=True

	def _create_user(self,phone,password,**extra_fields):
		if not phone:
			raise ValueError ('user must have a phone number')
			phone=phone
			user=self.model(phone=phone,**extra_fields)
			user.set_password(password)
			user.save(using=self._db)
			return user
	def create_user(self,phone,password,**extra_fields):
		extra_fields.setdefault('is_staff',False)
		extra_fields.setdefault('is_superuser',False)
		return self._create_user(phone,password,**extra_fields)
	def create_superuser(self,phone,password=None,**extra_fields):
		extra_fields.setdefault('is_staff',True)
		extra_fields.setdefault('is_superuser',True)
		if extra_fields.get('is_staff') is not True:
			raise ValueError('superuser must have is_staff=True') 
		if extra_fields.get('is_superuser') is not True:
			raise ValueError('superuser must have is_superuser=True') 
		return self._create_user(phone,password,**extra_fields)


class User(AbstractUser):
	username=None
	name=models.CharField(max_length=50)
	email=models.EmailField(blank=True,null=True)
	phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 12 digits allowed.")
	phone = models.CharField(_('phone number'), validators=[phone_regex], max_length=17, unique=True) # validators should be a list
	friends=models.ManyToManyField('User', blank=True)

	USERNAME_FIELD='phone'
	REQUIRED_FIELDS=['email','name']
	objects=UserManager()

	def __str__(self):
		return self.name
		