# myCutter

A cookiecutter template for my projects

## Getting Started

Install cookiecutter

```bash
pip3 install -U cookiecutter
```

Generate a python package:

```bash
cookiecutter https://github.com/sankhaMukherjee/myCutter
```

## Prerequisites

You will need to have a valid Python installation on your system. This has been tested with 
Python 3.6. It does not assume a particulay version of python, however, it makes no assertions
of proper working, either on this version of Python, or on another. Note that many of the supplied
libraries use f-strings that is only available in Python version 3.6 onward.

## Built For

 - Python 3.7

## Contributing

Please send in a pull request.

## Authors

Sankha S. Mukherjee - Initial work (October, 2017)

## License

This project is licensed under the MIT License - see the [LICENSE.txt](LICENSE.txt) file for details.

## Acknowledgments

 - Python and the great cookiecutter templates
 - Some inspiration from the already available DataScience template

## Updates

 - 2021-03-20: 
    - New module `src\modules\bayTune` that serves as a model for Bayesian optimization.
        - New file: `src\modules\bayTune\baytune.py` -> base file for starting optimizations
        - New file: `src\modules\bayTune\utils\utils.py` -> file where the actual code is present
        - New file: `config\modules\bayTune.json` -> Example configuration settings for Bayesian optimization
    - Update file: `config\config.json` -> inclide the `bayTune` module
    - Update file: `\bin\vEnv.sh` -> changed `sklearn` to `scikit-learn`, added the `baytune` library by default
    - Update file: `cookiecutter.json` -> Updated default year information
    - Update file: `Readme.md` -> change the location of the `bin\vEnv.sh` file
 - 2019-06-06: Updated the `src\Makefile` so that the documentation included the `__init__` documentation for the classes
 - 2019-04-06: Updated the `pgIO.commitData` functions to return `None` on failure
 - 2019-04-06: `argparse` updated. Now modules can be specified with `-m` or `--modules`