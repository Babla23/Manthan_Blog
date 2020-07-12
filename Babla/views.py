from django.shortcuts import render, get_object_or_404
from Babla.models import babla


# Create your views here

def Home(request):
    project = babla.objects
    return render(request, 'Babla/babla_index.html', {'Babla': project})


def Second(request):
    return render(request, 'Babla/Register.html')


def detail(request, babla_id):
    babla_detail = get_object_or_404(babla, pk=babla_id)
    return render(request, 'Babla/view_page.html', {'baba_detail': babla_detail})
