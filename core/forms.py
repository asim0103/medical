from django import forms

from core.models import Contact

class ContactForm(forms.ModelForm):
    
    class Meta:
        model= Contact
        fields= ('name', 'surname', 'email', 'message', )
        widgets={
            'name': forms.TextInput(attrs={'class': 'form-control', 'col-sm-6' 'placeholder' : ('Name')}),
            'surname': forms.TextInput(attrs={'class': 'form-control', 'col-sm-6' 'placeholder' : ('Surname')}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'col-sm-6' 'placeholder' : ('Email')}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'col-sm-6'  'placeholder' : ('Message'), 'rows':5,  }),
        }