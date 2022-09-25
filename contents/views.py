from django.shortcuts import render
from django.views.generic import ListView
from .models import Induction, Research, ScriptSuggestions


class ContentListView(ListView):
    # model_list.html
    model = Induction

