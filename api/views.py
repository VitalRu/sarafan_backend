# from products.models import Product
from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.serializers import ProductSerializer


@api_view(['GET'])
def api_home(request, *args, **kwargs):

    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        print(serializer.data)
        return Response(serializer.data)
    return Response({'invalid': 'not good data'}, status=400)
