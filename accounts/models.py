from django.db import models
from django.contrib.auth.models import User


class Testimonial(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return self.user.username
