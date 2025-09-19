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
            order = form.save()
            #send email to client
            subject= "Your Essay Order confirmation"
            message= (
                f"Hello {order.name}, \n\n"
                f"Thank you for your order! Here are your details:\n\n"
                f"Topic: {order.topic}\n"
                f"pages: {order.pages}\n"
                f"Deadline: {order.deadline}\n"
                f"Academic Level: {order.academic_level}\n"
                f"Formatting Style: {order.formatting_style}\n"
                f"Price: {order.price}\n\n"
                f"We'll contact you shortly.\n\n"
                f"Best regards, \nEssay Service Team"
            )
            try:

               send_mail(
                subject,
                message,
                "noreply@essayservice.com", #sender email
                [order.email],  #recepient (client's email)
                fail_silently=False,
            )
            except Exception as e:
             print("Email failed", e)


            return render(request, 'a_home/thank_you.html', {'order': order})
        else:
            return render (request, 'a_home/order_form.html', {'form': form})
    else:
        form = EssayOrderForm()
        return render(request, 'a_home/order_form.html', {'form': form})

