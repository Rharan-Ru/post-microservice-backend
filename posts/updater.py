from apscheduler.schedulers.background import BackgroundScheduler

from .cron import sync_comments


# Method to let a background task, in this case sync the dabase comments with post database
def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(sync_comments, 'interval', minutes=1)
    scheduler.start()
