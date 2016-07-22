from django.shortcuts import render, render_to_response

from django.template import RequestContext

# Create your views here.

def screen_home(request):
    return render_to_response('screen_home.html', context_instance=RequestContext(request))

