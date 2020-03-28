from django.urls import path

from django.conf.urls import include
from rest_framework import routers
from .views import IncomeStatement, income_statement


router = routers.DefaultRouter()
# router.register('income_statement', IncomeStatement)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/income_statement', IncomeStatement.as_view()),
    path('income_statement', income_statement)
]