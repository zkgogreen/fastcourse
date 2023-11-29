from django import forms
from .models import Room, Bab, Pelajaran, Questions

class RoomForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(RoomForm, self).__init__(*args, **kwargs)
        
        # Add the 'form-control' class to all form fields
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            
    class Meta:
        model = Room
        fields = ['bahasa', 'level', 'time', 'mulai', 'jadwal']
        widgets = {
            'mulai': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

class BabForm(forms.ModelForm):
    class Meta:
        model = Bab
        fields = ['bab','premium']
        widgets = {
            'bab'    : forms.TextInput(attrs={'class': 'form-control'}),
            'premium': forms.CheckboxInput(attrs={'type': 'checkbox', 'class': 'form-check-input'}),
        }

class AddPelajaran(forms.ModelForm):
    class Meta:
        model = Pelajaran
        fields = ['judul','keterangan','vidio','text']

        widgets = {
            'judul'    : forms.TextInput(attrs={'class': 'form-control'}),
            'keterangan': forms.TextInput(attrs={'class': 'form-control'}),
            'vidio'    : forms.TextInput(attrs={'class': 'form-control'}),
        }

class AddSoal(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AddSoal, self).__init__(*args, **kwargs)
        
        # Add the 'form-control' class to all form fields
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Questions
        fields = ['soal','answer','wrong1','wrong2','wrong3','penjelasan']  
