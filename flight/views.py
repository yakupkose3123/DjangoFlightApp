from django.shortcuts import render
from requests import request
from .serializers import FlightSerializer, ReservationSerializer, StaffFlightSerializer
from .models import Flight, Passenger, Reservation
from rest_framework import viewsets
from .permission import IsStafforReadOnly
from datetime import datetime, date
from django.db.models import Q


class FlightView(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    permission_classes = (IsStafforReadOnly,)  #! For permission

    def get_serializer_class(self):
        serializer = super().get_serializer_class()
        if self.request.user.is_staff: #user staff sa ilgili uçuşun altındaki rezservations görsün
            return StaffFlightSerializer 
        return serializer

#! Bulunduğum zamandan sonraki uçuşları göster
    def get_queryset(self):
        now = datetime.now()
        current_time = now.strftime('%H:%M:%S')
        today = date.today()
        print(current_time)

        # if self.request.user.is_staff:
        #     return super().get_queryset()
        # else:
        #     return Flight.objects.filter(Q(date_of_departure__gte=today) | Q(date_of_departure=today, etd__gt=current_time))
     
        if self.request.user.is_staff:
            return super().get_queryset()
        else:
            queryset = Flight.objects.filter(date_of_departure__gt=today) #günü bu günden sonra olanlar
            if Flight.objects.filter(date_of_departure=today): #Bu günse saati bu saatten sonra olanlar
                today_qs = Flight.objects.filter(date_of_departure=today).filter(etd__gt=current_time)
                queryset = queryset.union(today_qs) #iki queryset i birleştir.
            return queryset




class ReservationView(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

#admin olmayan userlar da tüm reservationları görmesin diye 
    def get_queryset(self):
        queryset = super().get_queryset()
        # queryset = Reservation.objects.all() 
        if self.request.user.is_staff: #staff usersa hepsini dön
            return queryset
        return queryset.filter(user=self.request.user) #değilse user ı selfçuser olan döndür.
