from django.shortcuts import render, render_to_response, RequestContext

# Create your views here.

def home(request):
    return render(request, "index.htm", {})

def information(request):
	return render(request, "informacion.htm", {})
	#return render_to_response('information.html', context=RequestContext(request))