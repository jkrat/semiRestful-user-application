from __future__ import unicode_literals
from django.db import models

class UserManager(models.Manager):
    def validate(self, data):
        if len(data['firstName']) < 1:
            return False
        if len(data['lastName']) < 1:
            return False
        if len(data['email']) < 1:
            return False 
        return True
    def validate_change(self, data):
        if len(data['name']) < 1:
            return False
        if len(data['email']) < 1:
            return False 
        return True
    def register(self, data):
        nameString = data['firstName'] + ' ' + data['lastName']
        User.objects.create(name=nameString, email=data['email'])
    def update(self, data):
        user= User.objects.get(id=data['id'])
        user.name=data['name']
        user.email=data['email']
        user.save()

class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = UserManager()




# class UserManager(models.Manager):
#     def Validate(self, data):
#         if len(data['name']) < 1 :
#             return False

#         user.objects.create(first_name=data['full_name'])