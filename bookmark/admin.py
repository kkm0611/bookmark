from django.contrib import admin

from .models import Bookmark #현재 디랙토리 models에 가서 불러와라

admin.site.register(Bookmark) #admin사이트에 등록해라
# Register your models here.
