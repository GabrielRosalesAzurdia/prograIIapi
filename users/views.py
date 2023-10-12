from rest_framework import viewsets, permissions
from django.contrib.auth import get_user_model
from .serializer import UserSerializer
from rest_framework.decorators import api_view, permission_classes
from sells.models import Receipt
from sells.serializer import ReceiptSerializer
from rest_framework.response import Response

class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

# Gets a client related receipts
# @csrf_exempt
@api_view(['GET'])
@permission_classes((permissions.IsAuthenticated,))
def userReceipts(request):
    queryset = Receipt.objects.filter(employee = request.user.id)
    serializer = ReceiptSerializer(queryset, many=True)
    return Response(serializer.data)