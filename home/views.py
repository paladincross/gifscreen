from django.shortcuts import render, render_to_response

from django.template import RequestContext

# Create your views here.

def index(request):
    return render_to_response('index.html', context_instance=RequestContext(request))

def index_blog(request):
    return render_to_response('index_blog.html', context_instance=RequestContext(request))

def index_gifscreen(request):
    return render_to_response('index_gifscreen.html', context_instance=RequestContext(request))
