from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.db.models import Q
from conf_app.models import ConferenceHall, Reservation
from conf_app.forms import HallForm, ReservationForm
from datetime import datetime

def show_halls(request):
    if 'message' in request.session:
        del request.session['message']
    halls = ConferenceHall.objects.all()
    reservations = Reservation.objects.all()
    status_d = {}
    for h in halls:
        for r in reservations:
            if h != r.hall:
                status = 'Free'
            else:
                if r.date == datetime.today():
                    status = 'Reserved'
                else:
                    status = 'Free'
        status_d[h.id] = status
    return render(request, 'show_halls.html', context={'halls': halls, 'status_d': status_d})

def show_halls_details(request):
    if 'message' in request.session:
        del request.session['message']
    halls = ConferenceHall.objects.all()
    reservations = Reservation.objects.all()
    if request.method == 'GET':
        if request.session.get('order_by'):
            if request.session.get('order_by') == 2:
                halls = ConferenceHall.objects.all().order_by('-capacity')
            elif request.session.get('order_by') == 1:
                halls = ConferenceHall.objects.all().order_by('capacity')
        return render(request, 'show_halls_details.html', context={'halls': halls, 'reservations': reservations})
    else:
        if request.POST.get('sort') == "2":
            halls = ConferenceHall.objects.all().order_by('-capacity')
            request.session['order_by'] = 2
        elif request.POST.get('sort') == "1":
            halls = ConferenceHall.objects.all().order_by('capacity')
            request.session['order_by'] = 1
        else:
            request.session['order_by'] = 0
    return render(request, 'show_halls_details.html', context={'halls': halls, 'reservations': reservations})

def add_hall(request):
    if 'message' in request.session:
        del request.session['message']
    form = HallForm()
    if request.method == 'GET':
        return render(request, 'add_hall.html', context={'form': form})
    else:
        form = HallForm(request.POST)
        name = request.POST.get('name')
        halls = ConferenceHall.objects.all()
        names = []
        for hall in halls:
            names.append(hall.name)
        if form.is_valid() and name not in names:
            form.save()
            request.session['message'] = f'{name} hall added to database.'
            return redirect('halls')
        else:
            message = 'Something went wrong. Hall was not added do database'
            form = HallForm()
            return render(request, 'add_hall.html', context={'form': form, 'message': message})

def add_reservation(request, id):
    if 'message' in request.session:
        del request.session['message']
    hall = ConferenceHall.objects.get(pk=id)
    form = ReservationForm()
    if request.method == 'GET':
        return render(request, 'add_reservation.html', context={'form': form, 'hall': hall})
    else:
        description = request.POST.get('description')
        date = datetime.strptime(request.POST.get('date'), '%Y-%m-%d')
        if date >= datetime.today():
            reservations = Reservation.objects.all()
            if len(reservations) != 0:
                for r in reservations:
                    if r.hall == hall and r.date == date.date():
                        message = 'This hall is reserved for this date'
                        return render(request, 'add_reservation.html', context={'form': form, 'message': message, 'hall': hall})
            reservation = Reservation.objects.create(date=date, hall=hall, description=description)
            request.session['message'] = f'{reservation} added to database.'
            return redirect('halls')
        else:
            message = 'Wrong date. Reservation was not added do database'
            return render(request, 'add_reservation.html', context={'form': form, 'message': message, 'hall': hall})

def new_reservation(request):
    if 'message' in request.session:
        del request.session['message']
    form = ReservationForm()
    if request.method == 'GET':
        return render(request, 'add_reservation.html', context={'form': form})
    else:
        description = request.POST.get('description')
        date = datetime.strptime(request.POST.get('date'), '%Y-%m-%d')
        if date >= datetime.today():
            reservations = Reservation.objects.all()
            if len(reservations) != 0:
                for r in reservations:
                    if r.hall == hall and r.date == date.date():
                        message = 'This hall is reserved for this date'
                        return render(request, 'add_reservation.html', context={'form': form, 'message': message, 'hall': hall})
            reservation = Reservation.objects.create(date=date, hall=hall, description=description)
            request.session['message'] = f'{reservation} added to database.'
            return redirect('halls')
        else:
            message = 'Wrong date. Reservation was not added do database'
            return render(request, 'add_reservation.html', context={'form': form, 'message': message, 'hall': hall})

