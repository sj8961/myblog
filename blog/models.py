from django.db import models
# from login.models import User

class Article(models.Model):
    # article_id = id
    title = models.CharField(max_length=64, default='Title')
    author_id = models.ForeignKey("User", to_field="id", on_delete=models.CASCADE, default=0)
    content = models.TextField(null=True)
    pub_time = models.DateTimeField(auto_now_add=True, null=True, editable=True)
    update_time = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.title

class User(models.Model):
    '''用户'''

    gender = (
        ('male','男'),
        ('female', '女'),
    )

    name = models.CharField(max_length=64, unique=True)
    password = models.CharField(max_length=250)
    email = models.CharField(max_length=128, unique=True)
    sex = models.CharField(max_length=32, choices=gender, default='男')
    c_time = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name

    class Meta:
        ordering = ['c_time']
        verbose_name = '用户'
        verbose_name_plural = '用户'
