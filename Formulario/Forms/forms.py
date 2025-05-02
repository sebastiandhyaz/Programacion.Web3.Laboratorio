from django import forms

class FormularioNuevoUsuario(forms.Form):
    nombre = forms.CharField(max_length=100, label="Nombre")
    apellido = forms.CharField(max_length=100, label="Apellido")
    fecha_dia = forms.ChoiceField(
        choices=[(str(i), str(i)) for i in range(1, 32)],
        label="Día de nacimiento"
    )
    fecha_mes = forms.ChoiceField(
        choices=[
            ('enero', 'Enero'), ('febrero', 'Febrero'), ('marzo', 'Marzo'),
            ('abril', 'Abril'), ('mayo', 'Mayo'), ('junio', 'Junio'),
            ('julio', 'Julio'), ('agosto', 'Agosto'), ('septiembre', 'Septiembre'),
            ('octubre', 'Octubre'), ('noviembre', 'Noviembre'), ('diciembre', 'Diciembre')
        ],
        label="Mes de nacimiento"
    )
    fecha_anio = forms.ChoiceField(
        choices=[(str(i), str(i)) for i in range(1950, 2026)],
        label="Año de nacimiento"
    )
    genero = forms.ChoiceField(
        choices=[('M', 'Masculino'), ('F', 'Femenino')],
        widget=forms.RadioSelect,
        label="Género"
    )
    password = forms.CharField(widget=forms.PasswordInput, label="Contraseña")
    email = forms.EmailField(max_length=100, label="Correo Electrónico")
    aficiones = forms.MultipleChoiceField(
        choices=[
            ('deportes', 'Deportes'),
            ('coches', 'Coches'),
            ('musica', 'Música')
        ],
        widget=forms.CheckboxSelectMultiple,
        label="Aficiones"
    )
