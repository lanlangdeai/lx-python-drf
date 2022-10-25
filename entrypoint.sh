# 是否需要执行数据库变更
if [ "$ENABLE_MIGRATE" == "true" ];then
  python3 manage.py migrate
fi

echo "start demo web service"

# 根据配置环境指定运行方式
if [ "$ENV" == "local" ];then
  exec python3 manage.py runserver 0.0.0.0:8080
else
  python3 manage.py collectstatic
  exec gunicorn demo.wsgi:application \
    --name main_django \
    --max-requests 2000 \
    --max-requests-jitter 500 \
    --bind 0.0.0.0:8080 \
    --workers 4 \
    --threads 4 \
    "$@"
fi