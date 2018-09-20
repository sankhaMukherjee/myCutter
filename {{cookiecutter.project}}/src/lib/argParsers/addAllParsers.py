from lib.argParsers import config

from logs import logDecorator as lD
import json

config = json.load(open('../config/config.json'))
logBase = config['logging']['logBase'] + '.lib.argParsers.addAllParsers'

@lD.log(logBase + '.parsersAdd')
def parsersAdd(logger, parser):
    '''add all available CLI arguments to the parser
    
    This function is going to add all available parser
    information into the provided parser argument.
    
    Parameters
    ----------
    logger : {logging.Logger}
        The logger used for logging error information
    parser : {argparse.ArgumentParser instance}
        An instance of ``argparse.ArgumentParser()`` that will be
        used for parsing the command line arguments.
    
    Returns
    -------
    ``argparse.ArgumentParser()`` instance
        This is a ``argparse.ArgumentParser()`` instance that captures
        all the optional argument options that have been passed to 
        the instance
    '''

    parser = config.addaddConfigParsers(parser)

    return parser
