from django.db import models
from django.utils import timezone


# Create your models here.
class UserDb(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    first_name = models.CharField(null=False, max_length=30)
    last_name = models.CharField(null=False, max_length=30)
    email = models.EmailField(unique=True, null=False)
    password = models.CharField(null=False, max_length=100)

    def __str__(self):
        return '%s %s %s %s' % (self.id, self.email, self.first_name, self.last_name)


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


