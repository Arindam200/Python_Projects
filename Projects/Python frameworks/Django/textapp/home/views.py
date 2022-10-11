from ast import Param
from os import remove
from urllib import response
from django.http import HttpRequest
from django.shortcuts import render ,HttpResponse
from gingerit.gingerit import GingerIt

# Create your views here.

def index(request):
    return render(request,"index.html")

def analyse(request):
    get_text=request.GET.get('text','default')
    remove=request.GET.get("removepunc",'off')
    upper=request.GET.get("uppercase",'off')
    lower=request.GET.get("lowercase",'off')
    spell=request.GET.get("Spelling-check",'off')
    
    done=get_text
    if remove =="on":
        if upper=="on":
            print("erfdgbdsfghfrferghfrf")
            punc='''!@#$%^&*()_+-=?/>.<,"':;'''
            analized=""
            for i in done:
                if i not in punc:
                    analized+=i
            analized=analized.upper()
            params={"your":"Remove puncuation and uppercase", "final":analized}
            return render(request,"index.html",params)
        elif lower=="on":
                punc='''!@#$%^&*()_+-=?/>.<,"':;'''
                analized=""
                for i in done:
                    if i not in punc:
                        analized+=i
                params={"your":"Remove puncuation and lowercase", "final":analized.lower()}
                return render(request,"index.html",params)
        else:

            punc='''!@#$%^&*()_+-=?/>.<,"':;'''
            analized=""
            for i in done:
                if i not in punc:
                    analized+=i
            params={"your":"Remove puncuation", "final":analized}
            return render(request,"index.html",params)
    elif upper=="on":
        print("yesss")
        params={"your":"uppercase", "final":done.upper()}
        return render(request,"index.html",params)
        
    elif lower=="on":
        params={"your":"lowercase", "final":done.lower()}
        return render(request,"index.html",params)
   
    elif spell=="on":
        parser = GingerIt()
        print(type(parser.parse(done)))
        result=parser.parse(done)['result']
        params={"your":"Remove puncuation and lowercase", "final":result}
        
        return render(request,"index.html",params)

    
    else:
        return HttpResponse("error")