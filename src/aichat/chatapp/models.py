from django.db import models
from django.db.models import CharField, TextField, NullBooleanField, DateTimeField, IntegerField
from django.conf import settings
from django.core.validators import MinLengthValidator


CHOICES_IS_GLOBSTAR = ((None, ''), (True, 'Yes'), (False, 'No'))


class TimestampedModel(models.Model):
    """ Abstract base class with self-updating ``created`` and ``modified`` fields. """
    created = DateTimeField(auto_now_add=True)
    modified = DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class AuthoredModel(TimestampedModel):
    """ Abstract base class with ``author`` field. """
    author = CharField(max_length=100)
    user = models.OneToOneField(settings.AUTH_USER_MODEL)

    class Meta:
        abstract = True


class Profile(models.Model):
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )

    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    first_name = models.CharField(max_length=120, blank=False)
    last_name = models.CharField(max_length=120, blank=False)
    gender = models.CharField(max_length=1, choices=GENDER)
    zip_code = models.CharField(max_length=5, validators=[MinLengthValidator(5)], blank=False)

    def __unicode__(self):
        return u'Profile of user: {0}'.format(self.user.email)


class TriggerResponse(AuthoredModel):
    trigger = CharField(max_length=200)
    response = TextField()
    source_state = CharField(max_length=200)
    dest_state = CharField(max_length=200)
    is_globstar = NullBooleanField(choices=CHOICES_IS_GLOBSTAR, max_length=3, null=True, blank=True, default=None)

    def __str__(self):
        return self.source_state + ' to ' + self.dest_state


class node(models.Model):
    name = CharField(max_length=200, default='')
    x_loc = IntegerField(default=0)
    y_loc = IntegerField(default=0)

    def __str__(self):
        return self.name


class edge(models.Model):
    trigger = CharField(max_length=200, default='')
    response = CharField(max_length=200, default='')
    source = models.ForeignKey(node, on_delete=models.CASCADE, related_name='source', null=True)
    dest = models.ForeignKey(node, on_delete=models.CASCADE, related_name='dest', null=True)
    is_globstar = NullBooleanField(choices=CHOICES_IS_GLOBSTAR, max_length=3, null=True, blank=True, default=None)

    def __str__(self):
        return self.trigger + ' to ' + self.response
