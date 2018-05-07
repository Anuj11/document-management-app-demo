from django import forms
from app.models import Document, Profile

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields ='__all__'


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'        