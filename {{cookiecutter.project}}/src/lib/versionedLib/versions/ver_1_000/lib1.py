from logs       import logDecorator as lD
import jsonref

config = jsonref.load(open('../config/config.json'))
logBase = config['logging']['logBase'] + '.lib.versionedLib.versionedLib.ver_1_000'

@lD.log( logBase + '.someVersionedLib' )
def someVersionedLib(logger):
    '''[summary]
    
    Parameters
    ----------
    logger : [type]
        [description]
    '''

    print('We are within a function of a  versioned library: version 1.000')

    return
