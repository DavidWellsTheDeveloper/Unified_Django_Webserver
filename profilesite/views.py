from rest_framework import viewsets
from rest_framework import routers
from .models import (
  Faq
)

from .serializers import (
  FaqSerializer
)

# Create your views here.
router = routers.DefaultRouter()

class ViewFaq(viewsets.ModelViewSet):
  serializer_class = FaqSerializer
  queryset = Faq.objects.all()

router.register(r'faq', ViewFaq)