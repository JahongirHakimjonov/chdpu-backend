def get_domain():
    from django.contrib.sites.models import Site

    return Site.objects.get_current().domain
