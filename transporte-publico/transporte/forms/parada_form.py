from django import forms
from transporte.models import Parada


class ParadaForm(forms.ModelForm):
    class Meta:
        model = Parada
        fields = ['nombre', 'direccion']
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Nombre de la parada'}),
            'direccion': forms.TextInput(attrs={'placeholder': 'Dirección'}),
        }

    def clean_nombre(self):
        nombre = self.cleaned_data['nombre'].strip()
        if len(nombre) < 3:
            raise forms.ValidationError('El nombre debe tener al menos 3 caracteres.')
        return nombre