from .form import UserSignUpForm
from .models import User
from django.http import HttpResponse
from django.shortcuts import render,redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserCreateSerializer


def index(request):
    count = User.objects.count()
    total = User.objects.all()
    context = {
        'count':count,
        'total':total,
    }
    return render(request,'users/index.html',context)

def signup(request):
    form = UserSignUpForm()
    errors = []
    message = None
    if request.method=="POST":
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            message = "New user created"
            return redirect('../signup')
        else:
            errors = form.errors
    print(errors)
    print(message)
    context = {
        'form':form,
        'errors':errors,
        'message':message,
    }
    return render(request,'users/signup.html',context)


@api_view(['POST'])
def create_user(request):
    serializer = UserCreateSerializer(data=request.data)
    response_data = {
        'errors':{},
        'data':'',
    }
    if serializer.is_valid():
        user = serializer.save()
        response_status = status.HTTP_201_CREATED
        response_data['data'] = {'id':user.id}
    else:
        response_data['errors'] = serializer.errors
        response_status = status.HTTP_400_BAD_REQUEST


    return Response(response_data,status=response_status)