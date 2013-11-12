killall -9 'uwsgi -x blog.xml'
find . -name "*.pyc" | xargs rm -rf
uwsgi -x blog.xml
nginx -s reload
