from django.db import models

class Article(models.Model):
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    date=models.DateTimeField(auto_now_add=True)
    password = models.CharField(max_length=50,default='12345')

    def __str__(self):
        return self.title