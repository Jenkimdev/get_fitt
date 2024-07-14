from django.shortcuts import render, redirect
from .forms import FeedbackForm
from .models import Feedback

def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thank_you')
    else:
        form = FeedbackForm()
    return render(request, 'feedback_form.html', {'form': form})

def thank_you_view(request):
    return render(request, 'thank_you.html')

def testimonials_view(request):
    feedbacks = Feedback.objects.all()
    return render(request, 'testimonials.html', {'feedbacks': feedbacks})