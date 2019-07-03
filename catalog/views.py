from django.shortcuts import render
from django.http import HttpResponse


from .forms import SearchForm


def homepage(request):

    if request.method == 'GET':
        search_form = SearchForm()
        return render(request, 'catalog/homepage.html', {
            'form': search_form
        })
    else:
        search_form = SearchForm(request.POST)
        if search_form.is_valid():
            content = search_form.cleaned_data['search_content']
            radio_button = search_form.cleaned_data['selected_radio']
            print(content)
            print(radio_button)
