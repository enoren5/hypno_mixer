from django.urls import path
from .views import ContentListView # ThankYouView, ContactFormView, TeacherCreateView

app_name = 'contents'

urlpatterns = [
    path('', ContentListView.as_view(), name='home'),
]