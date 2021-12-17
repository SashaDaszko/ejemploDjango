from django import forms


class EmpleadoFormulario(forms.Form):

    #HAY QUE PONER QUE CAMPOS QUEREMOS QUE SE VEAN EN LA WEB
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    dni = forms.IntegerField()
    profesional = forms.BooleanField()
    fechaDeNacimiento = forms.DateField()



class EstadioFormulario(forms.Form):

    #Especificar los campos

    direccion = forms.CharField(max_length=40)
    anioFund = forms.IntegerField()


class JugadorFormulario(forms.Form):

    apellido = forms.CharField(max_length=40)
    numero = forms.IntegerField()
    esBueno = forms.BooleanField()