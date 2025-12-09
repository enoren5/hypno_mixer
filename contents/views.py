from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView
from .models import Preamble, Induction, Research, ScriptSuggestion,StockScript,Content,NYTimes, TorStar, WSJournal,AssortedPeriodicals,AssortedLiterature,Binaurals
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.admin.models import CHANGE, LogEntry
from django.db.models import OuterRef, Subquery
from django.contrib.contenttypes.models import ContentType
from django.db.models.functions import Cast
from django.db.models import CharField
from django.http import Http404
from django.utils.decorators import method_decorator
from gateway_defender.custom_decorator import protected_redirect
from gateway_defender.models import AuthToggle

method_decorator(protected_redirect,name='dispatch')
class ContentListView(LoginRequiredMixin,ListView):
    model = Content
    # template_name = 'home.html'   
        
    def get_context_data(self, **kwargs):
    
        # Call the base implementation first to get a context
        context = super(ContentListView, self).get_context_data(**kwargs)
        
        script_type1 = ContentType.objects.get_for_model(ScriptSuggestion)
        context['scriptsuggestions'] = ScriptSuggestion.objects.annotate(
            last_change=Subquery(
                LogEntry.objects.filter(
                    content_type=script_type1,
                    action_flag=CHANGE,
                    object_id=Cast(
                        OuterRef('id'), 
                        CharField()
                        )
                    ).order_by('-action_time').values('action_time')[:1]
                )
            ).order_by('-last_change')
        
        script_type2 = ContentType.objects.get_for_model(Research)
        context['research'] = Research.objects.annotate(
            last_change=Subquery(
                LogEntry.objects.filter(
                    content_type=script_type2,
                    action_flag=CHANGE,
                    object_id=Cast(
                        OuterRef('id'), 
                        CharField()
                        )
                    ).order_by('-action_time').values('action_time')[:1]
                )
            ).order_by('-last_change')
        
        script_type3 = ContentType.objects.get_for_model(Induction)
        context['inductions'] = Induction.objects.annotate(
            last_change=Subquery(
                LogEntry.objects.filter(
                    content_type=script_type3,
                    action_flag=CHANGE,
                    object_id=Cast(
                        OuterRef('id'), 
                        CharField()
                        )
                    ).order_by('-action_time').values('action_time')[:1]
                )
            ).order_by('-last_change')
        
        script_type4 = ContentType.objects.get_for_model(StockScript)
        context['stockscripts'] = StockScript.objects.annotate(
            last_change=Subquery(
                LogEntry.objects.filter(
                    content_type=script_type4,
                    action_flag=CHANGE,
                    object_id=Cast(
                        OuterRef('id'), 
                        CharField()
                        )
                    ).order_by('-action_time').values('action_time')[:1]
                )
            ).order_by('-last_change')
        
        script_type5 = ContentType.objects.get_for_model(NYTimes)
        context['nytimes'] = NYTimes.objects.annotate(
            last_change=Subquery(
                LogEntry.objects.filter(
                    content_type=script_type5,
                    action_flag=CHANGE,
                    object_id=Cast(
                        OuterRef('id'), 
                        CharField()
                        )
                    ).order_by('-action_time').values('action_time')[:1]
                )
            ).order_by('-last_change')
        
        script_type6 = ContentType.objects.get_for_model(TorStar)
        context['torstar'] = TorStar.objects.annotate(
            last_change=Subquery(
                LogEntry.objects.filter(
                    content_type=script_type6,
                    action_flag=CHANGE,
                    object_id=Cast(
                        OuterRef('id'), 
                        CharField()
                        )
                    ).order_by('-action_time').values('action_time')[:1]
                )
            ).order_by('-last_change')
        
        script_type7 = ContentType.objects.get_for_model(WSJournal)
        context['wsj'] = WSJournal.objects.annotate(
            last_change=Subquery(
                LogEntry.objects.filter(
                    content_type=script_type7,
                    action_flag=CHANGE,
                    object_id=Cast(
                        OuterRef('id'), 
                        CharField()
                        )
                    ).order_by('-action_time').values('action_time')[:1]
                )
            ).order_by('-last_change')
     
    
        context["assorted_literature"] = AssortedLiterature.objects.order_by("-id") 
        context["assorted_periodicals"] = AssortedPeriodicals.objects.order_by("-id") 
        context["binaurals"] = Binaurals.objects.order_by("-id") 
        
        return context

