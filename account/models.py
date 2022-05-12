from django.db import models

from django.contrib.auth.models import AbstractUser


class Account(AbstractUser):
    username = models.CharField(max_length=13, unique=True,
                                help_text=(
                                    "siz 50 ta belgidan iborat username tanlashingiz mumkin"
                                ),
                                error_messages={
                                    "unique": "Bunaqa user avval ro`yxatdan o`tgan."
                                },
                                )
    phone_number = models.CharField(max_length=13, null=True, blank=True, 
                                    error_messages = {
                 'required':"Faqat raqam kiriting!!!"
                 })
    data_of_birth = models.DateField(null=True, blank=True)
    image = models.ImageField(upload_to='account')
    address = models.CharField(max_length=150, null=True, blank=True)
    
    USERNAME_FILED = "username"
    
    def __str__(self):
        return self.username