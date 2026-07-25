from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Lead,Note
from .forms import LeadForm,NoteForm
from activity.models import Activity
from django.http import HttpResponseForbidden
from django.core.paginator import Paginator
from django.contrib import messages


@login_required
def lead_list(request):

    if request.user.groups.filter(name="Admin").exists():
        leads = Lead.objects.all().order_by("-created_at")
    else:
        leads = Lead.objects.filter(
            assigned_to=request.user
        ).order_by("-created_at")

    # Search
    search = request.GET.get("search")

    if search:
        leads = leads.filter(name__icontains=search)

    # Status Filter
    status = request.GET.get("status")

    if status:
        leads = leads.filter(status=status)

    # Pagination
    paginator = Paginator(leads, 10)

    page_number = request.GET.get("page")

    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "leads/lead_list.html",
        {
            "page_obj": page_obj,
            "search": search,
            "status": status,
        }
    )


from django.contrib import messages

@login_required
def add_lead(request):

    # Sirf Admin lead add kar sakta hai
    if not request.user.groups.filter(name="Admin").exists():
        return HttpResponseForbidden("Access Denied")

    if request.method == "POST":

        form = LeadForm(request.POST)

        if form.is_valid():

            lead = form.save(commit=False)
            lead.created_by = request.user
            lead.save()

            Activity.objects.create(
                lead=lead,
                user=request.user,
                action=f"Created lead '{lead.name}'"
            )

            messages.success(request, "Lead created successfully.")

            return redirect("lead_list")

    else:
        form = LeadForm()

    return render(request, "leads/lead_form.html", {
        "form": form
    })



@login_required
def edit_lead(request, id):

    lead = get_object_or_404(Lead, id=id)

    if request.method == "POST":

        form = LeadForm(request.POST, instance=lead)

        if form.is_valid():

            form.save()

            Activity.objects.create(
                lead=lead,
                user=request.user,
                action=f"Updated lead '{lead.name}'"
            )

            messages.success(request, "Lead updated successfully.")

            return redirect("lead_list")

    else:
        form = LeadForm(instance=lead)

    return render(request, "leads/lead_form.html", {
        "form": form
    })


@login_required
def delete_lead(request, id):

    lead = get_object_or_404(Lead, id=id)

    Activity.objects.create(
        lead=lead,
        user=request.user,
        action=f"Deleted lead '{lead.name}'"
    )

    lead.delete()

    messages.success(request, "Lead deleted successfully.")

    return redirect("lead_list")


@login_required
def lead_detail(request, id):

    lead = get_object_or_404(Lead, id=id)

    notes = Note.objects.filter(
        lead=lead
    ).order_by("-created_at")

    activities = Activity.objects.filter(
        lead=lead
    ).order_by("-created_at")

    if request.method == "POST":

        form = NoteForm(request.POST)

        if form.is_valid():

            note = form.save(commit=False)
            note.lead = lead
            note.user = request.user
            note.save()

            Activity.objects.create(
                lead=lead,
                user=request.user,
                action=f"Added a note to '{lead.name}'"
            )

            messages.success(request, "Note added successfully.")

            return redirect("lead_detail", id=lead.id)

    else:

        form = NoteForm()

    context = {
        "lead": lead,
        "notes": notes,
        "activities": activities,
        "form": form,
    }

    return render(
        request,
        "leads/lead_detail.html",
        context
    )