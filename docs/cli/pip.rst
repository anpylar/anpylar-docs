Package Installation - pip
##########################

For the full reference see: :doc:`/reference/cli/pip`

Python has a package repository: the Python Package Index or *pypi* which you
can visit at https://pypi.python.org/pypi

Even if we are developing for the web and this is new territory for Python, it
would be nice if at least part of the vast arsenal of available packages

That's the role of ``anpylar-pip``, which:

  - Instructs ``pip`` to install packages in a private directory

  - Scans the packages for Python purity

  - Installs the packages in the application

Pure Python
***********

Only packages which are pure Python can be installed. Those relying on ``C``
extensions are not supported.

Furthermore: **NOT** all pure Python packages can be used. See
:doc:`/technology` for the description of the underlying technology and the
constraints.

Installing a package
********************

Let's use a known pure Python package which provides a framework for working with
parameters in classes in a declarative manner: ``metaparams``

Let's recall a standard project layout:

.. code-block:: bash

    myapp
    ├── app
    │   ├── __init__.py
    │   ├── app_component.css
    │   ├── app_component.html
    │   ├── app_component.py
    │   └── app_module.py
    ├── anpylar.js
    ├── index.html
    ├── package.json
    └── styles.css

And the content of our ``package.json`` before the installation

.. code-block:: json

    {
        "packages": [
            "app"
        ],
        "app_name": "",
        "version": "",
        "author": "",
        "author_email": "",
        "license": "",
        "url": ""
    }


Change into the ``myapp`` directory and run

.. code-block:: bash

    $ anpylar-pip install metaparams
    Target for pip installation is: .
    Processing package.json
    Collecting metaparams
    Collecting metaframe (from metaparams)
    Installing collected packages: metaframe, metaparams
    Successfully installed metaframe-1.0.1 metaparams-1.0.4
    Moving pip packages to final destination

And the following happens to the file structure:

.. code-block:: bash

    myapp
    ├── app
    │   ├── __init__.py
    │   ├── app_component.css
    │   ├── app_component.html
    │   ├── app_component.py
    │   └── app_module.py
    ├── metaframe
    │   ├── __init__.py
    │   └── metaframe.py
    ├── metaparams
    │   ├── __init__.py
    │   ├── metaparams.py
    │   └── version.py
    ├── anpylar.js
    ├── index.html
    ├── package.json
    └── styles.css

We have two new directories containing the packages ``metaparams`` (as
expected) and a dependency which was pulled: ``metaframe``

And the content of our ``package.json`` before the installation

.. code-block:: json

    {
        "packages": [
            "app",
            "metaframe",
            "metaparams"
        ],
        "app_name": "",
        "version": "",
        "author": "",
        "author_email": "",
        "license": "",
        "url": ""
    }

Our new *pip* packages have been added to ``package.json`` and they will
therefore be collected when generating a webpack (see: :doc:`/cli/webpack`)

The newly added packages can now be used during testing and deployed for
production scenarios.
