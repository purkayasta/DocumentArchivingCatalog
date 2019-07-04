from django.shortcuts import render, redirect
from django.http import HttpResponse


from .forms import SearchForm, DocumentUploadForm
from .models import Document


def homepage(request):

    if request.method == 'GET':
        search_form = SearchForm()
        document_objects = Document.objects.all()
        return render(request, 'catalog/homepage.html', {
            'form': search_form,
            'documents': document_objects
        })
    else:
        search_form = SearchForm(request.POST)
        if search_form.is_valid():
            content = search_form.cleaned_data['search_content']
            radio_button = search_form.cleaned_data['selected_radio']
            print(content)
            print(radio_button)


def document_upload(request):
    if request.method == 'POST':
        upload_form = DocumentUploadForm(request.POST, request.FILES)
        if upload_form.is_valid():
            upload_form.save()
            return redirect('homepage')
    else:
        upload_form = DocumentUploadForm()
    return render(request, 'catalog/upload.html', {
        'upload_form': upload_form
    })
