Syntaxcheck
###########

For the full reference see: :doc:`/reference/cli/syntaxcheck`

Developing with Python in the web console can be a challenge. Sometimes a
single change in a file will generate errors which have to be looked into with
great care.

There is nothing but standard programmer's work to alleviate the
situation. But something was noticed during the development of *AnPyLar* and
hence the tool ``anpylar-syntaxcheck``.

  - Sometimes small syntax errors produce messages which are difficult

Being able to catch the syntax error before you even test it, is therefore
something to consider.

Let's run it in our standard project structure

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

Change into ``myapp`` and run the command::

  anpylar-syntaxcheck .

Because this is a standard clean project to start with, nothing happens. Let's
introduce an error in ``app_component.py``

.. code-block:: python

    class AppComponent(Component):

        title = 'Tour of Pyroes'

        bindings = {
        }

        def render(self, node):
            print('hello' world)
            pass

And let's re-run the command::

  anpylar-syntaxcheck .

which issues the following output

.. code-block:: bash

    File ".\app\app_component.py", line 15
      print('hello' world)
                        ^
    SyntaxError: invalid syntax

And this allows to steadily correct the error and proceed with further
development.

``anpylar-syntaxcheck`` is not magic, it uses the built-in capabilities of the
Python standard library (``ast``) to find the errors. It's a small tool, but it
can prove useful.
