from django.db import models


# Create your models here.
class Message(models.Model):
    username = models.CharField(max_length=30, verbose_name="昵称")
    email = models.EmailField(verbose_name="邮箱")
    subject = models.CharField(max_length=200, verbose_name="主题")
    content = models.TextField(verbose_name="留言内容")

    class Meta:
        verbose_name_plural = '留言'

    def __str__(self):
        return self.subject
