from django.db import models

# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=200,unique=True,null=False,error_messages ={
                    "unique":"The Name entered already exists."})
    email = models.EmailField(unique=True,null=False,error_messages ={
                    "unique":"The Email Id entered already exists."})
    notes = models.TextField(max_length=200, default="")
    created_time = models.DateTimeField(auto_now_add=True)
   
