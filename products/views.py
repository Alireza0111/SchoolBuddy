import os
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.conf import settings
from products.models import FilesAdmin
from sbuddy import settings


def index(request):
    return render(request, 'products/index.html')


@login_required
def books(request):
    context = {'file': FilesAdmin.objects.all()}
    return render(request, 'products/books.html', context)


def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/adminupload")
            response['Content_Disposition'] = 'inline; filename='+os.path.basename(file_path)
            return response
    raise Http404


def contact(request):
    if request.method == 'POST':
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        send_mail(subject, message, settings.EMAIL_HOST_USER, ['alirezashohan001@gmail.com'], fail_silently=False )
    return render(request, 'products/contact.html')

