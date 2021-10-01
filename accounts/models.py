from django.db import models
from django.contrib.auth.models import AbstractUser

class Account(AbstractUser):
  GENDER_CHOICES = (
    ('male', 'Male'),
    ('female', 'Female'),
  )

  # model fields
  profile_img = models.ImageField(upload_to="profile_images/", default="utility_images/default.png")
  gender = models.CharField(max_length=7, choices=GENDER_CHOICES)

  @property
  def fullname(self):
    return f"{self.first_name} {self.last_name}"

  def __str__(self):
    return self.fullname

  def __str__(self):
    return self.username