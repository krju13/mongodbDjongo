from djongo import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    tag =models.CharField(max_length=100)
    def __str__(self):
        return self.title