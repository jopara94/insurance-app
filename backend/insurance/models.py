from django.db import models

# Create your models here.
class Member(models.Model):
    first_name = models.CharField(max_length=30, default='')
    last_name = models.CharField(max_length=30, default='')
    phone_number = models.CharField(max_length=15, default='', null=True)

    def __str__(self):
        return self.first_name

class Dependent(models.Model):
    first_name = models.CharField(max_length=30, default='')
    last_name = models.CharField(max_length=30, default='')
    relationship = models.CharField(max_length=12, default='')
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='dependents')

    def __str__(self):
        return self.first_name