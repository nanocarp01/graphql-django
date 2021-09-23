from django.shortcuts import get_object_or_404, get_list_or_404, render, redirect
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required

#@login_required()
def index(request):
    #print('username: %s' % request.user.username)
  
    return render(request, 'logs/index.html')