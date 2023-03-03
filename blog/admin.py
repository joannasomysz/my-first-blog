from django.contrib import admin
from .models import Post


# Register your models here.

# rejestrujemy model Post aby byl widoczny w panelu admina
admin.site.register(Post)



