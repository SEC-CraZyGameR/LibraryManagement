from django.db import models

from django.contrib.auth.models import User

class UserProfile(models.Model):
	user = models.OneToOneField(User,on_delete = models.CASCADE)

	reg_no = models.CharField(max_length=10)
	phone_no = models.CharField(max_length=11)

	def __str__(self):
		return self.user.username