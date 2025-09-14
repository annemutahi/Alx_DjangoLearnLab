from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

# Example form to handle Book input safely
class ExampleForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date']

    # Optional extra validation
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if "<script>" in title.lower():
            raise forms.ValidationError("Invalid input detected.")
        return title