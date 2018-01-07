Webpack
#######

.. code-block:: bash

    $ anpylar-webpack --help
    usage: anpylar-webpack [-h] [--package PACKAGES] [--no-package-json]
                           [--dist DIST] [--no-overwrite]
                           [--extensions EXTENSIONS]
                           [--reset-anpylar | --only-anpylar] [--no-optimize]
                           [--quiet | --verbose]
                           [target]

    AnPyLar Web Application Packager

    positional arguments:
      target                Application directory to package (default: .)

    optional arguments:
      -h, --help            show this help message and exit
      --package PACKAGES    Add package from directory or vfs.js or auto_vfs.js
                            from directory to anpylar.js even if not present in
                            package.json. Can be specified multiple times
                            (default: [])
      --no-package-json     Ignore packages listed in packages.json (default:
                            False)
      --dist DIST           Specify destination directory for the webpack
                            (default: )
      --no-overwrite        Do not overwrite existing dist directory (default:
                            False)
      --extensions EXTENSIONS
                            Comma separated list of extensions to pack when
                            packaging directories (default: .py,.js,.css,.html)
      --reset-anpylar       Reset anpylar.js to default content ignoring
                            application packages. No packaging (default: False)
      --only-anpylar        Update only anpylar.js with packages code. No
                            packaging (default: False)
      --no-optimize         Do not optimize the size of the anpylar.js by
                            packaging only the needed stdlib modules (default:
                            False)
      --quiet, -q           Remove output (errors will be reported) (default:
                            False)
      --verbose, -v         Increase verbosity level (default: False)
