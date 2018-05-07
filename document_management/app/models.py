from __future__ import unicode_literals
from .validators import validate_file_extension
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	name = models.CharField(max_length=100, null=True, blank=True)
	email = email = models.EmailField(max_length=255, 
							null=True, blank=True, unique=True)
	dob = models.CharField(max_length=10, blank=True, null=True)

	def __str__(self):
		return str(self.name)

class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/%Y/%m/%d/', 
    					validators=[validate_file_extension],)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True)

    def __str__(self):
		return str(self.user)

    


 