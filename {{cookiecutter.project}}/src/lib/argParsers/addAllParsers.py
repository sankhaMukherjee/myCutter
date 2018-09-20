from lib.argParsers import config as cf

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

    parser = cf.addConfigParsers(parser)

    return parser

def updateArgs(logger, defaultDict, claDict):
    '''[summary]
    
    [description]
    
    Parameters
    ----------
    logger : {[type]}
        [description]
    defaultDict : {[type]}
        [description]
    claDict : {[type]}
        [description]
    
    Returns
    -------
    [type]
        [description]
    '''

    return defaultDict

@lD.log(logBase + '.decodeParsers')
def decodeParsers(logger, args):
    '''convert the parser namespace into a dict
    
    This takes the parsed arguments and converts the values
    into a dictionary that can be used ...
    
    Parameters
    ----------
    logger : {logging.Logger}
        The logger used for logging error information
    parser : {[type]}
        [description]
    '''

    allConfigs = {}

    configCLA = {}
    configCLA['logging'] = cf.decodeParser(args)

    allConfigs['config'] = configCLA

    return allConfigs

