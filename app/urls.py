from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from app.views import companyview,employeeview


router = routers.DefaultRouter()
router.register(r'companies',companyview)
router.register(r'employees',employeeview)


urlpatterns = [
    path('', include(router.urls)),
]