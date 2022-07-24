from email.policy import default
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
STATUS = ((0, "Draft"), (1, "Published"))
class Post(models.Model):
    title = models.CharField(max_length=200, unique = True )
    slug = models.CharField(max_length = 200, unique = True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,related_name = 'blog_posts')
    created_on = models.DateTimeField(auto_now_add= True)
    updated_on = models.DateTimeField(auto_now_add= True)
    content = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0 )
    image = models.ImageField(default='', upload_to='images', blank = True, null = True)
    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


