from logs import logDecorator as lD
from lib import simpleLib as sL
import json

config = json.load(open('../config/config.json'))

@lD.logInit(config['logging']['logBase'], config['logging']['logFolder'])
def main(logger):
    '''main program
    
    This is the place where the entire program is going
    to be generated.
    '''

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
    main()