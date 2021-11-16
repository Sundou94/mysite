from django.contrib import admin
from .models import Board

class BoardAdmin(admin.ModelAdmin):
    erarch_fields = ['subject']

# Register your models here.
admin.site.register(Board, BoardAdmin)

