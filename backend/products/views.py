from rest_framework import generics

from .models import Product
from .serializers import  ProductSerializer


# Create your views here.

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    #lookup_field = pk?
pdv = ProductDetailAPIView.as_view()
    
    
class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class=ProductSerializer
    def perform_create(self, serializer):
        print(serializer.validated_data)
        title = serializer.validated_data.get('name')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title        
        serializer.save()
plcv = ProductListCreateAPIView.as_view()