method_decorator(protected_redirect,name='dispatch')
class PreambleDetailView(LoginRequiredMixin,DetailView):
    model = Preamble
     
    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()
        pk = self.kwargs.get(self.pk_url_kwarg)
        slug = self.kwargs.get(self.slug_url_kwarg)
        if slug is not None and (pk is None or self.query_pk_and_slug):
            slug_field = self.get_slug_field()
            queryset = queryset.filter(**{slug_field: slug})
        if pk is None and slug is None:
            raise AttributeError(
            "Generic detail view %s must be called with either an object "
            "pk or a slug in the URLconf." % self.__class__.__name__
            )
        try:
            # Get the single item from the filtered queryset
            obj = queryset.get()
        except queryset.model.DoesNotExist:
            raise Http404(
                _("No %(verbose_name)s found matching the query")
                % {"verbose_name": queryset.model._meta.verbose_name}
            )
        if obj.is_published==True:
            return obj
        else:
            raise Http404('I borked this one, gotta fix it!')
    context_object_name = 'preambles'
    
    ''' if obj.is_published==False:
            raise Http404('I borked this one, gotta fix it!')
        else:
            return obj '''
        
'''
      context = {}
        context['preambles'] = super().Preamble.objects.get(is_published==True)
        context.save()
        return context
'''
    
method_decorator(protected_redirect,name='dispatch')
class InductionDetailView(LoginRequiredMixin, DetailView):
    model = Induction
    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()
        pk = self.kwargs.get(self.pk_url_kwarg)
        slug = self.kwargs.get(self.slug_url_kwarg)
        if slug is not None and (pk is None or self.query_pk_and_slug):
            slug_field = self.get_slug_field()
            queryset = queryset.filter(**{slug_field: slug})
        if pk is None and slug is None:
            raise AttributeError(
            "Generic detail view %s must be called with either an object "
            "pk or a slug in the URLconf." % self.__class__.__name__
            )
        try:
            # Get the single item from the filtered queryset
            obj = queryset.get()
        except queryset.model.DoesNotExist:
            raise Http404(
                _("No %(verbose_name)s found matching the query")
                % {"verbose_name": queryset.model._meta.verbose_name}
            )
        if obj.is_published==True:
            return obj
        else:
            raise Http404('I borked this one, gotta fix it!')
        
    context_object_name = 'inductions'

method_decorator(protected_redirect,name='dispatch')
class ScriptSuggestionDetailView(LoginRequiredMixin,DetailView):
    model = ScriptSuggestion
    
    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()
        pk = self.kwargs.get(self.pk_url_kwarg)
        slug = self.kwargs.get(self.slug_url_kwarg)
        if slug is not None and (pk is None or self.query_pk_and_slug):
            slug_field = self.get_slug_field()
            queryset = queryset.filter(**{slug_field: slug})
        if pk is None and slug is None:
            raise AttributeError(
            "Generic detail view %s must be called with either an object "
            "pk or a slug in the URLconf." % self.__class__.__name__
            )
        try:
            # Get the single item from the filtered queryset
            obj = queryset.get()
        except queryset.model.DoesNotExist:
            raise Http404(
                _("No %(verbose_name)s found matching the query")
                % {"verbose_name": queryset.model._meta.verbose_name}
            )
        if obj.is_published==True:
            return obj
        else:
            raise Http404('I borked this one, gotta fix it!')
             
    context_object_name = 'scriptsuggestions'


method_decorator(protected_redirect,name='dispatch')
class StockScriptDetailView(LoginRequiredMixin,DetailView):
    model = StockScript
    
    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()
        pk = self.kwargs.get(self.pk_url_kwarg)
        slug = self.kwargs.get(self.slug_url_kwarg)
        if slug is not None and (pk is None or self.query_pk_and_slug):
            slug_field = self.get_slug_field()
            queryset = queryset.filter(**{slug_field: slug})
        if pk is None and slug is None:
            raise AttributeError(
            "Generic detail view %s must be called with either an object "
            "pk or a slug in the URLconf." % self.__class__.__name__
            )
        try:
            # Get the single item from the filtered queryset
            obj = queryset.get()
        except queryset.model.DoesNotExist:
            raise Http404(
                _("No %(verbose_name)s found matching the query")
                % {"verbose_name": queryset.model._meta.verbose_name}
            )
        if obj.is_published==True:
            return obj
        else:
            raise Http404('I borked this one, gotta fix it!')
    context_object_name = 'stockscripts'

