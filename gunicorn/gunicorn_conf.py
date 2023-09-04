from multiprocessing import cpu_count

# Socket Path

bind = 'unix:/var/www/fastapi_project/gunicorn.sock'


# Worker Options

workers = cpu_count() + 3

worker_class = 'uvicorn.workers.UvicornWorker'


# Logging Options

loglevel = 'debug'

accesslog = '/var/www/fastapi_project/access_log'

errorlog =  '/var/www/fastapi_project/error_log'
