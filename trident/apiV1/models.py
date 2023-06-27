from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.user.username

class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.user.username
    
class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.user.username

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    type = models.CharField(max_length=200)
    owner = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.name
    
class OnlineCourse(Product):
    topic = models.CharField(max_length=50)
    

class Lesson(models.Model):
    course = models.ForeignKey(OnlineCourse, on_delete=models.CASCADE, related_name='lessons')
    title = models.CharField(max_length=200)
    description = models.TextField()
    video_url = models.URLField()
    
    def __str__(self):
        return self.title
    

