from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from news.views import index, NewspaperListView, \
    NewspaperDetailView, RedactorCreateView, \
    RedactorListView, TopicListView, RedactorDetailView, \
    TopicCreateView, TopicUpdateView, TopicDeleteView, \
    RedactorDataUpdateView, RedactorDeleteView, \
    NewspaperCreateView, NewspaperUpdateView, \
    NewspaperDeleteView, NewspaperPublishersUpdateView

urlpatterns = [
    path("", index, name="index"),
    path("newspapers/", NewspaperListView.as_view(), name="newspaper-list"),
    path("newspapers/<int:pk>/", NewspaperDetailView.as_view(), name="newspaper-detail"),
    path("newspapers/create/", NewspaperCreateView.as_view(), name="newspaper-create"),
    path("newspapers/<int:pk>/update/", NewspaperUpdateView.as_view(), name="newspaper-update"),
    path("newspapers/<int:pk>/update_publishers/", NewspaperPublishersUpdateView.as_view(), name="update-publishers"),
    path("cars/<int:pk>/delete/", NewspaperDeleteView.as_view(), name="newspaper-delete"),
    path("redactors/", RedactorListView.as_view(), name="redactor-list"),
    path("redactors/<int:pk>/", RedactorDetailView.as_view(), name="redactor-detail"),
    path("redactors/register/", RedactorCreateView.as_view(), name="redactor-register"),
    path("redactors/<int:pk>/update/", RedactorDataUpdateView.as_view(),name="redactor-update"),
    path("redactors/<int:pk>/delete/", RedactorDeleteView.as_view(),name="redactor-delete"),
    path("topics/", TopicListView.as_view(), name="topic-list"),
    path("topics/create/", TopicCreateView.as_view(), name="topic-create",),
    path("topics/<int:pk>/update/", TopicUpdateView.as_view(), name="topic-update"),
    path("topics/<int:pk>/delete/", TopicDeleteView.as_view(),name="topic-delete")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

app_name = "news"
