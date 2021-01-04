from django.contrib import admin
from .models import Articles
# Register your models here.

class ArticlesAdmin(admin.ModelAdmin):

    list_display = ('title','author','img','abstract','visited','created_at')
    
<<<<<<< HEAD
    search_fields = ('title','author','abstract','content')
=======
    search_fields = ('title',)
>>>>>>> f4d958d ('模板复用')
    
    list_filter = list_display


admin.site.register(Articles,ArticlesAdmin)