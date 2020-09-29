from django import forms
from .models import Article, Internship, Fellowship, Program, Gallery

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title","content","article_image"]

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
