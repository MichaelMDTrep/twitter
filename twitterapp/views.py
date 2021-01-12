from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from twitterapp.forms import LoginForm, SignUpForm
from twitterapp.models import MyUser
from twitterapp.models import Tweet


def index(request):
    Tweets = Tweet.objects.all().order_by("-id")
    return render(
        request,
        "index.html",
        {"twitterapp": Tweets}
    )


def history(request):
    Tweets = Tweet.objects.filter().order_by()
    return render(request, "history.html", {"Tweets": Tweets})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, username=data["username"], password=data["password"]
            )
            if user:
                login(request, user)
                return HttpResponseRedirect(
                    request.GET.get("next", reverse("homepage"))
                )

    form = LoginForm()
    return render(request, "generic_form.html", {"form": form})


def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse("homepage"))


def sign_up(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            newuser = MyUser.objects.create_user(
                username=data.get("username"),
                password=data.get("password"),
                first_name=data.get("first_name"),
                last_name=data.get("last_name"),
                age=data.get("age"),
            )
            login(request, newuser)
        return HttpResponseRedirect(reverse("homepage"))

    form = SignUpForm()
    return render(request, "generic_form.html", {"form": form})
