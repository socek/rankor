from rankor.services.queues import app


@app.task
def broadcast(event, request_id, payload=None, ignores=[]):
    from rankor.services.s1 import s1
    from rankor.services.s2 import s2

    tasks = [s1, s2]
    print('broadcasting: {}:{}'.format(event, request_id))
    for task in tasks:
        if task.__name__ in ignores:
            continue
        print('sending', task.__name__, task, event, request_id, payload)
        task.delay(event, request_id, payload)
