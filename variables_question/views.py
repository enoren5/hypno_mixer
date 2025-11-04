from django.shortcuts import render
from variables_question.models import AuthToggle
# Create your views here.


def portal(request):
    context = {
        "email": AuthToggle.objects.first(),
        "linkedin": AuthToggle.objects.first(),
    }
    return render(request, 'partials/_footer.html', context)