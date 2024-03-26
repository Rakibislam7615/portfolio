from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from . models import Message
from .forms import MessageForm
# Create your views here.
def contact(request):
    if request.method == 'POST':
        forms = MessageForm(request.POST)
        if forms.is_valid():
            forms.save()
    else:
        forms = MessageForm()
    return render(request,'contact/contact.html',{'forms':forms})