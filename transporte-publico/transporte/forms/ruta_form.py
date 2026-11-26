from django import forms
from transporte.models import Ruta


class RutaForm(forms.ModelForm):
    class Meta:
        model = Ruta
        fields = ['nombre', 'origen', 'destino', 'distancia', 'tarifa', 'paradas']
        widgets = {
            'paradas': forms.CheckboxSelectMultiple(),
        }

    def clean_tarifa(self):
        tarifa = self.cleaned_data['tarifa']
        if tarifa <= 0:
            raise forms.ValidationError('La tarifa debe ser mayor a 0.')
        return tarifa