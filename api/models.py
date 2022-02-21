from pyexpat import model
from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    '''
    모델 meta와 관련된 옵션
    https://docs.djangoproject.com/en/4.0/ref/models/options/
    '''
    class Meta:
        managed = True
        db_table = 'post'
        app_label = 'api'
        ordering = ['created_at']
        verbose_name = 'Post table'
