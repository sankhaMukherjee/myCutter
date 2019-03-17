from logs import logDecorator as lD
import json, psycopg2

from lib.celery.App import app

config = json.load(open('../config/config.json'))
logBase = config['logging']['logBase'] + 'lib.celeryWorkerExample.worker_1'

@app.task
@lD.log(logBase + '.add')
def add(logger, a, b):
    '''add two supplied items
    
    This example takes two arguments and adds them together. This
    is much like the function available with ``lib.testLib.simpleLib.py``
    and will be used only for the purpose of having a very simple function
    that can be run via a Celery worker. This function will return the 
    result of the sum, or ``None`` in the case that there was an error.
    Handling errors within distributed computing tasks is generally 
    complicated and needs a significant amount of thought to be put in
    while programming. 
    
    Parameters
    ----------
    logger : {[type]}
        [description]
    a : {[type]}
        [description]
    b : {[type]}
        [description]
    
    Returns
    -------
    [type]
        [description]
    '''

    try:
        result = a+b
        return result
    except Exception as e:
        logger.error('Unable to log the task: {e}')
        return None

    return 
