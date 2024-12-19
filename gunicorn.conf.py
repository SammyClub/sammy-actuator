import multiprocessing
from actuator.utils.logger import setup_logger

max_requests = 1000
max_requests_jitter = 50

bind = "0.0.0.0:8000"

worker_class = "uvicorn.workers.UvicornWorker"
workers = multiprocessing.cpu_count()

# Log Config
accesslog = "-"
errorlog = "-"
loglevel = "info"


def post_fork(server, worker):
    # hook is called after a worker has been forked
    logger = setup_logger(debug_console=True)
    logger.info("Worker process started")
