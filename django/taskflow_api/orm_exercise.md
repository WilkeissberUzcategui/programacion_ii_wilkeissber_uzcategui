from tasks.models import autobus

autobus.objects.all()
<QuerySet []>

>>> autobus.objects.get(aerolinea="MC Maria")
<autobus: MC Maria>

