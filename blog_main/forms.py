from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(UserCreationForm): # usercreatiinform its responsible for rendering the form
    class Meta:
        model=User
        fields=('email','username','password1','password2')