from django.db import models

class Category(models.Model):
      nam = models.CharField(max_length=100)
    
    
class Blog(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='home/')
    body = models.TextField()
    cat = models.ForeignKey(Category,on_delete=models.PROTECT)
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
