from django import forms

from fake.core.models import Fake


class FakeModelForm(forms.ModelForm):

    class Meta:
        model = Fake
        fields = ('url', )