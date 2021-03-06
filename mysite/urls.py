from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView

from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls

from search import views as search_views

from django.urls import path, include
from rest_framework import routers
from home.views import HomePageViewSet
from rest_framework.schemas import get_schema_view

router = routers.DefaultRouter()
router.register(r'homepages', HomePageViewSet)

# API
api_patterns = [
    path('api/', include(router.urls)),
]

# Open api schema
urlpatterns = [
    url('openapi', get_schema_view(
    title='My test API',
    url='http://127.0.0.1:8000/',
    patterns=api_patterns,
    ))
]

urlpatterns += api_patterns

urlpatterns += [
    path('', include('frontend.urls')),
]


urlpatterns += [

    url(r'^django-admin/', admin.site.urls),

    url(r'^admin/', include(wagtailadmin_urls)),
    url(r'^documents/', include(wagtaildocs_urls)),

    url(r'^search/$', search_views.search, name='search'),

]


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = urlpatterns + [
    # For anything not caught by a more specific rule above, hand over to
    # Wagtail's page serving mechanism. This should be the last pattern in
    # the list:
    url(r"", include(wagtail_urls)),

    # Alternatively, if you want Wagtail pages to be served from a subpath
    # of your site, rather than the site root:
    #    url(r"^pages/", include(wagtail_urls)),
]
