from rest_framework import generics, mixins , permissions, authentication
from rest_framework.decorators import api_view
from rest_framework.response import Response

from  django.shortcuts import get_object_or_404

from .models import Product
from .serializers import  ProductSerializer
from .permissions import IsStaffEditorPermission
from api.authentication import TokenAuthentication


# Create your views here.

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    #lookup_field = pk?
pdv = ProductDetailAPIView.as_view()
    
    
class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class=ProductSerializer
    permission_classes = [permissions.IsAdminUser,
                          IsStaffEditorPermission,
                          ]
    
    def perform_create(self, serializer):
        print(serializer.validated_data)
        title = serializer.validated_data.get('name')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title        
        serializer.save(content=content)
plcv = ProductListCreateAPIView.as_view()


class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.DjangoModelPermissions]
    
    lookup_field = 'pk'
    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title
puv = ProductUpdateAPIView.as_view()


class ProductDeleteAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    #lookup_field = 'pk'
    
    def perform_destroy(self, instance):
        super().perform_destroy(instance)
pdev = ProductDeleteAPIView.as_view()

class ProductMixinView(mixins.ListModelMixin,
                       mixins.CreateModelMixin,
                       mixins.RetrieveModelMixin,
                       generics.GenericAPIView,
                       ):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    
    def get(self, request, *args, **kwargs):
        print(args, kwargs)
        pk = kwargs.get('pk')
        if pk != None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    def perform_create(self, serializer):
        print(serializer.validated_data)
        title = serializer.validated_data.get('name')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title        
        serializer.save(content=content)
    
pmv= ProductMixinView.as_view()
    

"""
@api_view(['GET','POST'])
def Product_alt_view(request, pk=None, *args, **kwargs):
    method = request.method 
    
    if method == 'GET':
        if pk != None:
            obj = get_object_or_404(Product, pk=pk)
            data = ProductSerializer(obj, many=False).data
            return Response(data)
        
    
        qs = Product.objects.all()
        data = ProductSerializer(qs , many= True).data
        return Response(data)
        
    
    
    if method == 'POST':
    
        serializer=ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get('name')
            content = serializer.validated_data.get('content') or None
            if content is None:
                content = title  
            #print(type(serializer.data))
            instance = serializer.save(content=content)
            print(type(instance))
            data = serializer.data
            print(type(data))                   
            return Response(data)
        
dpav = Product_alt_view
"""