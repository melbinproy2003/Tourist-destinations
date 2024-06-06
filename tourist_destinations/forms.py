from django import forms
from .models import Destination

class DestinationForm(forms.ModelForm):
    class Meta:
        model = Destination
        fields = ['name', 'weather', 'state','district', 'google_map_link', 'image', 'description']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(DestinationForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super(DestinationForm, self).save(commit=False)
        if self.request:
            user_id = self.request.session.get('id')
            instance.by_id = user_id
        if commit:
            instance.save()
        return instance
