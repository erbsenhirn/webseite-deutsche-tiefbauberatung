from django.http import HttpResponse

def suche(request):
    return HttpResponse("You're looking at question %s.")
