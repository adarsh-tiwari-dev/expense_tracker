# from django.shortcuts import render
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Expense
from .serializers import ExpenseSerializer
from django.db.models import Sum, Count, Avg, FloatField
from django.db.models.functions import TruncMonth
from rest_framework.decorators import action
from rest_framework.response import Response


from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwner
from rest_framework_simplejwt.tokens import RefreshToken



# Create your views here.

class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
        ]
    filterset_fields = ['category','date']
    search_fields = ['category','description']
    ordering_fields = ['amount','date','created_at']
    ordering = ['-date']

    def get_queryset(self):
        return Expense.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=False, methods=['get'])
    def summary(self, request):
        data = (
            Expense.objects
            .filter(user=request.user)
            .annotate(month=TruncMonth('date'))
            .values('month')
            .annotate(
                total=Sum('amount',output_field=FloatField()),
                count=Count('id'),
                average=Avg('amount', output_field=FloatField())
            )
            .order_by('month')
        )
        return Response(data)
    
@api_view(['POST'])
def register_user(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if User.objects.filter(username=username).exists():
        return Response({"error": "User already exists"}, status=400)

    user = User.objects.create_user(username=username, password=password)
    return Response({"message": "User created successfully"}, status=201)


@api_view(['POST'])
def logout_user(request):
    try:
        refresh_token = request.data["refresh"]
        token = RefreshToken(refresh_token)
        token.blacklist()
        return Response({"message": "Logged out successfully"})
    except Exception as e:
        return Response({"error": "Invalid token"},status=400)

   
