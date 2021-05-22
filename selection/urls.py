from django.contrib import admin
from django.urls import path
from rest_framework import routers
from .views import(
    CandidateViewSet,
    ContactViewSet
)
from rest_framework.documentation import include_docs_urls

router = routers.DefaultRouter()

router.register(r'candidate', CandidateViewSet, basename='candidate')
router.register(r'contact', ContactViewSet, basename='contact')


urlpatterns = [
    path('docs/', include_docs_urls(title='Selection Api',
                                    authentication_classes=[], permission_classes=[])),   
]

urlpatterns += router.urls