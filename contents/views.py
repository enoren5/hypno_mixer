from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Preamble, Induction, Research, ScriptSuggestion,StockScript,Content


class ContentListView(ListView):
    # model_list.html
    # model = Induction
    model = Content
    # template_name = 'home.html'
    
    # fields =['author','title',]

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ContentListView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the Baklawa
        context['inductions'] = Induction.objects.all()
        context['preambles'] = Preamble.objects.all()
        context['research'] = Research.objects.all()
        context['scriptsuggestions'] = ScriptSuggestion.objects.all()
        context['stockscripts'] = StockScript.objects.all()
        return context

class PreambleDetailView(DetailView):
    model = Preamble
    context_object_name = 'preambles'

class InductionDetailView(DetailView):
    model = Induction
    context_object_name = 'inductions'
    
class ResearchDetailView(DetailView):
    model = Research
    context_object_name = 'research'
    

class ScriptSuggestionDetailView(DetailView):
    model = ScriptSuggestion
    context_object_name = 'scriptsuggestions'

class StockScriptDetailView(DetailView):
    model = StockScript
    context_object_name = 'stockscripts'


    
'''def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ContentDetailView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the Baklawa
        context['preambles'] = Preamble.objects.all()
        #context['research'] = Research.objects.all()
        context['scriptsuggestions'] = ScriptSuggestion.objects.all()
        context['stockscripts'] = StockScript.objects.all()
        return context'''