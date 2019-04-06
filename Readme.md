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

You will need to have a valid Python installation on your system. This has been tested with Python 3.6. It does not assume a particulay version of python, however, it makes no assertions of proper working, either on this version of Python, or on another. 

## Built For

 - Python 3.6

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

 - 2019-04-06: updated the `pgIO.commitData` functions to return `None` on failure
 - 2019-04-06: `argparse` updated. Now modules can be specified with `-m` or `--modules`