from django.shortcuts import render
from .forms import ResponseForm
import csv

def index(request):
    if request.method == 'POST':
        form = ResponseForm(request.POST)
        if form.is_valid():
            with open('responses.csv', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([form.cleaned_data['job'], form.cleaned_data['satisfaction'], form.cleaned_data['email']])
            return render(request, 'index.html')
    else:
        form = ResponseForm()

    return render(request, 'index.html', {'form': form})



