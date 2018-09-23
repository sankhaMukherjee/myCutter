import json, argparse

from importlib      import util
from logs           import logDecorator  as lD
from lib.testLib    import simpleLib     as sL
from lib.argParsers import addAllParsers as aP

config   = json.load(open('../config/config.json'))
logBase  = config['logging']['logBase']
logLevel = config['logging']['level']
logSpecs = config['logging']['specs']

@lD.log(logBase + '.importModules')
def importModules(logger, resultsDict):
    '''import and execute required modules
    
    This function is used for importing all the 
    modules as defined in the ../config/modules.json
    file and executing the main function within it
    if present. In error, it fails gracefully ...
    
    Parameters
    ----------
    logger : {logging.Logger}
        logger module for logging information
    '''
    modules = json.load(open('../config/modules.json'))

    for m in modules:

        try:
            if not m['execute']:
                logger.info('Module {} is being skipped'.format(m['moduleName']))
                continue
        except Exception as e:
            logger.error('Unable to check whether ')

        try:
            name, path = m['moduleName'], m['path']
            logger.info('Module {} is being executed'.format( name ))

            module_spec = util.spec_from_file_location(
                name, path)
            module = util.module_from_spec(module_spec)
            module_spec.loader.exec_module(module)
            module.main(resultsDict)
        except Exception as e:
            print('Unable to load module: {}->{}\n{}'.format(name, path, str(e)))

    return

def main(logger, resultsDict):
    '''main program
    
    This is the place where the entire program is going
    to be generated.
    '''

    # First import all the modules, and run 
    # them
    # ------------------------------------
    importModules(resultsDict)

    # Lets just create a simple testing 
    # for other functions to follow
    # -----------------------------------

    sampleValues = [
        (1, 2),
        (1.2, 5),
        (3, 'a'),
        ('First', 'Second'),
        (55,)
    ]

    for s in sampleValues:
        try:
            sL.simpleTestFunction(*s)
        except Exception as e:
            logger.error('Unable to perform addition with values [{}]\n:{}'.format(
                s, str(e)))

    return

if __name__ == '__main__':

    # Let us add an argument parser here
    parser = argparse.ArgumentParser(description='{{cookiecutter.project}} command line arguments')
    parser = aP.parsersAdd(parser)
    results = parser.parse_args()
    resultsDict = aP.decodeParsers(results)

    # ---------------------------------------------------
    # We need to explicitely define the logging here
    # rather than as a decorator, bacause we have
    # fundamentally changed the way in which logging 
    # is done here
    # ---------------------------------------------------
    logSpecs = aP.updateArgs(logSpecs, resultsDict['config']['logging']['specs'])
    logInit  = lD.logInit(logBase, logLevel, logSpecs)
    logLevel = resultsDict['config']['logging']['level']
    main     = logInit(main, resultsDict)

    main()