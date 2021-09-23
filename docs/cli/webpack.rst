Webpack
#######

When the application is ready for deployment, ``anpylar-webpack`` comes to the
rescue in order to automate the process of packaging. It may not even be for
production, but just for a taste of real testing.

During development with a dir based application there is something which all
developers will notice:

  - Some initial ``404 Not Found`` answers are delivered when looking for
    ``.py`` files.
    Which is simply due to the need to look for the right file when importing.

    Once we have packaged our application, this will be gone.


A typical layout
****************

Our *Tour of Pyroes* has already shown the layouts, so let's simply reuse
them::

      ├── app
      │   ├── dashboard
      │   │   ├── __init__.py
      │   │   ├── dashboard_component.css
      │   │   ├── dashboard_component.html
      │   │   └── dashboard_component.py
      │   ├── pyro_detail
      │   │   ├── __init__.py
      │   │   ├── pyro_detail_component.css
      │   │   ├── pyro_detail_component.html
      │   │   └── pyro_detail_component.py
      │   ├── pyro_search
      │   │   ├── __init__.py
      │   │   ├── pyro_search_component.css
      │   │   ├── pyro_search_component.html
      │   │   └── pyro_search_component.py
      │   ├── pyroes
      │   │   ├── __init__.py
      │   │   ├── pyroes_component.css
      │   │   ├── pyroes_component.html
      │   │   └── pyroes_component.py
      │   ├── __init__.py
      │   ├── app_component.css
      │   ├── app_component.html
      │   ├── app_component.py
      │   ├── app_module.py
      │   ├── app_routing.py
      │   ├── mock_pyroes.py
      │   ├── pyro.py
      │   ├── pyro_search_service.py
      │   └── pyro_service.py
      ├── anpylar.js
      ├── index.html
      ├── package.json
      └── styles.css

And we'd ideally reduce this to the minimum possible amount of files. Let's try
webpacking. Enter the directory and simply execute::

  anpylar-webpack

And the result will be this (omitting everything we have already seen above)::

      ├── __webpack__
      │   ├── anpylar.js
      │   ├── index.html
      │   ├── package.json
      └── └── styles.css

This is what happened:

  - ``anpylar-webpack`` has taken our complete application and packaged it
    inside ``anpylar.js``.

  - And it has placed all necessary files inside the newly created
    ``__webpack__`` directory.


And now when the application is served, everything will be directly served from the
contents stored in ``anpylar.js``

The webpacking process can be tuned using ``package.json``. The options:

  - ``packages`` (an array of directories to package).

    In our sample above, the entry looks like this::

      "packages": [
         "app"
      ],


  - ``debug`` (a boolean: default ``false``)

    The default ``anpylar.js`` keeps the line information activated for
    debugging purposes when finding errors.

    Set it to ``true`` to keep this behavior in the packaged application.


See also
********

``anpylar-webpack`` has several command line switches to control its
behavior. See the reference :doc:`/reference/cli/webpack` if you need more.
