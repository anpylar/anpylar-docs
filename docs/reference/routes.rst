Routes
######

The specification of routes happens in a module in the directive ``routes``

.. code-block:: python

    class MyModule(Module):

        routes = [route_defininitions]


That is: an iterable (list, tuple) of route_definitions.

Route Definition
----------------

A route definition is a ``dict`` which can contain the following
``key`` / ``value`` pairs

  - ``path`` (a string)

    Used to match the route in the browser. This ``path`` will be appended to
    the ``baseurl`` of the app (automatically calculated)

    The ``path`` of child routes will be appended to that of parent routes

    if ``path`` is ``*`` or ``**`` it will be the last resort
    (route-not-found) route

    The ``path`` can start with a leading slash if wished for clarity.

  - ``component`` (a subclass of ``anpylar.Component``)

    Which component will be loaded when the route is a match. In the case of
    nested child routes, several components can be instantiated, one for each
    child, when a route is hit

  - ``params`` (a *dict*)

    The dictionary key is the name of the param for the route and the value is
    a transformation function. For example::

      'params': {'did': int},  # transformation function

    ``did`` will show up as an int.

    ``None`` can be specified as a transformation function to leave the
    parameter untouched (i.e.: deliver it as a string)

  - ``path_match`` (string ``full``) Either not present or with the value
    ``full``. Used to match a route when the others have failed and the
    remaining content fully matches the ``path``

  - ``redirect_to`` (string referencing a ``path``)

    If this is set, the route will redirec to to a different url (within the
    application)


  - ``load_children`` (an iterable of ``anpylar.Module`` subclasses)

    Used to load other modules as sub-modules and include the routing (under
    the defined ``path``) in this routing

  - ``can_activate`` (an iterable of ``anpylar.AuthGuard`` subclasses) which
    will determine if the given ``path`` can be navigated to

  - ``children`` (an iterable of route_definitions) Effectively this defines a
    new hierarchy of routes that are appended to the defined ``path`` of the
    entry.

  - ``outlet`` (a string) This defines a route which will render the associated
    component inside a named outlet. Other outlets at the same level will
    remain unaffected.

Some examples now.

From the *Tourer* sample
************************

The defined routes in the main module are::

    routes = [
        {
            'path': 'compose',
            'component': ComposeMessageComponent,
            'outlet': 'popup'
        },

        {'path': 'disaster-center', 'load_children': [DisasterCenterModule]},

        {'path': 'admin', 'load_children': [AdminModule]},

        {'path': '', 'redirect_to': '/superpyroes', 'path_match': 'full'},

        {'path': '*', 'component': PageNotFoundComponent},
    ]

And from the ``DisasterCenterModule``
::

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


Being defined in a sub-module and loaded with ``load_children`` the entire set
is a child of the main routing definition. This definition contains also nested
children.
