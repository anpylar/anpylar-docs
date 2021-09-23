Apps/Modules/Components
#######################

There are three commands which can aid in creating the basic skeleton of

  - Applications: ``anpylar-application``

  - Modules: ``anpylar-modules``

  - Components: ``anpylar-component``

For the full reference see: :doc:`/reference/cli/application`,
:doc:`/reference/cli/module`, :doc:`/reference/cli/component`

Application
***********

To create an application simply execute::

  anpylar-application myapp

This will create a directory named ``myapp`` with the following contents
inside::

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

.. note:: If ``myapp`` does already exist, ``anpylar-application`` will not do
          anything


Components
**********

Adding a component to the generated app is easy. Change into ``app`` directory
inside ``myapp`` and execute::

  anpylar-component Pyroes

and the resulting layout::

       ├── app
       │   ├── pyroes
       │   │   ├── __init__.py
       │   │   ├── pyroes_component.css
       │   │   ├── pyroes_component.html
       │   │   └── pyroes_component.py
       │   ├── __init__.py
       │   ├── app_component.css
       │   ├── app_component.html
       │   └── app_module.py
       ├── anpylar.js
       ├── index.html
       ├── package.json
       └── styles.css

Notice the naming conventions:

  - ``Pyroes`` was the argument for the command

  - The directory for the component has been created with the lowercase version
    ``pyroes``

  - And the files containing the component parts (``.py``, ``.html`` and
    ``.css``) use the format

    *lowercase_component.ext*

Were you to open ``pyroes_component.py`` the name of the genrated class component
would be::

  class PyroesComponent

I.e.: the provided argument + ``Component``


Modules
*******

``anpylar-module`` main use case is the generation of sub-modules. From inside
the ``app`` directory execute::

  anpylar-module --submodule mysubmodule

And the final layout::

       ├── app
       │   ├── pyroes
       │   │   ├── __init__.py
       │   │   ├── pyroes_component.css
       │   │   ├── pyroes_component.html
       │   │   └── pyroes_component.py
       │   ├── __init__.py
       │   ├── app_component.css
       │   ├── app_component.html
       │   └── app_module.py
       ├── mysubmodule_module
       │   ├── __init__.py
       │   └── mysubmodule_module.py
       ├── anpylar.js
       ├── index.html
       ├── package.json
       └── styles.css

This allows the development of a completely isolated module by adding
components to it which can later be loaded as a sub-module of the main module.
