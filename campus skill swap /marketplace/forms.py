from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Skill, Review, BookingRequest


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['title', 'description', 'category', 'price', 'is_free', 'contact_preference', 'availability']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }

    def clean(self):
        cleaned_data = super().clean()
        price = cleaned_data.get('price')
        is_free = cleaned_data.get('is_free')

        if is_free:
            cleaned_data['price'] = 0

        if not is_free and (price is None or price < 0):
            self.add_error('price', 'Enter a valid price or mark as free.')

        return cleaned_data


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']
        widgets = {
            'comment': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Share your experience with this skill...'}),
        }


class BookingRequestForm(forms.ModelForm):
    class Meta:
        model = BookingRequest
        fields = ['message', 'preferred_date']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Describe what you need help with and any specific requirements...'}),
            'preferred_date': forms.DateInput(attrs={'type': 'date'}),
        }
