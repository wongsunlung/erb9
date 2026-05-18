from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.
# def index(req):
#     return HttpResponse("<h1>Hello, world ! </h1>")

def index(request):
    # context = {
    #     'test_id': 1, context
    # }
    return render(request, "pages/index.html")
def about(request):
    return render(request, "pages/about.html")