Syntaxcheck
###########

.. code-block:: bash

    $ anpylar-syntaxcheck --help
    usage: anpylar-syntaxcheck [-h] [--no-stop] [--quiet | --verbose]
                               files_dirs [files_dirs ...]

    AnPyLar Syntax Checker

    positional arguments:
      files_dirs     Files or Directories to check

    optional arguments:
      -h, --help     show this help message and exit
    --no-stop      Process all targets regardless of errors (default: False)
      --quiet, -q    Remove output (errors will be reported) (default: False)
      --verbose, -v  Increase verbosity level (default: False)
