from datetime import datetime as dt
from time import time
import json, logging
from functools import wraps

class log(object):
    '''decorator for logging values
    
    This decorator can be used for injecting a
    logging function into a particular function. 
    This takes a function and injects a logger 
    as the first argument of the decorator. For 
    the generated logger, it is also going to 
    insert the time at which the paticular function
    was called, and then again when the function was
    finished. These serve as convinient functions for
    inserting values into the decorator. 
    '''

    def __init__(self, base):
        '''initialize the decorator
        
        Parameters
        ----------
        base : {str}
            The string used for prepending the value of the decorator
            with the right path for this function. 
        '''
        self.base   = base
        return

    def __call__(self, f):

        from time import time

        # Function to return
        @wraps(f)
        def wrappedF(*args, **kwargs):
            logger = logging.getLogger(self.base)
            logger.info('Starting the function [{}] ...'.format(f.__name__))
            t0     = time()
            result = f(logger, *args, **kwargs)
            logger.info('Finished the function [{}] in {:.6e} seconds'.format( 
                f.__name__, time() - t0 ))

            return result

        return wrappedF

class logInit(object):
    '''initialize the decorator for logging
    
    This generates a decorator using a fresh file with the right
    date and time within the function name. This way it will be
    east to find the last log file generated using a simple script
    in the case that a person wants to generate instantaneous 
    statistics for the last run. 
    '''

    def __init__(self, base, folder='logs'):
        '''Initialize the logger object for the program
        
        This logger object generates a new logger object, instantaniates
        a new file object with the current date and time in the filename
        and creates a associates the logger object to the current file. 
        
        Parameters
        ----------
        base : {str}
            base name of the decorator. This is typically the name of the
            module that is being generated. However, this can really be 
            anything. 
        folder : {str}, optional
            The folder where the log files are to be kept. (the default is 
            'logs', within the 'src' folder. It is advisable not to change
            this unless absolutely necessary.)
        '''
        self.base   = base
        self.folder = folder
        return

    def __call__(self, f):


        # Function to return
        @wraps(f)
        def wrappedF(*args, **kwargs):
            logger    = logging.getLogger(self.base)
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            fH        = logging.FileHandler(               \
                self.folder  +  '/'                      + \
                dt.now().strftime('%Y-%m-%d_%H-%M-%S')   + \
                '.log')
            fH.setFormatter(formatter)
            logger.addHandler(fH)
            logger.setLevel(logging.INFO)

            logger.info('Starting the main program ...')
            t0     = time()
            result = f(logger, *args, **kwargs)
            logger.info('Finished the main program in {:.6e} seconds'.format( time() - t0 ))

            return result

        return wrappedF
        