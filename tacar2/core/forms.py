from captcha.fields import CaptchaField
from django.forms import ModelForm
from core.models import Cliente, Fabricante, Veiculo, TabelaPreco, Rotativo, Mensalista


class FormCliente(ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = Cliente
        fields = "__all__"


class FormVeiculo(ModelForm):
    class Meta:
        model = Veiculo
        fields = "__all__"


class FormFabricante(ModelForm):
    class Meta:
        model = Fabricante
        fields = "__all__"

class FormTabelaPreco(ModelForm):
    class Meta:
        model = TabelaPreco
        fields = "__all__"

class FormRotativo(ModelForm):
    class Meta:
        model = Rotativo
        fields = "__all__"

class FormMensalista(ModelForm):
    class Meta:
        model = Mensalista
        fields = "__all__"