
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect, HttpResponse, render_to_response, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login
import json

def mygetview(request):
    if request.method == 'GET':

        print("**get**")
        data = request.GET['mydata']
        astr = "<html><b> get request가 들어왔습니다. </b> <br> returned data: %s</html>" % data
        return HttpResponse(astr)
    return render(request)

def mypostview(request):
    if request.method == 'POST':
        print("**post**")
        data = request.POST['mydata']
        astr = "<html><b> post request가 들어왔습니다 </b> <br> returned data: %s</html>" % data
        return HttpResponse(astr)
    return render(request)

def myajaxview(request):
    if request.method == 'POST':
        if request.is_ajax():
            print ("**ajax post**")
            data = request.POST['mydata']
            astr = "<html><b> ajax post request가 들어왔습니다. </b> <br> returned data: %s</html>" % data
            return HttpResponse(astr)
    return render(request)

def myajaxformview(request):
    if request.method == 'POST':
        if request.is_ajax():
            import json

            print ("**ajax form post**")
            for k,v in request.POST.items():
                print(k,v)

            print ("field1 data: %s" % request.POST['field1'])
            print ("field2 data: %s" % request.POST['field2'])

            mydata = [{'name':'혜림', 'etc':2}]
            return HttpResponse(json.dumps(mydata), content_type="application/json")

    return render(request)

def foo(request,template='ajx/foo.html'):
    return render(request,template)
