from django.db import models


# Create your models here.
class Post(models.Model):
    post_name = models.CharField(max_length=100)
    post_image = models.ImageField(upload_to='')
    post_description = models.TextField()
    post_created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post_name



