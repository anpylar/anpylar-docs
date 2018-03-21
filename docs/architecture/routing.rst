Routing
#######

The *routes*
************

Inside *Modules* and *Components* there is access to a pre-defined attribute::

  self.router

This gives access to the routing engine, which is controlled by *routes*
definitions given in the topmost module and *sub-routes* in sub-modules
thereof. Notice that unlike *bindings* and *services* which can be defined in
both *Modules* and *Components*: **routes cannot be defined in components**.

Let's see a real definition from the *Tour of Pyroes*
:doc:`/tutorial/top5/index` sample.

.. code-block:: python

      routes = [
          {
              'path': '',
              'redirect_to': '/dashboard',
              'path_match': 'full'
          },
          {
              'path': 'dashboard',
              'component': DashboardComponent
          },
          {
              'path': 'pyroes',
              'component': PyroesComponent
          },
          {
              'path': 'detail',
              'component': PyroDetailComponent,
              'params': {'pyd': int},  # param transformation function
          },
      ]

As you may see above, the routes is a *list* (or iterable) of *dict*
entries. Let's try to bring light to the definitions.

The most usual aspect for an entry will probably be this.

.. code-block:: python

          {
              'path': 'dashboard',
              'component': DashboardComponent
          },


The route defines a:

  - ``path``, i.e.: the matching pattern for the route.
    In this case we have ``dashboard``, so that this will be matched::

      baseurl/dashboard

    Obviously, we don't have to care about ``baseurl`` in the definition of the
    route, because our app can be located and relocated to different servers,
    paths.

  - ``component``, i.e.: which component will be instantiated when the route is
    a match.

    Actually, a component is **not** always instantiated. Ideally this will only
    happen once. All other times when navigating to/from the route, the
    component (and the associated html) will be *loaded* and *unloaded*. See
    :doc:`/architecture/component` for details about ``loading`` and
    ``unloading``.

    .. note:: Although not shown here, the code in :doc:`/tutorial/top5/index`
              contains an import statement for ``Dashboardcomponent`` to make
              it visible inside the module and avoid an error.

Route Rendering
===============

When navigating to the route and the route is a match and a component has to be
rendered on-screen, the following (basically) happens

  - Within the hierarchy of the current component (if any) a
    ``<router-outlet>`` tag is sought.

  - If none is found, the default behavior is to generate one in-place.

  - Be it the found one or the generated one, the ``<router-outlet>`` tag
    becomes the parent node for the rendering of the component.

  - The component is then given the chance to render itself underneath
    ``<router-outlet>``..

  - The component is told it is ``loading`` into the DOM by calling the method
    with the same name.

When navigating away from the route the following (basically) happens

  - The component is told it is ``unloading`` from the DOM by calling the
    method with the same name.

  - The ``<router-outlet>`` tag is emptied (the component's html is removed
    fromt he DOM).

Additionally:

  - Navigating to and away from routes can be controlled with authentication
    guards/deactivation controls.

More on that later.

Defining parameters for routes
==============================

.. code-block:: python

          {
              'path': 'detail',
              'component': PyroDetailComponent,
              'params': {'pyd': int},  # param transformation function
          },

This component adds a parameter entry::

  'params': {'pyd': int},  # param transformation function

Which includes a remark that ``{'pyd': int}`` is a transformation function. A
URL is a text string and parameters are therefore when parse also *text*. The
possibility to specify a transformation function means that components don't
have to care about the details. The details are being taken care of for them.

A sample URL with parameters (also from the tutorial sample reference above)::

      http://127.0.0.1:2222/detail;pyd=13

Before our ``PyroDetailComponent`` is given a chance to act, the *router* knows
it has to parse the parameter and transform that to an ``int``. The parameter
is later available for the component under ``self.params``. Actual code from the
sample.

.. code-block:: python

          def loading(self):
              self.pyro_service \
                  .get_pyro(self.params.get('pyd', 0)) \
                  .subscribe(self.pyro_)  # fetch async and fire self.pyro_ when done

As anyone can guess: ``self.params`` is a *dict*. Hence possibility to do::

  self.params.get('pyd', 0)

The reader may have been expecting this though::

  self.params['pyd']

But this wouldn't work if someone had wrongly pasted this URL in the browser::

      http://127.0.0.1:2222/detail

Because there would be no ``pyd`` parameter. And that's why the code tries to
play nice and issue a ``get('pyd', 0)``

