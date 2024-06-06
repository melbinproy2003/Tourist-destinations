from django.shortcuts import render, redirect
from rest_framework import generics
from .models import Destination
from .serializers import DestinationSerializer
from .forms import DestinationForm

class DestinationList(generics.ListCreateAPIView):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer

class DestinationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer

def home(request):
    destinations = Destination.objects.all()
    return render(request, 'home.html', {'destinations': destinations})

def destination_create(request):
    if request.method == 'POST':
        form = DestinationForm(request.POST, request.FILES, request=request)
        if form.is_valid():
            form.save()
            return redirect('home')  # Replace 'index' with your desired redirect URL name
    else:
        form = DestinationForm(request=request)
    return render(request, 'destination_form.html', {'form': form})

def destination_update(request, pk):
    destination = Destination.objects.get(pk=pk)
    if request.method == 'POST':
        form = DestinationForm(request.POST, request.FILES, instance=destination)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DestinationForm(instance=destination)
    return render(request, 'destination_form.html', {'form': form})

def destination_delete(request, pk):
    destination = Destination.objects.get(pk=pk)
    if request.method == 'POST':
        destination.delete()
        return redirect('colletion')
    return render(request, 'destination_confirm_delete.html', {'destination': destination})

def collections(request):
    id = request.session.get('id')
    if id is not None:
        destinations = Destination.objects.filter(by=id)
    else:
        destinations = Destination.objects.none()  # Empty QuerySet if no user ID is found
    return render(request, 'collection.html', {'destinations': destinations})