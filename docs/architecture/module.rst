Module
######

For the reference see: :doc:`/reference/module`

A *Module* is the main control unit for several components, which for example
will all access a shared service defined in the module.

A *Module* can host *Submodules* which will be either specified through
``Modules`` or inside the *routes* directive with ``load_children``.

The module is responsible for instantiating the one-and-only ``router``
instance, which controls the navigation between components.

Properties of a *Module*
========================

  - Attributes and other defininitions, like *services* in the *Module* can be
    accessed by:

    - Submodules (and components of it)

    - Components (and subcomponents of it) created by the module or during
      routing

  - It can declare:

    - *bindings*: which auto-generates an attribute bound to an *Observable*

    - *services*: which will be added as attributes and instantiated to provide
      a service to components and submodules

    - *modules*: which will be instantiated as submodules. Submodules don't,
      for example, host a ``router`` instance

    - *components*: which will be bootstrapped during initialization (before
      the routing engine takes over, if routes are defined)

    - *routes*: which define the navigation hierarchy

    - *selector* (default: ``None``)

      The default behavior of a module controlling an application is that
      things are plotted in the body of the html document. Where exactly is
      decided by the rendering engine (i.e.: the browser in most cases).

      If finer control is wished, one can

        - Insert a ``<module-outlet></module-outlet>`` tag in the html document
          and the module will use the tag as the root node for components to be
          rendered to.

        - Specify a different name in the module definition with for example
          ``selector = 'my-module-tag'`` and later have this as a tag in the
          html document as in: ``<my-module-tag></my-module-tag>``. Everything
          will be rendered under this tag.


An Empty Module
===============

With no definitions it would simply look like this after having inherited from
``Module`` and if we looked into the contents of each of the directives.

.. code-block:: python

   from anpylar import Module

   class MyModule(Module):
       bindings = {}
       services = {}
       modules = []
       components = []  # can be a single item or an iterable
       routes = []

A more standard look for a real application could look like this.

.. code-block:: python

   from anpylar import Module

   from .app_component import AppComponet
   from .one_component import OneComponent
   from .two_component import TwoComponent
   from .the_service import TheService

   class MyModule(Module):
       bindings = {}
       services = {'the_service': TheService}
       modules = []
       components = AppComponent  # can be a single item or an iterable
       routes = [
           {'path': 'one', 'component': OneComponent,},
           {'path': 'two', 'component': TwoComponent,},
       ]

This defines a *Module* that:

  - Creates a service from ``TheService`` and makes it reachable as an
    attribute under the name ``the_service``

  - Bootstraps the component ``AppComponent`` before the routing engine takes
    over

  - Instantiates the routing engine with two routes: ``http://baseurl/one`` and
    ``http://baseurl/two`` for which components ``OneComponent`` and
    ``TwoComponent`` will be respectively instantiated
