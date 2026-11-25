from transporte.views.parada_views import parada_list, parada_detail
from transporte.views.conductor_views import conductor_list, conductor_detail
from transporte.views.ruta_views import ruta_list, ruta_detail, ruta_create, ruta_update, ruta_delete
from transporte.views.vehiculo_views import (
    vehiculo_list, vehiculo_detail, vehiculo_create, vehiculo_update, vehiculo_delete,
)
from transporte.views.auth_views import registro, login_view, logout_view