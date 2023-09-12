import calendar

from django.shortcuts import render, redirect
from django.utils import timezone

from .models import FeedBack
from .forms import FeedBackForm, CalendarForm
# Create your views here.

def calendar_index(request):
    current_year = timezone.now().year
    calendar_html = calendar.HTMLCalendar().formatyear(current_year)

    return render(request, 'calendar.html', {'current_year': current_year, 'calendar_html': calendar_html})


def calendar_month(request):
    current_year = timezone.now().year
    current_month = timezone.now().month
    calendar_html = calendar.HTMLCalendar().formatmonth(current_year, current_month)

    return render(request, 'calendar.html', {'current_year': current_year, 'calendar_html': calendar_html})


def search_calendar(request):
    if request.method == 'POST':
        form = CalendarForm(data=request.POST)
        if form.is_valid():
            post = form.cleaned_data
            print(post)
            current_year = int(post['year'])
            current_month = int(post['month'])
            calendar_month_html = calendar.HTMLCalendar().formatmonth(current_year, current_month)
            calendar_html = calendar.HTMLCalendar().formatyear(current_year)
            context = {'form': form, 'current_year': current_year, 'calendar_html': calendar_html, 'calendar_month_html': calendar_month_html}
            return render(request, 'calendar_form.html', context)
    else:
        form = CalendarForm()
    return render(request, 'calendar_form.html', {'form': form})


def all_reviews(request):
    reviews = FeedBack.objects.all().order_by('-date_submitted')
    context = {'reviews': reviews}
    return render(request, 'all_reviews.html', context)

def submit_review(request):
    context = {}
    """Let user add a review"""
    if request.method == 'POST':
        form = FeedBackForm(request.POST, request.FILES)
        if form.is_valid():
            new_review = form.save(commit=False)
            new_review.save()
            return redirect('/')
    else:
        form = FeedBackForm()
        context = {'form': form}
    return render(request, 'submit_review.html', context)
