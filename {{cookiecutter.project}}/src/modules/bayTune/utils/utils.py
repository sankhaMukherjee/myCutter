from logs import logDecorator as lD 
import jsonref, pprint
import numpy as np
from tqdm import tqdm

import warnings

from sklearn.datasets        import load_wine
from sklearn.model_selection import train_test_split
from sklearn.linear_model    import SGDClassifier

from btb.tuning import Tunable
from btb.tuning.tuners import GPTuner

import matplotlib.pyplot as plt

config = jsonref.load(open('../config/config.json'))
logBase = config['logging']['logBase'] + '.modules.bayTune.utils.utils'

configM = jsonref.load(open('../config/modules/bayTune.json'))['params']

@lD.log( logBase + '.createDataSet' )
def createDataSet(logger):
    '''get the wind dataset

    This functionis going to load the wine dataset and generate
    outputs for training testing. If there is an error, a None
    is returned

    Parameters
    ----------
    logger : {logging.Logger}
        The logger used for logging error information

    Returns
    -------
    tuple
        The data present within the tuple will be a series of 
        numpy arrays as described below:
        - X_train : training dataset (N_train, M)
        - X_test  : testing dataset (N_test, M)
        - y_train : output for the train data (N_train,)
        - y_test  : output for the test data (N_test,)
    '''

    try:
        dataset = load_wine()
        X_train, X_test, y_train, y_test = train_test_split(
            dataset.data, dataset.target, test_size=0.3, random_state=0)

        print(X_train.shape, y_train.shape)

        return X_train, X_test, y_train, y_test
    except Exception as e:
        logger.error(f'Unable to load the wine dataset: {e}')

    return 

@lD.log( logBase + '.optimize' )
def optimize(logger):
    '''Simple optimization example

    A simple example of how to optimize hyperparameters of a model. The optimizer
    will propose different parameters depending upon previous runs. Based upon
    that, you will be able to organize your training process in a meaningful 
    manner. 

    Note that this example is taken (with slight modification) from one
    of the examples provided by bayTune here:
    https://github.com/MLBazaar/BTB/blob/master/tutorials/01_Tuning.ipynb

    Parameters
    ----------
    logger : {logging.Logger}
        The logger used for logging error information


    Returns
    -------
    dict
        This returns the best parameters for which the testing score
        was obtained. Not that this is not cross-validated, and thus
        there is a lot of room for improvement.
    '''


    try:
        # Turn off warnings if it gets annoying ...
        warnings.filterwarnings('ignore')

        ##########################################################
        # Generate the dataset
        ##########################################################

        dataset = createDataSet()
        if dataset is None:
            return
        X_train, X_test, y_train, y_test = dataset

        ##########################################################
        # Generate the tuneable and the tuners
        ##########################################################
        tunable = Tunable.from_dict( configM['hyperParams'] )
        tuner = GPTuner(tunable)

        ##########################################################
        # Optimize the hyperparameters
        ##########################################################

        best_score = 0
        best_iter  = 0
        allScores  = []

        for i in tqdm(range(configM['numIters']), total=configM['numIters']):

            proposal = tuner.propose()
            model = SGDClassifier(**proposal)
            model.fit(X_train, y_train)
            score = model.score(X_test, y_test)

            allScores.append(score)

            if score > best_score:
                best_params = proposal
                best_score  = score
                best_iter   = i
                
            tuner.record(proposal, score)
            
        print('Best score obtained: ', best_score)
        print('Best parameters: ', best_params)

        ##########################################################
        # Plot best parameters
        ##########################################################

        plt.plot(np.arange(configM['numIters']), allScores, '+', mfc='None', mec='black')
        plt.plot( [best_iter], [best_score], 'o', ms=10, mfc='None', mec='red' )
        plt.ylim([0, 1])
        plt.xlabel('Iterations')
        plt.ylabel('Score')
        plt.savefig( configM['outFigure'] )

        return best_params

    except Exception as e:
        logger.error(f'Unable to tune the hyperparameters: {e}')
        

    return