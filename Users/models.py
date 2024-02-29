from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.



class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    tel = models.CharField(max_length=16, null=True)
    address = models.ForeignKey("Address", on_delete=models.SET_NULL, null=True)
    pfp = models.ImageField(upload_to='user_images', default='default_user_image.png')
    date_of_birth = models.DateField(null=True, blank=True)
    # Make email, first name, and last name required
    email = models.EmailField(unique=True, blank=False, null=False)
    first_name = models.CharField(max_length=30, blank=False, null=True)
    last_name = models.CharField(max_length=30, blank=False, null=True)
    points = models.IntegerField(blank=True, null=True)

    def save(self, *args, **kwargs):
        # If the email field is not provided and a User instance exists, set the email field to the user's email
        if not self.email and self.user:
            self.email = self.user.email
        super().save(*args, **kwargs)
    
    def __str__(self):
        return str(self.user)

@receiver(post_save, sender=User)
def create_custom_user(sender, instance, created, **kwargs):
    if created and not hasattr(instance, 'customuser'):
        print("Creating User")
        CustomUser.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_custom_user(sender, instance, **kwargs):
    try:
        print("Saving User")
        instance.customuser.save()
    except CustomUser.DoesNotExist:
        pass


class Address(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='addresse', blank=True, null=True)
    country = models.CharField(max_length=255, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    zip_code = models.CharField(max_length=20, null=True, blank=True)
    street = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.street}, {self.city}, {self.state} {self.zip_code}"