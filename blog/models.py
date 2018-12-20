from django.db import models

class Article(models.Model):
    # article_id = id
    title = models.CharField(max_length=64)
    content = models.TextField(null=True )

    def __str__(self):
        return self.title
