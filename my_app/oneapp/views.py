from django.shortcuts import render
from .forms import contactform
from django.core.mail import send_mail


    
def indexpage(request):
    submitted = False
    form = contactform()
    if request.method == 'POST':
        form = contactform(request.POST)
        if form.is_valid():
            form.save()
        else:
            form = contactform
            if 'submmitted' in request.GET:
                submitted = True

    template_name = 'index.html'
    return render(request, template_name, context={'form':form, 'submitted':submitted})


    






