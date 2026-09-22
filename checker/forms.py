from django import forms
from .models import Resume


class ResumeUploadForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['name', 'resume_file', 'job_description']
        widgets = {
            'job_description': forms.Textarea(attrs={
                'rows': 6,
                'class': 'form-control',
                'placeholder': 'Job description paste karo jya sathe resume match karvu che...'
            }),
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Tamaru naam'
            }),
            'resume_file': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
