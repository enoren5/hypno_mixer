from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView
from .models import Preamble, Induction, Research, ScriptSuggestion,StockScript,Content
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.admin.models import CHANGE, LogEntry
'''
class CustomLoginView(LoginView):
    form_class = LoginForm
    template_name = 'registration/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    #def get_success_url(self):
    #    return reverse_lazy('/')

def index(request):
    return render(request,'contents/index.html')
'''

class ContentListView(LoginRequiredMixin,ListView):
    # model_list.html
    # model = Induction
    model = Content
    # login_url = '/'
    # template_name = 'home.html'
    
    # fields =['author','title',]
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ContentListView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the Baklawa
        context['inductions'] = Induction.objects.all()
        context['preambles'] = Preamble.objects.all()
        context['research'] = Research.objects.all()
        context['scriptsuggestions'] = ScriptSuggestion.objects.all().order_by('-changed')

        context['stockscripts'] = StockScript.objects.all()
        return context

class PreambleDetailView(LoginRequiredMixin,DetailView):
    model = Preamble
    context_object_name = 'preambles'

class InductionDetailView(LoginRequiredMixin, DetailView):
    model = Induction
    context_object_name = 'inductions'
    
class ScriptSuggestionDetailView(LoginRequiredMixin,DetailView):
    model = ScriptSuggestion
    context_object_name = 'scriptsuggestions'

class StockScriptDetailView(LoginRequiredMixin,DetailView):
    model = StockScript
    context_object_name = 'stockscripts'


class ResearchDetailView(LoginRequiredMixin, DetailView):
    model = Research
    context_object_name = 'research'
    
        
'''def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ContentDetailView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the Baklawa
        context['preambles'] = Preamble.objects.all()
        #context['research'] = Research.objects.all()
        context['scriptsuggestions'] = ScriptSuggestion.objects.all()
        context['stockscripts'] = StockScript.objects.all()
        return context'''