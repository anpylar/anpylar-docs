Serve
#####

.. code-block:: bash

    $ anpylar-serve --help
    usage: anpylar-serve [-h] [--sname SNAME] [--port PORT] [--index INDEX]
                         [--simple] [--browser] [--auto-serve AUTO_SERVE]
                         [--dev-on] [--dev-brython DEV_BRYTHON]
                         [--dev-stdlib DEV_STDLIB]
                         [--dev-anpylar-js DEV_ANPYLAR_JS]
                         [--dev-anpylar-vfs DEV_ANPYLAR_VFS]
                         [--dev-anpylar-dir DEV_ANPYLAR_DIR]
                         [--dev-pkg-vfs DEV_PKG_VFS] [--dev-pkg-auto DEV_PKG_AUTO]
                         [--dev-pkg-dir DEV_PKG_DIR] [--dev-optimize]
                         [--api-url API_URL] [--api-mod API_MOD]
                         [--api-data API_DATA] [--api-index API_INDEX]
                         [--quiet | --verbose]
                         [application]

    AnPyLar Simple Server

    positional arguments:
      application           Application directory to serve (default: .)

    optional arguments:
      -h, --help            show this help message and exit
      --quiet, -q           Remove output (errors will be reported) (default:
                            False)
      --verbose, -v         Increase verbosity level (default: False)

    Server Options:
      --sname SNAME         Server Name (default: 127.0.0.1)
      --port PORT           Port to listen to (default: 2222)
      --index INDEX         Index file to look for (default: index.html)
      --simple              Use built-in SimpleHTTPRequestHandler (default: False)

    Miscelenaous options:
      --browser             Try to open a browser to the served app (default:
                            False)

    Development options:
      If any of the options in this group is set, the server will construct an
      on-the-fly anpylar.js bundle with each reload either with the default
      files in the package or with the provided files/directories

      --auto-serve AUTO_SERVE
                            Serve the path/file given as argument, automatically
                            providing a wrapping index.html file and anpylar.js.
                            This activates development mode (default: None)
      --dev-on              Activate dev serving unconditionally (default: False)
      --dev-brython DEV_BRYTHON
                            Serve dev brython (default: None)
      --dev-stdlib DEV_STDLIB
                            Serve dev brython stdlib (default: None)
      --dev-anpylar-js DEV_ANPYLAR_JS
                            Serve dev anpylar_js.js (default: None)
      --dev-anpylar-vfs DEV_ANPYLAR_VFS
                            Serve dev from anpylar.vfs.js (default: None)
      --dev-anpylar-dir DEV_ANPYLAR_DIR
                            Serve dev anpylar from directory (default: None)
      --dev-pkg-vfs DEV_PKG_VFS
                            Add a vfs.js package to the dev bundle (default: [])
      --dev-pkg-auto DEV_PKG_AUTO
                            Add a auto_vfs.js package to the dev bundle (default:
                            [])
      --dev-pkg-dir DEV_PKG_DIR
                            Add a directory package to the dev bundle (default:
                            [])
      --dev-optimize        Optimized the generated bundle (default: False)

    API options:
      --api-url API_URL     URL path when serving an API request (default: )
      --api-mod API_MOD     Which python source file contains the data (default: )
      --api-data API_DATA   Name of the variable holding teh data (default: )
      --api-index API_INDEX
                            Name of the field which will serve as an index
                            (default: )
