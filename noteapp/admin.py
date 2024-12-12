from django.contrib import admin
from .models import Note
# Register your models here.

# what to display in the admin panel
class NoteAdmin(admin.ModelAdmin):
    list_display =["title", "category", "created", "updated"]


# If this is not registed you wont be able to the Note in the admin panel
admin.site.register(Note, NoteAdmin)