method_decorator(protected_redirect,name='dispatch')
class ResearchDetailView(LoginRequiredMixin, DetailView):
    model = Research    
    
    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()
        pk = self.kwargs.get(self.pk_url_kwarg)
        slug = self.kwargs.get(self.slug_url_kwarg)
        if slug is not None and (pk is None or self.query_pk_and_slug):
            slug_field = self.get_slug_field()
            queryset = queryset.filter(**{slug_field: slug})
        if pk is None and slug is None:
            raise AttributeError(
            "Generic detail view %s must be called with either an object "
            "pk or a slug in the URLconf." % self.__class__.__name__
            )
        try:
            # Get the single item from the filtered queryset
            obj = queryset.get()
        except queryset.model.DoesNotExist:
            raise Http404(
                _("No %(verbose_name)s found matching the query")
                % {"verbose_name": queryset.model._meta.verbose_name}
            )
        if obj.is_published==True:
            return obj
        else:
            raise Http404('I borked this one, gotta fix it!')
    context_object_name = 'research'
    
    
method_decorator(protected_redirect,name='dispatch')
class NYTimesDetailView(LoginRequiredMixin, DetailView):
    model = NYTimes    
    
    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()
        pk = self.kwargs.get(self.pk_url_kwarg)
        slug = self.kwargs.get(self.slug_url_kwarg)
        if slug is not None and (pk is None or self.query_pk_and_slug):
            slug_field = self.get_slug_field()
            queryset = queryset.filter(**{slug_field: slug})
        if pk is None and slug is None:
            raise AttributeError(
            "Generic detail view %s must be called with either an object "
            "pk or a slug in the URLconf." % self.__class__.__name__
            )
        try:
            # Get the single item from the filtered queryset
            obj = queryset.get()
        except queryset.model.DoesNotExist:
            raise Http404(
                _("No %(verbose_name)s found matching the query")
                % {"verbose_name": queryset.model._meta.verbose_name}
            )
        if obj.is_published==True:
            return obj
        else:
            raise Http404('I borked this one, gotta fix it!')
    context_object_name = 'nytimes'

method_decorator(protected_redirect,name='dispatch')
class TorStarDetailView(LoginRequiredMixin, DetailView):
    model = TorStar
    
    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()
        pk = self.kwargs.get(self.pk_url_kwarg)
        slug = self.kwargs.get(self.slug_url_kwarg)
        if slug is not None and (pk is None or self.query_pk_and_slug):
            slug_field = self.get_slug_field()
            queryset = queryset.filter(**{slug_field: slug})
        if pk is None and slug is None:
            raise AttributeError(
            "Generic detail view %s must be called with either an object "
            "pk or a slug in the URLconf." % self.__class__.__name__
            )
        try:
            # Get the single item from the filtered queryset
            obj = queryset.get()
        except queryset.model.DoesNotExist:
            raise Http404(
                _("No %(verbose_name)s found matching the query")
                % {"verbose_name": queryset.model._meta.verbose_name}
            )
        if obj.is_published==True:
            return obj
        else:
            raise Http404('I borked this one, gotta fix it!')
    context_object_name = 'torstar'

method_decorator(protected_redirect,name='dispatch')
class WSJournalDetailView(LoginRequiredMixin, DetailView):
    model = WSJournal    
    
    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()
        pk = self.kwargs.get(self.pk_url_kwarg)
        slug = self.kwargs.get(self.slug_url_kwarg)
        if slug is not None and (pk is None or self.query_pk_and_slug):
            slug_field = self.get_slug_field()
            queryset = queryset.filter(**{slug_field: slug})
        if pk is None and slug is None:
            raise AttributeError(
            "Generic detail view %s must be called with either an object "
            "pk or a slug in the URLconf." % self.__class__.__name__
            )
        try:
            # Get the single item from the filtered queryset
            obj = queryset.get()
        except queryset.model.DoesNotExist:
            raise Http404(
                _("No %(verbose_name)s found matching the query")
                % {"verbose_name": queryset.model._meta.verbose_name}
            )
        if obj.is_published==True:
            return obj
        else:
            raise Http404('I borked this one, gotta fix it!')
    context_object_name = 'wsj'

'''
class AssortedPeriodicalsListView(ListView):
    model = AssortedPeriodicals
    template_name = "content_list.html"
    context_object_name = "assorted_periodicals"
'''