**Rest Matching and Redirection**

There is another entry which looks different in the above *routes* definition

.. code-block:: python

          {
              'path': '',
              'redirect_to': '/dashboard',
              'path_match': 'full'
          },

The ``path`` definition is empty and a ``'path_match': 'full'`` is given which
translates to

  - If nothing else remains to be matched in the route, then do the defined
    action

In this case it dpes not load a component but specifies a::

              'redirect_to': '/dashboard',

to redirect to a different path. Notice that

  - The route definitions have no leading ``/`` because they are transformed
    internally to be ``baseurl/path`` (if a leading ``/`` is specified, it will
    be stripped internally to ensure proper route construction)

  - But when redirecting, we could be issuing a *relative* redirect (relative
    to the current path) or an absolute. In this case the redirect is absolute

Child Routes
============

Via the *routes* definition
---------------------------

Yes, they are also possible. Let's see the routes from the
:doc:`/tutorial/tourer/index` sample.


.. code-block:: python

    routes = [
        {
            'path': 'compose',
            'component': ComposeMessageComponent,
            'outlet': 'popup'
        },
        {
            'path': 'disaster-center',
            'load_children': [DisasterCenterModule]
        },
        {
            'path': 'admin',
            'load_children': [AdminModule]
            'can_activate', [AuthGuard],
        },

        {'path': '', 'redirect_to': '/superpyroes', 'path_match': 'full'},
        {'path': '*', 'component': PageNotFoundComponent},
    ]


The key here is the ``load_children``::

        {
            'path': 'disaster-center',
            'load_children': [DisasterCenterModule]
        },

In this case there is only 1 sub-module: ``DisasterCenterModule``. Any routes
defined in this *module* will be loaded and treated as chil routes of our
main module. And

  - They will be available under the defined ``path``::

            'path': 'disaster-center',

Benefits and goals of this:

  - Breaking the functionality into different, separated and isolated pieces to
    simplify and facilitate development

  - Having full modules which can act as a main module or as a sub-module. The
    ``DisasterCenterModule`` could be conceived as a complete application, which
    in this case is being created under the main ``AppModule``.

  - Being able to replace the ``DisasterCenterModule`` with something else very
    easily thanks to separation and isolation

Cascading Child Routes
+++++++++++++++++++++++++

The reasoning about including a fully-fledged module (``DisasterCenterModule``)
as a sub-module of another module, opens up the possibility that the sub-module
could have its own child routes defined. And yes, it is. From that sample, the
set of routes defined by ``DisasterCenterModule``

.. code-block:: python

    class DisasterCenterModule(Module):

        services = {
            'disaster_service': DisasterService,
        }

        routes = [{
            'path': '',
            'component': DisasterCenterComponent,
            'children': [
                {
                    'path': '',
                    'component': DisasterListComponent,
                    'children': [
                        {
                            'path': '',
                            'component': DisasterDetailComponent,
                            'params': {'did': int},  # transformation function
                        },
                        {
                            'path': '',
                            'component': DisasterCenterHomeComponent,
                        }
                    ]
                }
            ]
        }]

