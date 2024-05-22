from django.http import HttpResponse
from django.shortcuts import render, redirect
from image_app.forms import HotelForm
from image_app.models import Hotel

# Create your views here.
def home(request):

	if request.method == 'POST':
		form = HotelForm(request.POST, request.FILES)

		if form.is_valid():
			form.save()
			return redirect('display.html')
	else:
		form = HotelForm()
	return render(request, 'home.html', {'form': form})
def display(request):
	Hotels = Hotel.objects.all()
	return render(request, 'display.html',{'hotel_images': Hotels})
def success(request):
	return HttpResponse('successfully uploaded')
def delete(request,id):
	em=Hotel.objects.get(id=id)
	em.delete()
	return redirect('/display.html')
