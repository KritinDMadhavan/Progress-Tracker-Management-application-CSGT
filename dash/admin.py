from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(personal)
admin.site.register(conference)
admin.site.register(journal)
admin.site.register(book_chapters)
admin.site.register(book_editor)
admin.site.register(consultancy_project)
admin.site.register(patent)

