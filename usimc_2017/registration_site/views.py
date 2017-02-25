
from django.core.exceptions import ObjectDoesNotExist

from rest_framework import status, generics, viewsets, mixins
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Entry

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.views.generic.edit import FormView
from . import forms

from rest_framework.decorators import api_view, permission_classes
from rest_framework_jwt.views import obtain_jwt_token

from .models import (
    USIMCUserManager,
    USIMCUser,
    Entry,
)

from . import serializers

#
# Account Management
#


def stupid_authenticate(username, password):
    try:
        user = User.objects.get(username=username)
        if user.password == password:
            return user
        else:
            return None
    except ObjectDoesNotExist:
        return None

import jwt
from django.conf import settings
from rest_framework_jwt.utils import jwt_payload_handler

def create_token(user):
    payload = jwt_payload_handler(user)
    token = jwt.encode(payload, settings.SECRET_KEY)
    return token.decode('unicode_escape')

# @api_view(['POST'])
# @permission_classes(())
# def register(request):
#     serialized = serializers.UserSerializer(data=request.data)
#     if serialized.is_valid():
#         user = serialized.create(serialized.data)
#         response = serialized.data
#         response['token'] = create_token(user)
#         return Response(response, status=status.HTTP_201_CREATED)
#     else:
#         return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes(())
def register(request):
    serialized = serializers.UserSerializer(data=request.data)
    if serialized.is_valid():
        user = serialized.create( serialized.data )
        response = serialized.data
        response['token'] = create_token(user)
        return Response(response, status=status.HTTP_201_CREATED)
    else:
        return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes(())
def login(request):
    serialized = serializers.UserLoginSerializer(data=request.data)
    if serialized.is_valid():
        username = serialized.data.get('username', '')
        password = serialized.data.get('password', '')
        print username, password
        user = stupid_authenticate( username=username, password=password)
        if user is not None:
            response = {}
            response['token'] = create_token(user)
            return Response(response, status=status.HTTP_202_ACCEPTED)
        else:
            return Response({'status': 'Invalid Credentials'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['POST'])
# @permission_classes(())
# def login(request):
#     username = request.POST.get('username', '')
#     password = request.POST.get('password', '')
#     print password, user
#     user = authenticate( username=username, password=password )
#     if user is not None:
#         response = {}
#         response['token'] = create_token(user)
#         return Response(response, status=status.HTTP_202_ACCEPTED)
#     else:
#         return Response({'status': 'Invalid Credentials'}, status=status.HTTP_400_BAD_REQUEST)





class USIMCUserViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = USIMCUser.objects.all()
    serializer_class = serializers.USIMCUserSerializer

#
# Entry Management Functions
#


@api_view(['POST'])
@permission_classes(())
def create_entry(request):
    serialized = serializers.EntryCreateSerializer(data=request.data)
    if serialized.is_valid():
        user = serialized.create(serialized.data, request.user.usimc_user)
        return Response(serialized.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)


class EntryCreate(generics.CreateAPIView):
    serializer_class = serializers.EntryCreateSerializer
    # def create(request, *args, **kwargs):
        # return status.HTTP_202_ACCEPTED
    queryset = Entry.objects.all()

    # def create(request, *args, **kwargs):
    #     serialized = serializers.EntrySerializer(data=request.data, user=request.user)
    #     if serialized.is_valid():
    #         entry = serialized.create( serialized.data )
    #         entry.usimc_user = request.user
    #         entry.save()
    #         return Response(serialized.data, status=status.HTTP_201_CREATED)
    #     else:
    #         return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)

class EntryList(generics.ListAPIView):
    """
    View all entries for a user or create new entry
    """
    serializer_class = serializers.EntrySerializer
    def get_queryset(self):
        return Entry.objects.all()

class EntryDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.EntrySerializer
    lookup_fields = ('pk')
    def get_queryset(self):
        return Entry.objects.filter(usimc_user=self.request.user.usimc_user)



