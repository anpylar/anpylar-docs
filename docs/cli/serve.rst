Serving apps
############

For the full reference see: :doc:`/reference/cli/serve`

Included with *AnPyLar* is an application server to aid in development. It can:

  - Serve your application.

  - Open a browser/tab window for you.

  - Serve a JSON based API for your application.

Serving your application
************************

Given a regular project layout::

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

You can serve your application with::

  anpylar-serve myapp

which will output::

  Sun Dec  3 08:51:47 2027 Server Starts - http://127.0.0.1:2222

You can then use the given url to go to the browser::

  http://127.0.0.1:2222

Opening a browser tag/window
****************************

Pleae bear in mind that with modern multi-tabbed/multi-windowed browsers and
with virtual desktops, the actual tab/window may not open where you expect it.

But in any case::

  anpylar-serve --browser myapp


Serving an API
**************

You need a data structure which resembles the following::

      Pyroes = [
          {'pyd': 11, 'name': 'Pyro Nakamura'},
          {'pyd': 12, 'name': 'Mopynder Shuresh'},
          {'pyd': 13, 'name': 'Pyter Pytrelli'},
          {'pyd': 14, 'name': 'Angela Pytrelli'},
          {'pyd': 15, 'name': 'Claire Pynnet'},
          {'pyd': 16, 'name': 'Noah Pynnet'},
          {'pyd': 17, 'name': 'Pysaac Mendez'},
          {'pyd': 18, 'name': 'Pyki Sanders'},
          {'pyd': 19, 'name': 'The Pytian'},
          {'pyd': 20, 'name': 'Pylar'},
      ]

That is:

  - An array (*list*, *tuple*) of *dict* entries.

  - For the sake of it, they should all have the same structure. We are
    simulating a database.

If you store this under ``mock_pyroes.py`` in your application directory
(because you may also use it internally)::

  myapp
  ├── app
  │   ├── __init__.py
  │   ├── app_component.css
  │   ├── app_component.html
  │   ├── app_component.py
  │   ├── app_module.py
  │   └── mock_pyroes.py
  ├── anpylar.js
  ├── index.html
  ├── package.json
  └── styles.css

You may then serve the API as in::

  anpylar-serve myapp \
    --api-url /api/pyroes/ \
    --api-mod myapp/app/mock_pyroes.py \
    --api-data Pyroes \
    --api-index pyd

See for example a real application with the *Tour of Pyroes*:
:doc:`/tutorial/top6-plus/index`
