# wigs/views.py
from django.contrib.auth import get_user_model
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, status, generics
from rest_framework.permissions import IsAuthenticated  
from .models import Wig
from .serializers import WigSerializer, CustomizeWigSerializer, PurchaseWigSerializer, SwitchUserSerializer

class UserDetailsViewSet(generics.RetrieveAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = SwitchUserSerializer  
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)

class WigViewSet(viewsets.ModelViewSet):
    queryset = Wig.objects.all()
    serializer_class = WigSerializer
    permission_classes = [IsAuthenticated]  

    @action(detail=True, methods=['post'])
    def purchase(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = PurchaseWigSerializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(purchaser=request.user)
        return Response({'status': 'purchased'}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def customize(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = CustomizeWigSerializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @action(detail=False, methods=['post'])
    def switch_user(self, request, *args, **kwargs):
        serializer = SwitchUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        username_to_switch = serializer.validated_data['username']
        
        try:
            user_to_switch = get_user_model().objects.get(username=username_to_switch)
            request.user = user_to_switch
            return Response({'status': 'user switched'}, status=status.HTTP_200_OK)
        except get_user_model().DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
