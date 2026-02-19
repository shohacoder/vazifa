from django.shortcuts import render

from .models import ServiceCategory, Service, Mechanic

def view_all(request):
    service_categories = ServiceCategory.objects.all()
    services = Service.objects.all()
    mechanics = Mechanic.objects.all()

    context = {
        'service_categories' : service_categories,
        'services' : services,
        'mechanics' : mechanics
    }

    return render(request, 'core/index.html', context)


def service_by_category(request, category_id):
    service_categories = ServiceCategory.objects.all()
    mechanics = Mechanic.objects.all()
    services = Service.objects.filter(
        category_id=category_id,
        is_available=True
    )

    context = {
        'service_categories' : service_categories,
        'services' : services,
        'mechanics' : mechanics
    }

    return render(request, 'core/index.html', context)

def service_detail(request, pk):
    service =  Service.objects.get(pk=pk)
    mechanicss = Service.objects.filter(machenic = service.mechanic, is_available = True)

    context = {
        "service" : service,
        'mechanics' : mechanicss
    }

    return render(request, "core/detail.html", context)




def servise_by_mechanic(request, mechanic_id):
    service_categories = ServiceCategory.objects.all()
    mechanics = Mechanic.objects.all()
    services = Service.objects.filter(
        mechanic_id=mechanic_id,
        is_available=True
    )

    context = {
        'service_categories': service_categories,
        'mechanics': mechanics,
        'services': services,
    }
    return render(request, 'app/index.html', context)


