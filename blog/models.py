from django.db import models
from django.conf import settings
from django.utils import timezone


class Post_category(models.Model):
    category_name = models.CharField(max_length=60, verbose_name='Категориянын аты')
    category_image = models.ImageField(blank=True, null=True, upload_to='blog/image/%Y/%m/%d/')

    def __str__(self):
        return self.category_name

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.ForeignKey(Post_category, on_delete=models.CASCADE, verbose_name='Категория')
    title = models.CharField(max_length=200)
    text = models.TextField()
    image = models.ImageField(upload_to='blog/image/%Y/%m/%d/')
    created_date = models.DateField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


