# Create your views here.

from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User 

def VediFoto(request):
    return HttpResponse('TODO !')
