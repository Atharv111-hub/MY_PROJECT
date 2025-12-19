from django.db import models
from django.utils import timezone
from PIL import Image
import io
from django.core.files.base import ContentFile

CROP_WIDTH = 450
CROP_HEIGHT = 350

class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    created_at = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        # call original save to ensure image file exists
        super().save(*args, **kwargs)
        if self.image:
            try:
                img = Image.open(self.image.path)
                img = img.convert('RGB')
                # center-crop to maintain desired ratio
                img_ratio = img.width / img.height
                target_ratio = CROP_WIDTH / CROP_HEIGHT
                if img_ratio > target_ratio:
                    # crop width
                    new_width = int(target_ratio * img.height)
                    left = (img.width - new_width) // 2
                    img = img.crop((left, 0, left + new_width, img.height))
                else:
                    # crop height
                    new_height = int(img.width / target_ratio)
                    top = (img.height - new_height) // 2
                    img = img.crop((0, top, img.width, top + new_height))
                img = img.resize((CROP_WIDTH, CROP_HEIGHT), Image.LANCZOS)
                img.save(self.image.path, format='JPEG', quality=85)
            except Exception as e:
                # fallback: do nothing
                pass

    def __str__(self):
        return self.name

class Client(models.Model):
    name = models.CharField(max_length=200)
    designation = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='clients/')
    created_at = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.image:
            try:
                img = Image.open(self.image.path)
                img = img.convert('RGB')
                img = img.resize((450,350), Image.LANCZOS)
                img.save(self.image.path, format='JPEG', quality=85)
            except Exception:
                pass

    def __str__(self):
        return self.name

class ContactSubmission(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    mobile = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    submitted_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.full_name} - {self.email}"

class Subscription(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.email