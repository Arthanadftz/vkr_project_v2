from django.shortcuts import render
from django.utils.safestring import mark_safe
from django.contrib.auth.decorators import login_required

import json

# Create your views here.
def chat_index(request):
    return render(request, 'chat_index.html', {})

@login_required
def chat_select(request):
    return render(request, 'chat_select.html', {})

@login_required
def chat_room(request, room_name):
    return render(request, 'room.html',   #chat_room.html chat_room_test.html
    {
        'room_name_json': mark_safe(json.dumps(room_name)),
        'username': mark_safe(json.dumps(request.user.username))
    })
