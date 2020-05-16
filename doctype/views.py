from django.shortcuts import render
from django.http import HttpResponse
from doctype import dtdalgo
from . dtdalgo import detect
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage

# Create your views here.
def doctype(request):
    x = detect()
    return render(request, 'doctype.html', {'doctype': x})


def home(request):
    return render(request, 'index.html')

def upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        doctype = detect(filename)
        return render(request, 'upload.html', {
            'uploaded_file_url': uploaded_file_url,
            'doctype': doctype
        })
    return render(request, 'upload.html')
