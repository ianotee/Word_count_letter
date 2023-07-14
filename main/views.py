from django.shortcuts import render

def base(request):
    return render(request, "base.html")

def home(request):

    name = "THE WORD COUNTER"
    return render(request, "home.html", {'name':name})

def counter(request):

    noun = "The Amount of Words is"
    text = request.POST['text']

    amount = len(text.split())
    return render(request, "counter.html", {"amount": amount}, {'noun':noun})
