from django.shortcuts import render, redirect

users = []


def index(request):
    return render(request, 'index.html')


def index(request):
    print(request)
    context = {
        "name": "Bruno",
        "age": "23",
        "hobbies": ["chewing", "eating from the floor", "throwing up on the floor"],
        "users": users
    }
    return render(request, "index.html", context)


def new(request):
    print(request.POST["email"])
    users.append(request.POST["email"])
    return redirect("/")
