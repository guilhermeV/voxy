from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from .forms import WordCounterForm
from collections import Counter
import re

def index(request):
    return HttpResponse("Hello moto")
    
def get_text(request):
    result = {'quantity': '?', 'distinct': '?'}
    if request.method == 'POST':
        form = WordCounterForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            result = counter(form.cleaned_data['text_block'])
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return render(request, 'name.html', {'form': form, 'result': result})        

    else:
        form = WordCounterForm()
        
    return render(request, 'name.html', {'form': form, 'result': result})
    
def counter(text_block):
    cnt = Counter(text_block)
    words = re.findall(r'\w+', text_block.lower())
    return {'quantity': len(words), 'distinct': len(Counter(words))}