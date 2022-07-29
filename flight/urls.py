
from rest_framework import routers #! view da wiewset kullandığımız için bizim burada router yapısı kullanmamız gerekiyor. Bu bize  CRUD işlemlerinin hepsi için kendi url tanımlıyor.
from .views import FlightView, ReservationView

router = routers.DefaultRouter()
router.register('flights', FlightView)
router.register('resv', ReservationView)


urlpatterns = [
    # path('', include(router.urls))
]

urlpatterns += router.urls
