find . -name "*.pyc" | xargs rm -rf
uwsgi --reload ./uwsgi.pid
nginx -s reload