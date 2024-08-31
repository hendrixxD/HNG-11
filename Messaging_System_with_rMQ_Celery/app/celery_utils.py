from celery import Celery

def make_celery(app):
    celery = Celery(
        app.import_name,
        broker=app.config['RABBITMQ_URL'],
        backend=app.config['CELERY_RESULT_BACKEND']
    )
    celery.conf.update(app.config)
    return celery

