from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import WordCounterForm
from collections import Counter
import re

def index(request):
    return HttpResponse("Hello moto")
    
def get_text(request):
    if request.method == 'POST':
        form = WordCounterForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            counter(form.cleaned_data['text_block'])
            
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    else:
        form = WordCounterForm()

    return render(request, 'name.html', {'form': form})
    
def counter(text_block):
    cnt = Counter(text_block)
    words = re.findall(r'\w+', text_block.lower())
    print len(words)
    print len(Counter(words))
    