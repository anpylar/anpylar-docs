Application
###########

.. code-block:: bash

    $ anpylar-application --help
    usage: anpylar-application [-h] [--package PACKAGE] [--no-async]
                               [--title TITLE] [--no-preamble] [--license LICENSE]
                               [--htmlista | --selectista | --pythonista]
                               [--tutorial] [--no-package-json]
                               [--app-name APP_NAME] [--app-version APP_VERSION]
                               [--app-author APP_AUTHOR] [--app-e-mail APP_E_MAIL]
                               [--app-license APP_LICENSE] [--app-url APP_URL]
                               name

    AnPyLar Application Generator

    positional arguments:
      name                  Name of the application

    optional arguments:
      -h, --help            show this help message and exit
      --package PACKAGE     Name of the application package inside our app
                            (default: app)
      --no-async            Do not load anyplar.js asynchronously (default: False)
      --title TITLE         Title for index.html (default: )
      --no-preamble         Skip python interpreter line and coding info (default:
                            False)
      --license LICENSE     Name of file containing license text to add (default:
                            None)
      --htmlista            Component will only render (Default option) (default:
                            False)
      --selectista          Component will select nodes for rendering (default:
                            False)
      --pythonista          Component will only render. No html file generation
                            (default: False)
      --tutorial            Add title and styles from Tour of Pyroes (default:
                            False)

    package.json:
      --no-package-json     Skip generation of package.json (default: False)
      --app-name APP_NAME   Application name for package json (default: )
      --app-version APP_VERSION
                            Application version name for package json (default: )
      --app-author APP_AUTHOR
                            Author name for package json (default: )
      --app-e-mail APP_E_MAIL
                            E-Mail for package json (default: )
      --app-license APP_LICENSE
                            License for package.json (default: )
      --app-url APP_URL     Application URL for package.json (default: )
