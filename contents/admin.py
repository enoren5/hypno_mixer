from django.contrib import admin
from .models import Preamble,Induction, ScriptSuggestion, Research, StockScript, NYTimes, TorStar, WSJournal,AssortedPeriodicals,AssortedLiterature,Binaurals

admin.site.register(Preamble)
admin.site.register(Induction)
admin.site.register(ScriptSuggestion)
admin.site.register(Research)
admin.site.register(StockScript)
admin.site.register(NYTimes)
admin.site.register(TorStar)
admin.site.register(WSJournal)
# admin.site.register(AssortedPeriodicals)

@admin.register(AssortedPeriodicals)
class AssortedPeriodicalsAdmin(admin.ModelAdmin):
    list_display = ("title","media_type", "author_last_name", "publication_year")    
    
@admin.register(AssortedLiterature)
class AssortedLiteratureAdmin(admin.ModelAdmin):
    list_display = ("title", "media_type", "author_last_name", "publication_year")

@admin.register(Binaurals)
class BinauralsAdmin(admin.ModelAdmin):
    list_display = ("title", "author_last_name", "publication_year")