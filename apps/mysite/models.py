from django.db import models
from slugify import slugify


# Create your models here.

class Page(models.Model):
    title = models.CharField(max_length=240, verbose_name="文章标题")
    slug = models.SlugField(blank=True, unique=True, verbose_name="短标题")
    content = models.TextField(verbose_name="文章内容")
    image = models.ImageField(default="pic14.jpg", verbose_name="上传图片")

    class Meta:
        verbose_name_plural = "页面"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
