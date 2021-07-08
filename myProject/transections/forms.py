from django import forms

from .models import NetworkList, AddSubList, NewExposure


class NetListForm(forms.ModelForm):
    """Form class for NetworkList model"""

    class Meta:
        model = NetworkList
        fields = ('subnet_name', 'subnet_value')


class AddSubListForm(forms.ModelForm):
    """Form class for AddSubList model"""

    class Meta:
        model = AddSubList
        fields = ('acc_subnet_name', 'acc_subnet_value')

        
class NewExpForm(forms.ModelForm):
    """Formclass for NewExposure model"""

    class Meta:
        model = NewExposure
        fields = ("new_sub_name", "new_sub_value")