It's not only that it is defining *children*, it is already nesting them. In
this case not *loading* them from any other module but simply defining them as
``children``. In this manner, one can define a hierarchy of components. See::

            'path': '',
            'component': DisasterCenterComponent,
            'children': [

Which translates to:

  - As a route I am adding nothing to the ``path``, so the current match is
    valid.

  - As a route I am simply saying that a component named
    ``DisasterCenterComponent`` has to be loaded

  - And please be aware that I have ``children``

If we carry on::

                    'path': '',
                    'component': DisasterListComponent,
                    'children': [

There is a second iteration which is exactly like the previous. The most
important part in both definitions is, possibly, that they are **adding nothing
to the path** and therefore have no influence for the matching process.

Further descending, the final children::

                        {
                            'path': '',
                            'component': DisasterDetailComponent,
                            'params': {'did': int},  # transformation function
                        },
                        {
                            'path': '',
                            'component': DisasterCenterHomeComponent,
                        }

Both again ... have no content for ``path``. This at the end of the day means
that they add nothing for the matching when it comes down to the ``path``. The
main path will be valid for both.

But notice that::

                            'params': {'did': int},  # transformation function

There is a ``params`` definition for the first of the two chilren. This is the
tie breaker.

  - If there is param and matches ``did`` our first child and the component
    ``DiasterDetailComponent`` will be a winner

  - If there is no param or match, our 2nd child wins and the
    ``DisasterCenterHomeComponent`` will be loaded

Via the *module* directive
--------------------------

In that same sample, the following is made to load child routes

.. code-block:: python

    class AppModule(Module):
        components = AppComponent

        modules = PyroesModule, LoginModule

        ...

In this case two sub-modules are being added to the hierarchy of
``AppModule``. And every route defined in those components will be made a child
route of the main routes definition.

Of course, and because no ``path`` definition is possible:

  - The child routes from ``PyroesModule`` and ``LoginModule`` will be made
    available under the root path: ``/``.


Non matching routes
===================

From the :doc:`/tutorial/tourer/index` sample::

        {'path': '*', 'component': PageNotFoundComponent},

Use ``'*'`` or ``'**'`` to mark a route which will take over if all other
routes were not a match for the current path. In this case the action is:

  - Load the component ``PageNotFoundComponent``

It could also have been a redirect to the root path as in::

        {'path': '*', 'redirect_to': '/'},


Guards - Route Activation
*************************

A route can be **guarded** from entering/leaving it. The reasons for it:

  - A page may be *login* protected.

  - A page may be *permission* protected, i.e.: you may be logged in but your
    permissions may not be enough to access a specific section.

  - A page may allow navigation away from it after confirming that changes to a
    text field don't have to be saved.

  - A page may ask you if you really want to log-out.

Although it was not mentioned before, the definitions above from the
:doc:`/tutorial/tourer/index` already contained an entering guard. Let's recall it

.. code-block:: python

    ...
    from .auth_guard_service import AuthGuard
    ...

    routes = [
        {
            'path': 'compose',
            'component': ComposeMessageComponent,
            'outlet': 'popup'
        },
        {
            'path': 'disaster-center',
            'load_children': [DiasterCenterModule]
        },
        {
            'path': 'admin',
            'load_children': [AdminModule]
            'can_activate', [AuthGuard],
        },

        {'path': '', 'redirect_to': '/superpyroes', 'path_match': 'full'},
        {'path': '*', 'component': PageNotFoundComponent},
    ]


where the key is::

    ...
    from .auth_guard_service import AuthGuard
    ...


        {
            'path': 'admin',
            'load_children': [AdminModule]
            'can_load', [AuthGuard],
        },


Entering the ``'admin'`` path (and with it the entire ``AdminModule``) is
guarded by ``AuthGuard``. Let's have a look to see what it is doing

.. code-block:: python

    from anpylar import AuthGuard


    class AuthGuard(AuthGuard):

        def can_activate(self, route):
            return self.check_login(route.path)

        def can_activate_child(self, route):
            return self.can_activate(route)

        def check_login(self, path):
            if self.auth_service.is_logged:
                return True

            self.auth_service.redir_path = path
            self.router.route_to('/login', session_id=1234567890)
            return False

It can be easily spotted that the key method is::

        def can_activate(self, route):
            return self.check_login(route.path)

The main activation control:

  - ``def can_activate(self, route)``

    Takes a *route* parameter, which contains the details of the actual route
    to be activated and

    - Returns ``True`` if the route can be activated

    - Returns ``False`` if the route cannot be activated

In this case the work is delegated to another method of the *guard* which:

  - Will redirect to ``/login`` with a ``session_id`` if the user was not
    previously logged in.

Route De-Activation
*******************

Once a route is active, the component has taken over and that's why
deactivation is delegated to the *Component*. Using code from the advance
router

.. code-block:: python

    class DisasterDetailComponent(Component):
        ...

        def can_deactivate(self):
            if not self.edit_did or self.selected.name == self.edit_name:
                return True

            # dialog_service is in the main module
            return self.dialog_service.confirm('Discard changes?')


Skipping most of the code from ``DisasterDetailComponent`` allows us to focus on
the ``can_deactivate`` method.

It has to:

  - Return ``True`` if one can navigate away

  - Return ``False`` if one cannot navigate away

It may:

  - Return an *Observable* which will finally generate either ``True`` of
    ``False``

    This is exactly what's being made in this case with::

            return self.dialog_service.confirm('Discard changes?')

    A dialog is presented to the user and to avoid blocking things, the result
    will be piped through an *Observable*

The details of subscribing to the observable and using the result to carry on
with navigation are fully managed by the platform.

Routing in components
*********************

The ``routerlink`` directive
============================

In HTML Code
------------

Routing links can be directly specified in html code (or generated html
code). The main application component ``AppComponent`` in the *Tour of Pyroes*
has this html code

.. code-block:: html

    <nav>
      <a routerLink="/dashboard" routerLinkActive="active">Dashboard</a>
      <a routerLink="/pyroes" routerLinkActive="active">Pyroes</a>
    </nav>

Using the ``routerlink`` (or ``routerLink`` as you please) attribute means that
the specified path will be passed to the routing engine for processing. If you
had done it the usual way:

.. code-block:: html

    <nav>
      <a href="/dashboard">Dashboard</a>

The routing engine would have no chance do anything and the standard browser
mechanisms would take over, moving to a new URL.

.. note:: The *AnPyLar* engine could also intercept the ``href`` attribute, but
          that would be a permanent dilemma: Is this ``href`` for the routing
          engine or did the user want to specify a real ``href``?

          Using a different attribute clears the ambiguity.


The second directive is: ``routerLinkActive="active"``. This means:

  - Register this route for a callback to the element to add ``active`` to its
    ``class`` attribute.

This gives (via CSS) the possibility:

  - To highlight the element with specific styling when the route is active

  - To remove the specific styling when the route is no longer active


In Python Code
--------------

From the *Tour of Pyroes*

.. code-block:: python

    def render_pyroes(self, pyroes):
        for pyro in pyroes:
            with html.li() as li:  # per-pyro list item
                # per-pyro anchor routing path with parameter pyd
                with html.a(routerlink=('/detail', {'pyd': pyro.pyd})):

        ...

In this example:

  - A *tuple* (it could be a *list*) is passed specifying

    - The ``path`` (1st element of the tuple: a string)

    - ``params`` for the route (2nd element: a *dict*)

The benefit of being able to use this syntax is clear, because it allows
specifying specific parameters for the route

.. note:: One can of course just pass a string (like in html code) and that
          will be path to route to


The ``self.router`` attribute
=============================

*Components* have access to the routing engine via the ``self.router``
attribute. And with it, it can use it to:

  - Go backwards: ``self.router.back()``

  - Go forward: ``self.router.forward()``

  - Go somewhere::

       self.route_to(pathname, **kwargs)

With this last method in the hand we could have created the ``<a ...`` from
above like this:

.. code-block:: python

    def render_pyroes(self, pyroes):
        for pyro in pyroes:
            with html.li() as li:  # per-pyro list item
                # per-pyro anchor routing path with parameter pyd
                with html.a():
                    # use p=pyro to avoid the closure from using the last pyro
                    a._bindx.click(lambda p=pyro: self.goto_to(p))

    def goto_to(self, pyro):
        self.router.route_to('/detail', pyd=pyro.pyd)

It may seem pointless in this small example, but one could foressee a lot of
additional processing in the ``goto_to`` method before actually invoking the
router to ``route_to`` somewhere.

Named Outlet Routing
********************

In addition to the regular routing to the ``<router-outlet>`` tag, named outlet
routing is also possible. The syntax::

  <router-outlet name="the-outlet-name">

This functionality is intended for a kind of *dialog*/*form* service, in which
content can:

  - Be shown in a specific tag, rather than relying on regular routing
    mechanics

  - Be carried over from standard route to standard route

  - Closing is controlled by the component which is rendering inside the tag

Routing to a named outlet
=========================

The routing control happens inside a ``routes`` directive. The syntax::

  {
      'path': 'path-to-intercept',
      'component': ComponentToRender,
      'outlet': 'name-of-the-outlet'
  },

A working sample from the :doc:`tutorial/tourer/index` sample::

  {
      'path': 'compose',
      'component': ComposeMessageComponent,
      'outlet': 'popup'
  },


Closing a named outlet
======================

As explained above, the content inside a named outlet will be carried over when
the application routes from a standard route (unnamed outlet) to another. The
contents inside the named outlet will remain inside the outlet.

.. note:: This of course unless the entire surrounding tag is told to empty
          itself and re-render something else.

          See the :doc:`tutorial/tourer/index` for an example of how the named
          outlet (declared at top level) is carried over.

This means that extra functionality is needed for the controlling component to
decide (using an event for example) when the named outlet has to be *closed*
(i.e.: the component stops rendering inside)

This is achieved via the method::

  Component.close_outlet()

See :doc:`/reference/component` for the details.
