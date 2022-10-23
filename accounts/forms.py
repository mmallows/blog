from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        field = UserCreationForm.Meta.fields + ("pronouns",)

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        field = UserChangeForm.Meta.fields