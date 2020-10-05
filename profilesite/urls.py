from django.urls import path
from . import views
from .views import router

urlpatterns = router.urls