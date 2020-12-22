from datetime import datetime

from apscheduler.schedulers.blocking import BlockingScheduler


from wilioo import job_function

sched = BlockingScheduler()

# Schedule job_function to be called every two seconds
sched.add_job(job_function, 'interval', seconds=10)

sched.start()