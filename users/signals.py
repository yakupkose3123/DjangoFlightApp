from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

#! User modelinden çıkan sinyali yakala ve yeni bir user oluşturulduğunda bana bir token üret (rest_framework ün token modeli üzerinden)


@receiver(post_save, sender=User) #signal i yakalayan decorater
def create_token(sender, instance=None, created=False, **kwargs): #burası dokumanda var, standart burayı elleme 
    if created:   #Eğer user create olduysa
        Token.objects.create(user=instance)


      
