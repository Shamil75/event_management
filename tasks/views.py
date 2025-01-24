from django.shortcuts import render, redirect
from tasks.forms import EventModelForm, CategoryModelForm, ParticipantModelForm
from django.contrib import messages
from django.db.models import Q, Count, Max, Min, Avg
from tasks.models import Event, Category, Participant
# Create your views here.


def home(request):
    return render(request, "dashboard/home.html")

def dashboard(request):
    type = request.GET.get('type', 'all')

    participants = Participant.objects.all()
    total_participants = participants.count()

    categorys = Category.objects.all()

    counts = Event.objects.aggregate(
        total_event = Count('id'),
        completed = Count('id', filter=Q(status='COMPLETED')),
        in_progress = Count('id', filter=Q(status='IN_PROGRESS')),
        pending = Count('id', filter=Q(status='PENDING')),
    )

    base_query = Event.objects.all()

    if type == 'completed':
        events = base_query.filter(status='COMPLETED')
    elif type == 'in_progress':
        events = base_query.filter(status='IN_PROGRESS')
    elif type == 'pending':
        events = base_query.filter(status='PENDING')
    if type == 'all':
        events = base_query.all()

    context = {
        "events": events,
        "counts": counts,
        "total_participants": total_participants,
        "categorys": categorys,
        "participants":participants
    }
    return render(request, "dashboard/dashboard.html", context)


# for event
def create_event(request):
    task_form = EventModelForm()

    if request.method == "POST":
        task_form = EventModelForm(request.POST)

        if task_form.is_valid():
            task_form.save()
            messages.success(request, "Event Created Successfully")
            return redirect('create_event')

    context = {"task_form": task_form}
    return render(request, "form.html", context)



def update_event(request, id):
    event = Event.objects.get(id=id)
    task_form = EventModelForm(instance=event)

    if request.method == "POST":
        task_form = EventModelForm(request.POST, instance=event)

        if task_form.is_valid():
            task_form.save()

            messages.success(request, "Event Updated Successfully")
            return redirect('update_event', id)

    context = {"task_form": task_form}
    return render(request, "form.html", context)

def delete_event(request, id):
    if request.method == 'POST':
        event = Event.objects.get(id=id)
        event.delete()

        messages.success(request, 'Task Deleted Successfully')
        return redirect('dashboard')
    

# for category
def create_category(request):
    form = CategoryModelForm()

    if request.method == "POST":
        form = CategoryModelForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Category Created Successfully")
            return redirect('create_category')

    context = {"form": form}
    return render(request, "form2.html", context)

from django.shortcuts import get_object_or_404

def update_category(request, id):
    category = Category.objects.get(id=id)
    form = CategoryModelForm(instance=category)

    if request.method == "POST":
        form = CategoryModelForm(request.POST, instance=category)

        if form.is_valid():
            form.save()

            messages.success(request, "Event Updated Successfully")
            return redirect('update_category', id)

    context = {"form": form}
    return render(request, "form2.html", context)

def delete_category(request, id):
    if request.method == 'POST':
        category = Category.objects.get(id=id)
        category.delete()

        messages.success(request, 'Task Deleted Successfully')
        return redirect('dashboard')
    
# for participants

def create_participant(request):
    form = ParticipantModelForm()

    if request.method == "POST":
        form = ParticipantModelForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Participant Created Successfully")
            return redirect('create_participant')

    context = {"form": form}
    return render(request, "form3.html", context)

def update_participant(request, id):
    category = Participant.objects.get(id=id)
    form = ParticipantModelForm(instance=category)

    if request.method == "POST":
        form = ParticipantModelForm(request.POST, instance=category)

        if form.is_valid():
            form.save()

            messages.success(request, "Event Updated Successfully")
            return redirect('update_participant', id)

    context = {"form": form}
    return render(request, "form3.html", context)

def delete_participant(request, id):
    if request.method == 'POST':
        participant  = Participant.objects.get(id=id)
        participant .delete()

        messages.success(request, 'Task Deleted Successfully')
        return redirect('dashboard')