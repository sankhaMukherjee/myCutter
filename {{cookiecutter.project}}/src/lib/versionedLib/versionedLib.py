from logs       import logDecorator as lD
from importlib  import util
import jsonref, os

config = jsonref.load(open('../config/config.json'))
logBase = config['logging']['logBase'] + '.lib.versionedLib.versionedLib'

def getLib(version, libName):
    '''return a particular library dynamically, based upon a 
    version number.
    
    Parameters
    ----------
    version : [type]
        [description]
    libName : [type]
        [description]
    
    Returns
    -------
    [type]
        [description]
    '''

    
    name = libName + '__' + version
    path = f"lib/versionedLib/versions/ver_{version}/{libName}.py"

    assert os.path.exists(path), f'Unable to find the library: {path}'
            
    module_spec = util.spec_from_file_location(name, path)
    module = util.module_from_spec(module_spec)
    module_spec.loader.exec_module(module)

    return module

