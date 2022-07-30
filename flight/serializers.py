from rest_framework import serializers
from .models import Flight, Passenger, Reservation


class FlightSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Flight
        fields = (
            "id",
            "flight_number",
            "operation_airlines",
            "departure_city",
            "arrival_city",
            "date_of_departure",
            "etd"
        )
        

class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = '__all__'
        

#?NESTED SERİALİZERS
#flıght ile passenger ı birbirine bağlamak zorundayız        
class ReservationSerializer(serializers.ModelSerializer):
    
    passenger = PassengerSerializer(many=True, required=False)
    flight = serializers.StringRelatedField()  # default read_only=True
    user = serializers.StringRelatedField()  # default read_only=True

    #flight ve user create ederken StringRelatedField read only olduğu için id leri kullanmak için alttakifieldları ekledik
    flight_id = serializers.IntegerField(write_only=True)
    user_id = serializers.IntegerField(write_only=True, required=False)
    class Meta: #Görüntü şekli bu sırada olsun
        model = Reservation
        fields =(
            "id",
            "flight",
            "flight_id",
            "user",
            "user_id",
            "passenger"
        )
    # Reservation un içinde passenger create edebilmek için  
    def create(self, validated_data):
        passenger_data = validated_data.pop('passenger')
        print(validated_data)
        validated_data['user_id'] = self.context['request'].user.id
        reservation = Reservation.objects.create(**validated_data)
        for passenger in passenger_data:
            pas = Passenger.objects.create(**passenger)
            reservation.passenger.add(pas)
        reservation.save()
        return reservation
    
#!Staff user uçuşlarla birlikte yolcuları da görmesi için yeni bir serializer olşturduk
class StaffFlightSerializer(serializers.ModelSerializer):
    
    reservations = ReservationSerializer(many=True, read_only=True) #Yukarıdaki releted name i burada kullandık
    
    class Meta:
        model = Flight
        fields = (
            "id",
            "flight_number",
            "operation_airlines",
            "departure_city",
            "arrival_city",
            "date_of_departure",
            "etd",
            "reservations",
        )