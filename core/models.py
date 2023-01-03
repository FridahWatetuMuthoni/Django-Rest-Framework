from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from uuid import uuid4


# Create your models here.

GENDER = (('Female', 'Female'), ('Male', 'Male'), ('Other', 'Other'),)


class User(AbstractUser):
    phone_number = models.IntegerField(null=True)
    gender = models.CharField(max_length=200, choices=GENDER, null=True)


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)


class CoreQuerySet(models.QuerySet):
    def active(self):
        return self.filter(is_active=True)

    def inactive(self):
        return self.filter(is_active=False)


class CoreManager(models.Manager):
    def get_queryset(self):
        return CoreQuerySet(self.model, using=self._db)

    def active(self):
        return self.get_queryset().active()

    def inactive(self):
        return self.get_queryset().inactive()


class Post(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=100)
    text = models.TextField()
    tags = models.ManyToManyField(Tag, related_name='posts', blank=True)
    author = models.ForeignKey(
        User, related_name='posts', on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    created = models.DateTimeField(
        auto_now_add=True, db_index=True, verbose_name=_("created"))
    updated = models.DateTimeField(auto_now=True, verbose_name=_("updated"))
    is_active = models.BooleanField(default=True, db_index=True)

    objects = CoreManager()

    def __str__(self):
        return str(self.pk)

    def __repr__(self):
        return f"<{self.__class__.__name__} {self.pk}>"

    def activate(self):
        if not self.is_active:
            self.is_active = True
            self.save(update_fields=["is_active",
                      "updated"] if self.pk else None)

    def deactivate(self):
        if self.is_active:
            self.is_active = False
            self.save(update_fields=["is_active",
                      "updated"] if self.pk else None)
