from django.http import HttpResponse

''' index will serve following '''
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
