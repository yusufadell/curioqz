from django.conf import settings


def allauth_settings(request):
    """Expose some settings from django-allauth in templates.

    :param request:

    """
    return {
        "ACCOUNT_ALLOW_REGISTRATION": settings.ACCOUNT_ALLOW_REGISTRATION,
    }
