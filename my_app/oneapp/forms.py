from django import forms
from .models import contact



class contactform(forms.ModelForm):

    class Meta:
        model = contact
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(attrs={"class":"name_field", "placeholder":"Name"}),
            "phone": forms.TextInput(attrs={"class":"name_field", "placeholder":"Phone Number"}),
            "email": forms.EmailInput(attrs={"class":"email_field","placeholder":"Email"}),
            "goal" : forms.TextInput(attrs={"class":"goal_field","placeholder":"What's Your Goal?"}),
            "availability": forms.TextInput(attrs={  "class":"name_field","placeholder":"Availability for a brief discussion"})
        }