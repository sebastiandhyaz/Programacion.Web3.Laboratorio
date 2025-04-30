from django import forms

class ActividadForm(forms.Form):
    nombre = forms.CharField(max_length=100, label='Nombre')
    descripcion = forms.CharField(widget=forms.Textarea, label='Descripción')
    fecha_inicio = forms.DateField(widget=forms.SelectDateWidget, label='Fecha de Inicio')
    fecha_fin = forms.DateField(widget=forms.SelectDateWidget, label='Fecha de Fin')