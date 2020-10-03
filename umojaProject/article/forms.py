from django import forms
from .models import Article, Internship, Fellowship, Program, Gallery, PostImages, Profile
from trix.widgets import TrixEditor

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title","content","article_image"]

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["first_name","last_name","info","classof", "picture"]

class NoteFullForm(ArticleForm): #extending form
    images = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    class Meta(ArticleForm.Meta):
        fields = ArticleForm.Meta.fields + ['images',]

class InternshipForm(forms.ModelForm):
    class Meta:
        model = Internship
        fields = ["internship_company","name","link","industry", "location"]

class FellowshipForm(forms.ModelForm):
    class Meta:
        model = Fellowship
        fields = ["name","link","location"]

class ProgramForm(forms.ModelForm):
    class Meta:
        model = Program
        fields = ["program_company","diversity_program","diversity_link","diversity_industry","diversity_population"]

class ImageForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = ["image","eventName", "eventDate"]

from trix.widgets import TrixEditor

class EditorForm(forms.Form):
    content = forms.CharField(widget=TrixEditor)
