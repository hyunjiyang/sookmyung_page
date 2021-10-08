from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Sookplace(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    address = models.TextField()
    detail_addr = models.TextField()
    describe = models.TextField()
    photo = models.ImageField(null=True,blank=True, upload_to='sookplace/')

    def __str__(self):
        return self.title