screen -dmS InsHome bash -c 'cd /home/leeon/leeon/HomeServer/HomeServer; gunicorn --bind 0.0.0.0:8000 HomeServer.wsgi:application'
