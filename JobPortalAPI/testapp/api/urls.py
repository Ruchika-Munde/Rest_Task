from django.urls import path,include
from rest_framework import routers
from testapp.api.views import HydJobCRUD,ChennaiJobCRUD,PuneJobCRUD,BloreJobCRUD

router=routers.DefaultRouter()

router.register('hydjobsinfo',HydJobCRUD)
router.register('blorjobsinfo',BloreJobCRUD)
router.register('punejobsinfo',PuneJobCRUD)
router.register('chennaijobsinfo',ChennaiJobCRUD)

urlpatterns=[
    path('',include(router.urls)),
]