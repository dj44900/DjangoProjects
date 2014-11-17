from django.contrib import admin
from Main.models import DeathFeed
from Main.models import DeathBlog


# Register your models here.
admin.site.register(DeathBlog)
admin.site.register(DeathFeed)
