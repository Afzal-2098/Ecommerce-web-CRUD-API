from rest_framework.views import APIView
from .serializers import ProductSeriarizer
from .models import Product
from rest_framework.response import Response
from rest_framework import status


# Crud operations class
class ProductApi(APIView):
    # function for get product data
    def get(self, request, pk=None, format=None):
        if pk is not None:
            prod = Product.objects.get(pk=pk)
            serializer = ProductSeriarizer(prod)
            return Response(serializer.data, status=status.HTTP_200_OK)

        prod = Product.objects.all()
        serializer = ProductSeriarizer(prod, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    # function for update complete product's data
    def put(self, request, pk, format=None):
        id = pk
        prod = Product.objects.get(pk=id)
        serializer = ProductSeriarizer(prod, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete Data Updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    # function for update product's data partially
    def patch(self, request, pk, format=None):
        id = pk
        prod = Product.objects.get(pk=id)
        serializer = ProductSeriarizer(prod, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partial Data Updated'})
        return Response(serializer.errors)


    # function for inserting new data into database
    def post(self, request, format=None):
        serializer = ProductSeriarizer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'New Data Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    # function for deleting prticular data from the database
    def delete(self, request, pk, format=None):
        id = pk
        prod = Product.objects.get(pk=id)
        prod.delete()
        return Response({'msg':'Data Deleted'}, status=status.HTTP_204_NO_CONTENT)