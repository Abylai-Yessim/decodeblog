from django import forms
from .models import *

class AddBlogForm(forms.ModelForm):
    class Meta:
        model = NewBlog
        fields = ['name', 'category', 'image', 'description', 'date']
        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'fieldset input'}),
            # 'category': forms.ModelChoiceField(attrs={'class': 'fieldset input'}),
            'image': forms.FileInput(attrs={'class': 'fieldset button button-yellow input-file form-control'}),
            'description': forms.Textarea(attrs={'class': 'input input-textarea '}),

        }

    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        to_field_name='name',
        required=True,  
        widget=forms.Select(attrs={'class': 'form-control input '})
    )

    def save(self, commit: bool = ...):
        author = User.objects.get(id=self.data['author_id'])
        self.instance.author = author
        return super().save(commit)

# class BlogForm(forms.ModelForm):
#     class Meta:
#         model = EditBlogModel
#         fields = ['name', 'image', 'category', 'description', 'date']

#     def save(self, commit=True):
#         blog = super().save(commit=False)
#         # Выполните любую дополнительную логику здесь, если это необходимо
#         if commit:
#             blog.save()
#         return blog


class CommentForm(forms.ModelForm):
     class Meta:
        model = Comment
        fields = ['user', 'blog','text', 'date']
        widgets = {
            'description':forms.Textarea(attrs={'rows':3})
        }

