from datetime import date
from django import forms
from transporte.models import Conductor


class ConductorForm(forms.ModelForm):
    class Meta:
        model = Conductor
        fields = ['nombre', 'licencia', 'fecha_ingreso']
        widgets = {
            'fecha_ingreso': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
        }

    def clean_fecha_ingreso(self):
        fecha = self.cleaned_data['fecha_ingreso']
        if fecha > date.today():
            raise forms.ValidationError('La fecha de ingreso no puede ser futura.')
        return fecha