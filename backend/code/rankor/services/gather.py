from rankor.services.queues import app


@app.task
def gather(event, request_id, payload=None):
    pass
