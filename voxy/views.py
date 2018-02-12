from django.shortcuts import render
from .forms import WordCounterForm
from voxy import counter
import re

def get_text(request):
    result = {'quantity': '?', 'distinct': '?'}
    if request.method == 'POST':
        form = WordCounterForm(request.POST)
        if form.is_valid():
            result = counter.count(form.cleaned_data['text_block'])
            return render(request, 'index.html', {'form': form, 'result': result})        
    else:
        form = WordCounterForm()
    return render(request, 'index.html', {'form': form, 'result': result})