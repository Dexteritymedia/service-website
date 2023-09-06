from django.shortcuts import render, redirect

from .models import FeedBack
from .forms import FeedBackForm
# Create your views here.


def all_reviews(request):
    reviews = FeedBack.objects.all().order_by('-date_submitted')
    context = {'reviews': reviews}
    return render(request, 'all_reviews.html', context)

def submit_review(request):
    context = {}
    """Let user add a review"""
    if request.method == 'POST':
        form = FeedBackForm(data=request.POST)
        if form.is_valid():
            new_review = form.save(commit=False)
            new_review.save()
            return redirect('/')
    else:
        form = FeedBackForm()
        context = {'form': form}
    return render(request, 'submit_review.html', context)
