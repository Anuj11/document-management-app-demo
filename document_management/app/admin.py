from django.contrib import admin

# Register your models here.
from app.models import Document, Profile

class ProfileAdmin(admin.ModelAdmin):

    list_display =  ('name', 'email', 'dob', 'user')

class DocumentAdmin(admin.ModelAdmin):

    list_display =  ('description', 'document', 'uploaded_at', 'user')
	
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Document, DocumentAdmin)