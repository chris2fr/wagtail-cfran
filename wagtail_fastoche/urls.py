from django.urls import include, path
from django.utils.translation import gettext_lazy as _
from django_fastoche import urls as django_fastoche_urls  # , views
from django_fastoche.fastoche_components import ALL_TAGS

# from django_distill import distill_path
from wagtail import urls as wagtail_urls

from wagtail_fastoche.views import SearchResultsView, TagsListView, TagView


def get_all_tags():
    for key in ALL_TAGS:
        yield ({"tag_name": key})


urlpatterns = [
    path(_("search/"), SearchResultsView.as_view(), name="cms_search"),
    path("tags/<str:tag>/", TagView.as_view(), name="global_tag"),
    path("tags/", TagsListView.as_view(), name="global_tags_list"),
    path("", include(wagtail_urls)),
] + django_fastoche_urls.urlpatterns