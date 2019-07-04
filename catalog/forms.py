from django import forms

from .models import Document


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


class DocumentUploadForm(forms.ModelForm):

    # name = forms.CharField(
    #     max_length=50,
    #     required=True,
    #     label='Name',
    #     widget=forms.TextInput(
    #         attrs={
    #             'class': 'form-control',
    #             'placeholder': 'Document Name...'
    #         }
    #     )
    # )

    # file_content = forms.FileField(
    #     label='Document',
    #     required=False,
    #     widget=forms.FileInput(
    #         attrs={
    #             'class': 'form-control'
    #         }
    #     )
    # )

    # author = forms.ChoiceField(
    #     label='Owner',
    #     widget=forms.Select(
    #         attrs={
    #             'class': 'form-control'
    #         },
    #         choices=()
    #     )
    # )

    # word_art = forms.FileField(
    #     label='Cover Picture',
    #     required=False,
    #     widget=forms.FileInput(
    #         attrs={
    #             'class': 'form-control'
    #         }
    #     )
    # )

    class Meta:
        model = Document
        fields = ['name', 'file_content', 'author', 'word_art']
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Document Name...',
                    'required': True
                }
            ),
            'file_content': forms.FileInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'author': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'word_art': forms.FileInput(
                attrs={
                    'class': 'form-control'
                }
            )

        }
