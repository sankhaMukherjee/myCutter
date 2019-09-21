'''This is an example of a versioned lib

This structure can effectively be used for generating multiple versions of
a library. All versions of a library are saved within the ``versions`` folder
within different subfolders. In this case, a particular version may be specified
using the major and minor version numbers. An example structure is shown below:

.. code-block:: bash

    lib
    |--lib1
    |  |-- getLib.py 
    |  +--versions
    |     +-ver_1_000
    |     | |--lib1.py
    |     | |--lib2.py
    |     | +--lib3.py
    |     +-ver_1_001
    |       |--lib1.py
    |       |--lib2.py
    |       +--lib3.py




'''