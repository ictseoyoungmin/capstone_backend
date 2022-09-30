from importlib.resources import contents
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    # image = models.ImageField(upload_to='images/',blank=True, null=True)
    
    def __str__(self):
        """molde title"""
        return self.title

# class Photo(models.Model):
#     post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
#     image =  models.TextField()#models.ImageField(upload_to='images/', blank=True, null=True)
    