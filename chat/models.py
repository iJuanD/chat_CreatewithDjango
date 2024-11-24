from django.db import models
from django.forms import ValidationError

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=150, unique=True)
    profile_picture = models.ImageField(upload_to="profile_pictures/", blank=True, null=True)


class Message(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    content = models.TextField(blank=True)
    attachment = models.FileField(upload_to="attachments/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if not self.content and not self.attachment:
            raise ValidationError("El mensaje debe tener texto o un archivo adjunto.")