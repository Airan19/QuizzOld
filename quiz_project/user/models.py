from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone


class UserManager(BaseUserManager):

    def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        now = timezone.now()
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            is_staff=is_staff,
            is_active=True,
            is_superuser=is_superuser,
            last_login=now,
            date_joined=now,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, **extra_fields):
        return self._create_user(email, password, False, False, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        user=self._create_user(email, password, True, True, **extra_fields)
        return user


# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=254, null=False, blank=True)
    # last_name = models.CharField(null=False, max_length=30)
    email = models.EmailField(unique=True, null=False, max_length=254)
    # password = models.CharField(null=False, max_length=100)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def get_absolute_url(self):
        return "/users/%i/" % (self.pk)


    def __str__(self):
            return '%s %s %s' % (self.id, self.email, self.name)


class Tags(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    opt = models.CharField(max_length=50, null=False)


class SetofQuestions(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    question = models.TextField(null=False)
    answer = models.CharField(max_length=2, null=False)
    options = models.CharField(max_length=200)
    tags = models.ForeignKey(Tags, on_delete=models.SET_NULL, null=True)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return '%s %s %s' % (self.question, self.tags, self.answer)


class Options(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    opt = models.TextField(null=False)


