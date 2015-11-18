from django.db import models
from django.core import urlresolvers
from django.contrib.auth.models import User

class User(models.Model):
	user = models.OneToOneField(User, related_name='ask_user')
	avatar = models.ImageField(upload_to='user_pictures')

	def get_absolute_url(self):
		return urlresolvers.reverse('profile', kwargs={'pk': self.pk})

	def __unicode__(self):
		return self.user.username;

	class Meta:
		ordering = ['-user']
# Create your models here.
