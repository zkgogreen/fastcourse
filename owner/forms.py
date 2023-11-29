from django import forms
from teacher.models import Pelajaran, Kelas, Bab
from .models import Kategori, Level, Setting
from django.core.exceptions import ValidationError
from django.utils.safestring import mark_safe

class PelajaranForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['kelas'] = forms.ModelChoiceField(queryset=Kelas.objects.all())
    class Meta:
        model = Pelajaran
        fields = ['judul','urutan','keterangan','vidio','text']
        widgets = {
            'judul':forms.TextInput(attrs={'class':'form-control'}),
            'urutan':forms.NumberInput(attrs={'class':'form-control'}),
            'keterangan':forms.TextInput(attrs={'class':'form-control'}),
            'vidio':forms.TextInput(attrs={'class':'form-control'}),
        }

class KelasForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['kategori'] = forms.ModelChoiceField(queryset=Kategori.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
        self.fields['level'] = forms.ModelChoiceField(queryset=Level.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    class Meta:
        model = Kelas
        fields = ["kelas","bahasa","photo","kategori","level","keterangan","defaultget","premium","certificate","mahkota","biaya","discount",]
        widgets = {
            'kelas':forms.TextInput(attrs={'class':'form-control'}),
            'bahasa':forms.Select(attrs={'class':'form-select'}),
            'photo':forms.FileInput(attrs={'class':'form-control'}),
            'keterangan':forms.Textarea(attrs={'class':'form-control', 'rows':3}),
            'defaultget':forms.CheckboxInput(attrs={'class':'form-check-input'}),
            'mahkota':forms.NumberInput(attrs={'class':'form-control'}),
            'premium':forms.CheckboxInput(attrs={'class':'form-check-input'}),
            'certificate':forms.CheckboxInput(attrs={'class':'form-check-input'}),
            'biaya':forms.NumberInput(attrs={'class':'form-control'}),
            'discount':forms.NumberInput(attrs={'class':'form-control'}),
        }

class BabForm(forms.ModelForm):
    # def __init__(self,slug, *args,**kwargs):
    #     super().__init__(*args,**kwargs)
        # self.fields['kelas'] = forms.ModelChoiceField(queryset=slug)
        # self.fields['kelas'] = forms.ModelChoiceField(queryset=Kelas.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    class Meta:
        model = Bab
        fields = ['bab','premium']
        widgets = {
            'bab':forms.TextInput(attrs={'class':'form-control'}),
            'premium':forms.CheckboxInput(attrs={'class':'form-check-input'}),
        }

class Landing(forms.ModelForm):
    icon = forms.FileField(label='',  widget=forms.FileInput(attrs={'class':'d-none'}))
    logo = forms.FileField(label='',  widget=forms.FileInput(attrs={'class':'d-none'}))
    foto = forms.FileField(label='',  widget=forms.FileInput(attrs={'class':'d-none'}))
    fotoadv = forms.FileField(label='',  widget=forms.FileInput(attrs={'class':'d-none'}))
    class Meta:
        model = Setting
        fields = ['title','sub','icon','logo','foto','fotoadv', 'alamat','telp','email','ig','fb','tiktok','youtube','komisi_teacher','komisi_developer','komisi_owner']
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control my-2'}),
            'sub':forms.TextInput(attrs={'class':'form-control my-2'}),
            'alamat':forms.TextInput(attrs={'class':'form-control my-2'}),
            'telp':forms.NumberInput(attrs={'class':'form-control my-2'}),
            'email':forms.EmailInput(attrs={'class':'form-control my-2'}),
            'ig':forms.URLInput(attrs={'class':'form-control'}),
            'fb':forms.URLInput(attrs={'class':'form-control'}),
            'tiktok':forms.URLInput(attrs={'class':'form-control'}),
            'youtube':forms.URLInput(attrs={'class':'form-control'}),
            'komisi_teacher':forms.NumberInput(attrs={'class':'form-control', 'onchange':'getpercent()'}),
            'komisi_developer':forms.NumberInput(attrs={'class':'form-control', 'disabled':True}),
            'komisi_owner':forms.NumberInput(attrs={'class':'form-control', 'onchange':'getpercent()'}),
        }
    def __init__(self, *args, **kwargs):
        super(Landing, self).__init__(*args, **kwargs)
        setting = Setting.objects.get(id=1)
        self.label_suffix = ''
        self.fields['icon'].label = mark_safe(f'<img src="/media/{setting.icon}" class="img-thumbnail">')
        self.fields['logo'].label = mark_safe(f'<img src="/media/{setting.logo}" class="img-thumbnail">')
        self.fields['foto'].label = mark_safe(f'<img src="/media/{setting.foto}" class="img-thumbnail">')
        self.fields['fotoadv'].label = mark_safe(f'<img src="/media/{setting.fotoadv}" class="img-thumbnail">')
