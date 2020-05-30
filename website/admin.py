from django.contrib import admin
from .models import Post, Chat
# to_gather 모델
admin.site.register(Post)

# be_together 모델
admin.site.register(Chat)
