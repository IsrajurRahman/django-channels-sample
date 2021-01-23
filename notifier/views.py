from django.shortcuts import render, redirect
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
import time


def index(request):
    return render(request, 'home.html')

def status_form(request):
    if request.method =='POST':
        num = int(request.POST['TB_sample'])
        progress = 10
        for i in range(num):
            room_group_name = f'notify'
            status = "running....."
            channel_layer = get_channel_layer()
            async_to_sync(channel_layer.group_send)(
                room_group_name, {
                    "type": "status.notifier",
                    "data": progress
                }
            )
            message = "Status Running"
            print(message)
            progress += 10
            time.sleep(1)
            
    context = {'message': message}
    return render(request, 'home.html', context)