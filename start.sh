uwsgi -x blog.xml
uwsgi --reload ./uwsgi.pid
nginx -s reload