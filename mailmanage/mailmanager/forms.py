from django import forms
from .models import Mail

class Mail_Form(forms.ModelForm):
    
    class Meta:
        model = Mail
        fields = ['name', 'email', 'title', 'text', 'allow_data_process']
        widgets = {
			'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'rows': 8}),
            'allow_data_process': forms.CheckboxInput(attrs={'class': 'form-check-label'}),
        }

        # def clean_checkbox(self):
        #     allow_data_process = self.cleaned_data['allow_data_process']
        #     if allow_data_process.check_test=False:
        #         raise ValidationError('Соглашение на обработку персональных данных обязательно')
        #     return allow_data_process


        
