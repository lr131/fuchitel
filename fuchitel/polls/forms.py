from dataclasses import field
from django import forms

from .models import Applicant, Education, Schedule, Districts

class EmailForm(forms.Form):  
    email = forms.EmailField()
    
class SearchForm(forms.Form):
    query = forms.CharField()
    
class ApplicantForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
            self.fields[field].widget.attrs.update({'placeholder': self.fields[field].label})
        self.fields['education'].empty_label = "Не указано"
        self.fields['schedule'].empty_label = "Не указано"
        self.fields['district'].empty_label = "Не указано"
        self.fields['driver_license'].empty_label = "Не указано"
        
    
    class Meta:
        model = Applicant
        fields = '__all__'
        widgets = {
            'registration': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
            'address': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
            'note': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
            'education_descr': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
            'hobby': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
            'black_list': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }