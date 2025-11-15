from django.contrib import admin

# Register your models here.
from .models import Preamble,Induction, ScriptSuggestion, Research, StockScript, NYTimes, TorStar, WSJournal

admin.site.register(Preamble)
admin.site.register(Induction)
admin.site.register(ScriptSuggestion)
admin.site.register(Research)
admin.site.register(StockScript)
admin.site.register(NYTimes)
admin.site.register(TorStar)
admin.site.register(WSJournal)
