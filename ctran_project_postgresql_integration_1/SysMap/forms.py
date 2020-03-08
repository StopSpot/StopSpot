from django import forms


class LocationId(forms.Form):
    stop_location_id = forms.CharField(label='Location ID', max_length=4, required=True)
    lat = forms.HiddenInput()
    lon = forms.HiddenInput()

