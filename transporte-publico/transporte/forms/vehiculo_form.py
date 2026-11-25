from django import forms
from transporte.models import Vehiculo

class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = ['placa', 'tipo', 'capacidad', 'activo', 'ruta', 'conductor']
        widgets = {
            'placa': forms.TextInput(attrs={'placeholder': 'ABC-123'}),
        }

    def clean_placa(self):
        return self.cleaned_data['placa'].strip().upper()

    def clean_capacidad(self):
        capacidad = self.cleaned_data['capacidad']
        if capacidad <= 0:
            raise forms.ValidationError('La capacidad debe ser mayor a 0.')
        return capacidad