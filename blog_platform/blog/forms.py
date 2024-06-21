from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'body')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'value': "welcome to my blog!"}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['author'].widget = forms.Select(attrs={'class': 'form-control'}) 

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
        return instance
