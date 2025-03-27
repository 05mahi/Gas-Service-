from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import ServiceRequest
from .forms import ServiceRequestForm
from django.shortcuts import render

@login_required
def create_service_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.user = request.user
            service_request.save()
            return redirect('service_request_list')
    else:
        form = ServiceRequestForm()
    return render(request, 'service_request_form.html', {'form': form})

@login_required
def service_request_list(request):
    requests = ServiceRequest.objects.filter(user=request.user)
    return render(request, 'service_request_list.html', {'requests': requests})

def home(request):
    return render(request, 'home.html')