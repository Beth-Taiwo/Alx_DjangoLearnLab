from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Post, Comment
from django.forms import Textarea
from taggit.forms import TagWidget

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["email"]  # Allow users to change their email address


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["bio", "profile_picture"]  # filelds for bio and profile picture


class PostForm(forms.ModelForm):
    tags = forms.CharField(
        max_length=50,
        required=False,
        help_text='Add new tag (comma-separated)',
        widget= TagWidget()
    )
    
    class Meta:
        model = Post
        fields = ["title", "content", "tags"]
        widgets = {
            "content": Textarea(attrs={"cols": 100, "rows": 25}),
        }
        
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            self.fields['tags'].initial = ','.join([tag.name for tag in self.instance.tags.all()])

    def save(self, commit=True):
        post = super().save(commit=False)
        tags = self.cleaned_data.get("tags", "")
        if tags:
            post.save()  # Save the post to generate an ID before adding tags
            post.tags.set([t.strip() for t in tags.split(",")])
        if self.user:
            post.author = self.user
        if commit:
            post.save()
        return post


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]
        
        def __init__(self, *args, **kwargs):
            self.post = kwargs.pop("post", None)
            super().__init__(*args, **kwargs)
            
            if self.post:
                self.fields["author"].initial = self.post.author
                
                # Ensure the comment author is the same as the post author
                self.fields["author"].widget.attrs["disabled"] = True
                
                # Hide the comment creation date field
                self.fields["created_at"].widget = forms.HiddenInput()
                self.fields["updated_at"].widget = forms.HiddenInput()
                
            # Limit the comment length to 500 characters
            self.fields["content"].widget.attrs["maxlength"] = 500
            self.fields["content"].widget.attrs["rows"] = 5
            self.fields["content"].widget.attrs["placeholder"] = "Write a comment..."
            
        def save(self, commit=True):
            comment = super().save(commit=False)
            if self.post:
                comment.post = self.post
            if commit:
                comment.save()
            return comment
    