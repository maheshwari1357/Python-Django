from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_dict={
    "jan":"January",
    "feb":"Febrauary",
    "mar":"March",
    "apr":"April",
    "may":"May"
}

def index(request):
    list_items=""
    month=list(monthly_dict.keys())
    for i in month:
        month_path=reverse("month-challenge",args=[i])
        list_items+=f"<li><a href=\"{month_path}\">{i.capitalize()}</a></li>"
    response_data=f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)

def monthly_challenge_num(request, month):
    redirect_month=list(monthly_dict.keys())[month-1]
    return HttpResponseRedirect("/challenges/"+redirect_month)


def monthly_challenge(request,month):
    try:
        return HttpResponse(monthly_dict[month])
    except:
        return HttpResponseNotFound("Not supported")