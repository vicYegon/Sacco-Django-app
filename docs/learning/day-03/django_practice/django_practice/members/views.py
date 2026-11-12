from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import permission_classes

from .models import Member
from .serializers import MemberSerializer

# Create your views here.
def welcome(request):
    return HttpResponse(
        "Welcome to Sacco member management system"
    )

@api_view(["GET"])
@permission_classes([IsAdminUser])
def member_list(request):
    members = Member.objects.all()

    serializer = MemberSerializer(
        members,
        many = True
    )

    return Response(serializer.data)