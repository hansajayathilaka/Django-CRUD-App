from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('eId', 'eName', 'eEmail', 'eContact')
        labels = {
            'eId': 'ID',
            'eName': 'Name',
            'eEmail': 'E-mail',
            'eContact': 'Contact',
        }
