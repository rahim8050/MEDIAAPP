from django.db import models
from django.contrib.auth import get_user_model  # ✅ Correct
User = get_user_model()

# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    bio = models.TextField(blank=True)
    profileimg = models.ImageField(upload_to = 'profile_images',  default='profileicon.png')
    location = models.TextField(blank=True)
    def __str__(self):
        return self.user.username
