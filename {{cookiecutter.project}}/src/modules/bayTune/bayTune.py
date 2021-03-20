from logs import logDecorator as lD 
import jsonref, pprint

from modules.bayTune.utils import utils

config = jsonref.load(open('../config/config.json'))
logBase = config['logging']['logBase'] + '.modules.bayTune.bayTune'

@lD.log(logBase + '.main')
def main(logger, resultsDict):
    '''main function for bayTune
    
    This function finishes all the tasks for the
    main function. This is a way in which a 
    particular module is going to be executed. 
    
    Parameters
    ----------
    logger : {logging.Logger}
        The logger used for logging error information
    resultsDict: {dict}
        A dintionary containing information about the 
        command line arguments. These can be used for
        overwriting command line arguments as needed.
    '''

    print('='*30)
    print('Main function of bayTune')
    print('='*30)
    print('We get a copy of the result dictionary over here ...')
    pprint.pprint(resultsDict)

    utils.optimize()

    print('Getting out of bayTune')
    print('-'*30)

    return

