from django import forms
from .models import Meep,Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ProfilePicForm(forms.ModelForm):
    profile_image = forms.ImageField(label='Profile picture')
    profile_bio = forms.CharField(label='Profile Bio', widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Profile Bio'}))
    homepage_link = forms.CharField(label='HomePage Link', widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'HomePage Link'}))
    facebook_link = forms.CharField(label='Facebook Link', widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Facebook Link'}))
    instagram_link = forms.CharField(label='Instagram Link', widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Instagram Link'}))
    


    class Meta:
        model = Profile 
        fields = ('profile_image', 'profile_bio', 'homepage_link','facebook_link', 'instagram_link')


class MeepForm(forms.ModelForm):
    body = forms.CharField(required=True, widget=forms.widgets.Textarea(attrs={'placeholder': 'Enter Your Tweet!', 'class':'form-control',}), label='',)


    class Meta:
        model = Meep
        exclude = ('user','likes', )



# class SignUpForm(UserCreationForm):
#     email = forms.EmailField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}))
#     first_name = forms.CharField(label='', max_length=100,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'firstname'}))
#     last_name = forms.CharField(label='', max_length=100,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'last_name'}))


    # class Meta:
    #     model = User
    #     fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


    #     def __init__(self, *args, **kwargs):
    #         super(SignUpForm, self).__init__(*args, **kwargs)
            
 

    #         self.fields['username'].widget.attrs['class'] = 'form-control'
    #         self.fields['username'].widget.attrs['placeholder'] = 'User Name'
    #         self.fields['username'].label = ''
    #         self.fields['username'].help_text = '<span class=form-text text-muted><small>Required.</small></span>'

    #         self.fields['username'].widget.attrs['class'] = 'form-control'
    #         self.fields['password1'].widget.attrs['placeholder'] = 'Password1'
    #         self.fields['username'].label = ''
    #         self.fields['password1'].help_text = '<ul class=form-text text-muted><small>Enter the correct password.</small></ul>'

    #         self.fields['password2'].widget.attrs['class'] = 'form-control'
    #         self.fields['password2'].widget.attrs['placeholder'] ='Confirm Password'
    #         self.fields['password2'].label = ''
    #         self.fields['password2'].help_text = '<span class=form-text text-muted><small>Enter the same password as before, for verification.</small></span>'

class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'