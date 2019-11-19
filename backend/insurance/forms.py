from django import forms
from .models import Member, Dependent

class MemberForm(forms.ModelForm):

    class Meta:
        model = Member
        fields = ('first_name', 'last_name', 'phone_number',)


class DependentForm(forms.ModelForm):
    
    class Meta:
        model = Dependent
        fields = ('first_name', 'last_name', 'relationship', 'member',)
