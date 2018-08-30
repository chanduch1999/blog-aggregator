from django.contrib import admin
from .models import Article

#def article_list(request):
admin.site.register(Article)
