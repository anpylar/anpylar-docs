Module
######

.. code-block:: bash

    $ anpylar-module --help
    usage: anpylar-module [-h] [--submodule] [--preamble] [--modpath MODPATH]
                          [--no-bindings] [--no-services] [--no-routes]
                          [--no-components] [--bootstrap BOOTSTRAP] [--no-init]
                          [--license LICENSE] [--import] [--no-package-json]
                          name [outdir]

    AnPyLar Component Generator

    positional arguments:
      name                  Name of the module. The string: "Module" will be
                            appended to the name. For example: Pyro -> PyroModule
      outdir                Name for the output directory. If not provided the
                            name will be generated automatically, by lowercasing
                            the name and inserting "_" between lowercase-uppercase
                            letters. For example: PyroDetail -> pyro_detail. If
                            the directory exists (or is a file), nothing will be
                            generated (default: None)

    optional arguments:
      -h, --help            show this help message and exit
      --submodule           Create a subdirectory for the module (default: False)
      --preamble            Add python interpreter line and coding info (default:
                            False)
      --modpath MODPATH     Specify a name for the module code file If not
                            provided, the default, the name is is calculated
                            automatically as in: PyroDetail -> pyro_detail.py
                            (default: None)
      --no-bindings         Do not add the bindings directive (default: False)
      --no-services         Do not add the services directive (default: False)
      --no-routes           Do not add the routes directive (default: False)
      --no-components       Do not add the components directive. The bootstrap
                            option overrides this (default: False)
      --bootstrap BOOTSTRAP
                            List of comma separated names of components to
                            bootstrap. Import statements will be added with the
                            following naming convention: CompName -> from
                            .comp_name import Compname (default: None)
      --no-init             Do not add an init method (default: False)
      --license LICENSE     Name of file containing license text to add (default:
                            None)
      --import              Add __init__.py an import even if no submodule
                            (default: False)
      --no-package-json     Do not update package.json (default: False)
