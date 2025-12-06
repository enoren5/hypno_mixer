from django.shortcuts import render
from variables_question.models import AuthToggle
from gateway_defender.custom_decorator import protected_redirect
from gateway_defender.models import AuthToggle


@protected_redirect
def portal(request):
    context = {
        "email": AuthToggle.objects.first(),
        "linkedin": AuthToggle.objects.first(),
        "github": AuthToggle.objects.first(),
        "name": AuthToggle.objects.first(),
    }
    return render(request, 'partials/_footer.html', context)