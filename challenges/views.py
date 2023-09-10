from django.http import HttpResponse, HttpResponseNotFound

def january(request):
    return HttpResponse("Welcome to the Homepage of MyPage!!")

def feb(request):
    return HttpResponse("Welcome to the Second Homepage of MyPage!!")

def monthly_challenge(request,month):
    response=None
    if month== "January":
        response="January"
    elif month=="Feb":
        response="February"
    else:
        return HttpResponseNotFound("Not supported")
    return HttpResponse(response)