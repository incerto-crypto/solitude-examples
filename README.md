# solitude-examples

A collection of examples on how to use solitude

## Solitude

Solitude is a framework for developing and testing contracts

### Installing solitude

Install the requirements on your OS:

-   Python3.5 or greater
-   node8 or greater
-   yarn

Create a python3 virtual environment and activate it. Install solitude.

```bash
python3 -mvenv myenv
source myenv/bin/activate
pip install git+ssh://git@gitlab.com/cryptostallions/solitude.git
```

### Using solitude

Move to your project directory and create a YAML or JSON configuration file for solitude. The default is `solitude.yaml`. A file filled with default configurations can be created by running `solitude init`.

This file contains a version string for each of the external tools you are going to use. Solitude can download the tools for you by running `solitude install`. By default the tools are installed in `~/.solitude-dev`.

```bash
solitude init
solitude install
```

You can use solitude in your project by either importing and using specific parts of the framework in your python scripts. This is covered in the examples.
