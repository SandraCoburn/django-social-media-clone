from django.contrib.auth import get_user_model #will return the active user in form
from django.contrib.auth.forms import UserCreationForm #sign up page

class UserCreateForm(UserCreationForm):
    class Meta:
      fields = ('username', 'email', 'password1', 'password2')
      model = get_user_model()

    # to create labels for the above fields
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Display Name'
        self.fields['email'].label = "Email Address"