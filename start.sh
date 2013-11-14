find . -name "*.pyc" | xargs rm -rf
nginx -s reload