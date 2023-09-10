from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

monthly_dict={
    "jan":"January",
    "feb":"Febrauary",
    "mar":"March",
    "apr":"April",
    "may":"May"
}

def monthly_challenge_num(request, month):
    redirect_month=list(monthly_dict.keys())[month-1]
    return HttpResponseRedirect("/challenges/"+redirect_month)


def monthly_challenge(request,month):
    try:
        return HttpResponse(monthly_dict[month])
    except:
        return HttpResponseNotFound("Not supported")