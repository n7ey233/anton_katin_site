from django import forms
from .models import *

class order_partForm(forms.ModelForm):

    class Meta:
        model = order_part
        widgets = {}
        fields = '__all__'
        exclude = ('created_date',)
    def __init__(self, *args, **kwargs):
        super(order_partForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class order_callForm(forms.ModelForm):

    class Meta:
        model = order_call
        widgets = {}
        fields = '__all__'
        exclude = ('created_date',)
    def __init__(self, *args, **kwargs):
        super(order_callForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'