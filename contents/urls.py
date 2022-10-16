from django.urls import path, include
from .views import ContentListView, InductionDetailView,ResearchDetailView, PreambleDetailView, ScriptSuggestionDetailView,StockScriptDetailView # index

app_name = 'contents'

urlpatterns = [
    path('', ContentListView.as_view(),name='home'), 
    path('preambles/<str:slug>', PreambleDetailView.as_view(),name='preamble_details'), 
    path('inductioning/<str:slug>', InductionDetailView.as_view(),name='induction_details'), 
    path('scripting/<str:slug>', ScriptSuggestionDetailView.as_view(),name='scriptsuggestion_detail'), 
    path('stock_scripting/<str:slug>', StockScriptDetailView.as_view(),name='stockscript_detail'), 
    path('researching/<str:slug>', ResearchDetailView.as_view(),name='research_detail'), 
]

    