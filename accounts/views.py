from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from leads.models import Lead
from activity.models import Activity
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def login_view(request):

    if request.user.is_authenticated:
        return redirect("dashboard")

    if request.method == "POST":

        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user:
            login(request, user)
            return redirect("dashboard")

        return render(
            request,
            "accounts/login.html",
            {"error": "Invalid Username or Password"}
        )

    return render(request, "accounts/login.html")


def logout_view(request):
    logout(request)
    return redirect("login")


@login_required
def dashboard(request):

    if request.user.groups.filter(name="Admin").exists():

        context = {
            "total_leads": Lead.objects.count(),
            "new_leads": Lead.objects.filter(status="New").count(),
            "won_leads": Lead.objects.filter(status="Won").count(),
            "lost_leads": Lead.objects.filter(status="Lost").count(),
            "members": User.objects.filter(groups__name="Member").count(),
            "recent_leads": Lead.objects.order_by("-created_at")[:5],
            "activities": Activity.objects.order_by("-created_at")[:5],
        }

        return render(request, "dashboard/admin_dashboard.html", context)

    leads = Lead.objects.filter(assigned_to=request.user)

    context = {
        "assigned_leads": leads,
        "total_assigned": leads.count(),
    }

    return render(request, "dashboard/member_dashboard.html", context)