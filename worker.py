import os
from rq import Worker, Queue
import redis
from tasks import process_analysis_job

redis_url = os.getenv('REDIS_URL', 'redis://localhost:6379/0')
conn = redis.from_url(redis_url)

if __name__ == '__main__':
    worker = Worker(['default'], connection=conn)
    worker.work() 