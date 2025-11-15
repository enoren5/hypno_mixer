from .models import AuthToggle

def auth_vars(request):
    """Return latest AuthToggle values for templates."""
    try:
        obj = AuthToggle.objects.order_by('-pk').first()
        return {
            'auth_email': obj.email if obj else '',
            'auth_linkedin': obj.linkedin if obj else '',
            'auth_github': obj.github if obj else '',
            'auth_name': obj.name if obj else '',
        }
    except Exception:
        return {'auth_email': '', 'auth_linkedin': '','auth_github':'','name_github':'',}