from froala_editor.fields import FroalaEditor
from django import forms

from posts.models import Post

class PostForm(forms.ModelForm):
    content = forms.CharField(widget=FroalaEditor(plugins=('font_size', 'font_family')))
    publish = forms.DateField(widget=forms.SelectDateWidget)
    class Meta:
        model = Post

        fields = [
                'title',
                'content',
                'image', 
                'draft',
                'publish'
                ]
