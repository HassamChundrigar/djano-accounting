from django.urls import path

from django.conf.urls import include
from rest_framework import routers
from .views import HeadViewSet, SubHeadViewSet, AccountSubHeadViewSet, EntryGetViewset, EntryPostViewset


router = routers.DefaultRouter()
router.register('head', HeadViewSet)
router.register('subhead', SubHeadViewSet)
router.register('account_subhead', AccountSubHeadViewSet)
# router.register('entry_get', EntryGetViewset)
router.register('entry_post', EntryPostViewset)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/entry_get', EntryGetViewset.as_view())
]