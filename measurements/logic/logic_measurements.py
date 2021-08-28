from ..models import Measurement

def get_all_measurements():
	measurements = Measurement.objects.all()
	return measurements

def get_measurement_by_pk(pk_e):
    measurement = Measurement.objects.get(pk = pk_e)
    return measurement

def delete_measurement_by_pk(pk_e):
    measurement = Measurement.objects.get(pk = pk_e)
    measurement.delete()
    return measurement

def update_measurement_by_pk(pk_e, value, units, place):
    measurement = Measurement.objects.get(pk = pk_e)
    measurement.value = value
    measurement.unit = units
    measurement.place = place
    measurement.save()
    return measurement