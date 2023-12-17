from django.db import models

class HomePage(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    

class AboutPage(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

class News(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    

class ContactPage(models.Model):
    title = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()