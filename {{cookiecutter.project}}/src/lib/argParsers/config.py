from logs import logDecorator as lD
import json

config = json.load(open('../config/config.json'))
logBase = config['logging']['logBase'] + '.lib.argParsers.config'

@lD.log(logBase + '.parsersAdd')
def addConfigParsers(logger, parser):
    '''add argument parsers specific to the ``config/config.json`` file
    
    This function is kgoing to add argument parsers specific to the 
    ``config/config.json`` file. This file has several options for 
    logging data. This information will be 
    
    Parameters
    ----------
    logger : {logging.Logger}
        The logger used for logging error information
    parser : {argparse.ArgumentParser instance}
        An instance of ``argparse.ArgumentParser()`` that will be
        used for parsing the command line arguments specific to the 
        config file
    
    Returns
    -------
    [type]
        [description]
    '''
    
    parser.add_argument("--logging_level", 
        type=str, 
        choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'],
        help="change the logging level")
    parser.add_argument("--logging_specs_file_todo", 
        action="store_true",
        help="allow file logging")
    parser.add_argument("--logging_specs_file_logFolder", 
        type = str,
        help = "folder in which to log files")
    parser.add_argument("--logging_specs_stdout_todo", 
        action="store_true",
        help="allow stdout logging")
    parser.add_argument("--logging_specs_logstash_todo", 
        action="store_true",
        help="allow logstash logging")
    parser.add_argument("--logging_specs_logstash_version", 
        type = int,
        help = "version for the logstash server")
    parser.add_argument("--logging_specs_logstash_port", 
        type = int,
        help = "port for the logstash server")
    parser.add_argument("--logging_specs_logstash_host", 
        type = str,
        help = "hostname for the logstash server")

    return parser

def parseArguments(logger, args):
    '''generate a dictionary from the parsed args
    
    The parsed args may/may not be present. When they are
    present, they are pretty hard to use. For this reason,
    this function is going to convert the result into
    something meaningful.
    
    Parameters
    ----------
    logger : {logging.Logger}
        The logger used for logging error information
    args : {args Namespace}
        parsed arguments from the command line
    
    Returns
    -------
    dict
        Dictionary that converts the arguments into something
        meaningful
    '''

    return value