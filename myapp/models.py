
from django.db import models
from django.contrib.auth.models import User

class mapPointers(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()
    rate = models.IntegerField()
    photo = models.ImageField()
    status = models.BooleanField(default=False)
    booked_by = models.CharField(default="empty", max_length=500)
    email = models.EmailField(default = "megh.shah2003@gmail.com",max_length=254)
    Booked_email = models.EmailField(default = "sample@gmail.com",max_length=254)

    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)
        img = Image.open(self.photo.path)
        if img.height > 1000 or image.width > 700:
            output_size = (800,500)
            img.thumbnail(output_size)
            img.save(self.photo.path)
    
    def __str__(self):
        return f'MapPointer {self.id} - User: {self.user.username}'


class myBooking1(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    latitude = models.FloatField()
    longitude = models.FloatField()
    rate = models.IntegerField()
    photo = models.ImageField()
    var = models.IntegerField(default = 0)
    email = models.EmailField(default = "megh.shah2003@gmail.com",max_length=254)


class Booked(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()
    rate = models.IntegerField()
    photo = models.ImageField()
    status = models.BooleanField(default=False)


    def __str__(self):
        return f'MapPointer {self.id} - User: {self.user.username}'

class Chat(models.Model):
    sender = models.ForeignKey(User, related_name='sender', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='receiver', on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)


class Earning(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    earning = models.IntegerField(default=0)


class Previous(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    latitude = models.FloatField()
    longitude = models.FloatField()
    rate = models.IntegerField()
    
