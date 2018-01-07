Pip
###

.. code-block:: bash

    $ anpylar-pip --help
    usage: anpylar-pip [-h] [--target TARGET] [--make-target] [--no-replace]
                       [--no-package-json] [--pkgdir PKGDIR]
                       [--single-pkgdir SINGLE_PKGDIR] [--force-pkgdir]
                       [--quiet | --verbose]
                       command packages [packages ...]

    AnPyLar pip Installer

    positional arguments:
      command               only *install* supported
      packages              pip packages to install

    optional arguments:
      -h, --help            show this help message and exit
      --target TARGET       Target directory, defaults to current dir (default: .)
      --make-target         Create target directory if does not exist (default:
                            False)
      --no-replace          Do not replace existing packages with new install
                            (default: False)
      --quiet, -q           Remove output (errors will be reported) (default:
                            False)
      --verbose, -v         Increase verbosity level (default: False)

    package.json:
      --no-package-json     If the installation directory contains a package.json
                            file the installed packages will be added to the
                            *packages* entry to be later taken into consideration
                            for packing the complete application. Using this
                            option disables the behavior (default: False)
      --pkgdir PKGDIR       Install packages under pkgdir in the application
                            directory. This overrides the entry pkgdir in
                            package.json (default: )
      --single-pkgdir SINGLE_PKGDIR
                            Add (if possible) a single directory entry to packages
                            rather than each packet individually (default: )
      --force-pkgdir        If a pkgdir is supplied and package.json is being
                            processed, update the entry for pkgdir even if a value
                            already exists (default: False)
