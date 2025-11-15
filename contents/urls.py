from django.urls import path, include
from .views import ContentListView, InductionDetailView,ResearchDetailView, PreambleDetailView, ScriptSuggestionDetailView,StockScriptDetailView,NYTimesDetailView,TorStarDetailView,WSJournalDetailView # AssortedPeriodicalsListView # index

app_name = 'contents'

urlpatterns = [
    path('', ContentListView.as_view(),name='home'), 
    #path('', AssortedPeriodicalsListView.as_view(),name='assorted_periodicals'), 
    path('preambles/<str:slug>', PreambleDetailView.as_view(),name='preamble_details'), 
    path('inductioning/<str:slug>', InductionDetailView.as_view(),name='induction_details'), 
    path('scripting/<str:slug>', ScriptSuggestionDetailView.as_view(),name='scriptsuggestion_detail'), 
    path('stock_scripting/<str:slug>', StockScriptDetailView.as_view(),name='stockscript_detail'), 
    path('researching/<str:slug>', ResearchDetailView.as_view(),name='research_detail'), 
    path('nytimesing/<str:slug>', NYTimesDetailView.as_view(),name='nytimes_detail'), 
    path('torstaring/<str:slug>', TorStarDetailView.as_view(),name='torstar_detail'), 
    path('wsj-ing/<str:slug>', WSJournalDetailView.as_view(),name='wsj_detail'), 
]

    