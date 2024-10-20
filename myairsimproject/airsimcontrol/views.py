from django.http import JsonResponse
from .airsim_client import AirSimDroneClient

airsim_client = AirSimDroneClient()

from django.shortcuts import render

def index(request):
    return render(request, 'airsimcontrol/index.html')

def takeoff_view(request):
    airsim_client.takeoff()
    return JsonResponse({'status': 'Takeoff initiated'})

def land_view(request):
    airsim_client.land()
    return JsonResponse({'status': 'Landing initiated'})

def move_view(request):
    x = float(request.GET.get('x', 0))
    y = float(request.GET.get('y', 0))
    z = float(request.GET.get('z', 0))
    airsim_client.move_to_location(x, y, z)
    return JsonResponse({'status': 'Move initiated'})

def state_view(request):
    state = airsim_client.get_state()
    return JsonResponse(state.to_dict(), safe=False)