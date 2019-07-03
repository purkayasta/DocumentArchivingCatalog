from django import forms


class SearchForm(forms.Form):
    RADIO_CHOICES = (
        (1, 'All'),
        (2, 'Name'),
        (3, 'Keyword'),
    )
    search_content = forms.CharField(
        max_length=20,
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'id': 'search_bar',
                'placeholder': 'Search...',
            }
        ))
    selected_radio = forms.IntegerField(
        required=True,
        widget=forms.RadioSelect(choices=RADIO_CHOICES),
    )
