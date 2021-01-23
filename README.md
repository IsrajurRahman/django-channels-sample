# django-channels-sample
Send asynchronous socket status using django-channels

 Clone and install requirements from requirements.txt file
 > pip install -r requirements.txt

Install redis-server
> sudo apt update
> sudo apt install redis-server

Enable redis-server and check staus
> sudo systemctl enable redis
> sudo systemctl status redis

Run project:
> python manage.py runserver

Install chrome extension **Simple WebSocket Client** and insert URL **ws://127.0.0.1:8000/ws/status/**
and click open it will connect with socket and wait for response.

Go to http://127.0.0.1:8000 and insert an intiger number and submit, now go to Simple WebSocket Client
tab and see the status/responses.

