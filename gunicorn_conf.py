#Gunicorn Config File
#29.03.2023 


from multiprocessing import cpu_count



# Socket Path

bind = 'unix:/home/pi/CalculateApi/gunicorn.sock'



# Worker Options

workers = cpu_count() + 1

worker_class = 'uvicorn.workers.UvicornWorker'



# Logging Options

loglevel = 'debug'

accesslog = '/home/pi/CalculateApi/access_log'

errorlog =  '/home/pi/CalculateApi/error_log'
