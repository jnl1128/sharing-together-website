from django.shortcuts import render
from django.utils.safestring import mark_safe
import json


def be_together(request):
    return render(request, 'be_together.html', {})


def room(request, room_name):
    return render(request, 'room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })
