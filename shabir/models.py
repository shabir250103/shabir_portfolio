
# Create your models here.
from django.db import models

class Projects(models.Model):
    name = models.CharField(max_length=500, verbose_name="Project name")
    description = models.TextField(max_length=10000, verbose_name="Project description")
    redirect = models.CharField(max_length=50000, verbose_name="Project URL")
    banner = models.ImageField(upload_to='pages/photos', verbose_name='Project banner', null=True, blank=True)


    def __str__(self):
        return self.name

class ProjectImage(models.Model):
    project = models.ForeignKey(Projects, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='projects/images', verbose_name='Project Images')

    def __str__(self):
        return f"{self.project.name} Image"



class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    company = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.email}'

