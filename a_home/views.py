from django.shortcuts import render, redirect
from .forms import EssayOrderForm

# Create your views here.
def home(request):
    return render (request, 'a_home/index.html')
def about(request):
    return render (request, 'a_home/about.html')
def contact(request):
    return render (request, 'a_home/contact.html')
def services(request):
    return render (request, 'a_home/services.html')
def resume(request):
    return render (request, 'a_home/resume.html')
def portfolio(request):
    return render (request, 'a_home/portfolio.html')

def order_essay(request):
    if request.method == 'POST':
        form = EssayOrderForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'a_home/thank_you.html')
        else:
            return render (request, 'a_home/order_form.html', {'form': form})
    else:
        form = EssayOrderForm()
    return render(request, 'a_home/order_form.html', {'form': form})
