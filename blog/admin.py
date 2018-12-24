from django.contrib import admin

from blog.models import Article, User

@admin.register(Article)
class Articleadmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'pub_time')
    list_filter = ('pub_time',)


admin.site.register(User)

