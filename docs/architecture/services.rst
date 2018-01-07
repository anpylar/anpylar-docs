Services
########

For the reference see :doc:`/reference/service`.

Simple Services
***************

A *Service* can be just anything which can provide *Modules* and *Components*
with a service. They can be declared with the *services* directive. A complete
example:

.. code-block:: python

    from anpylar import Component, Module


    class MyService:
        count = 0

        def next_count(self):
            self.count += 1
            return self.count


    class MyComponent(Component):
        htmlsheet = '''
        <h2 [counter_]>The count is {}</h2>
        <button (click)="countup()">Count</button>
        '''

        bindings = {'counter': 0}

        def countup(self):
            self.counter_(self.myservice.next_count())


    class MyModule(Module):
        services = {'myservice': MyService}
        components = MyComponent


    MyModule()

The service has been declared in the module::

    class MyModule(Module):
        services = {'myservice': MyService}

And is simply used in the component::

        def countup(self):
            self.counter_(self.myservice.next_count())


Just like this service provides a simple counter, it can for example provide a
service to fetch data from the network. From the *Tour of Pyroes* tutorial.

.. code-block:: python

    from anpylar import http, Observable
    from .pyro import Pyro

    import json

    class PyroSearchService:
        def __init__(self):
            self.http = http.Http(
                url='api/pyroes/',
                headers={'Content-Type': 'application/json'},
            )

        def search(self, term):
            return self.http.get(data={'name': term}) \
                .map(lambda x: [Pyro(**p), for p in json.loads(x)])


Which indeed connects to the network to retrieve *Pyroes* containing ``name``
in the Pyro's name.

Subclassing from ``Service``
****************************

In order for full integration in the platform, custom services can be
subclasses of ``Service``. This brings the benefit of:

  - Attribute searching in parent classes

I.e.: when an attribute cannot be found in the current service instance, the
attribute will be sought in its *parent*. The *parent* is the *Component* or
*Module* in which it is defined.

Bear in mind that following the attribute searching policy of *Component* and
*Module* classes, the search can progress further up the hierarchy.

This allows, for example, that a service uses some other services which have
been defined elsewhere.

All that is neede for this is

.. code-block:: python

    from anpylar import Component, Module, Service


    class MyService(Service):
        count = 0

        def next_count(self):
            self.count += 1
            return self.count

    ...

As easy as subclassing.


The Service *Namespace*
***********************

In both *Component* and *Module* classes, one can define the following
directive::

.. code-block:: python

    class MyComponent(Component):
        service_ns = True

This will be like if the *service namespace* will have been declared as::

  service_ns = '_s'

or

.. code-block:: python

    class MyComponent(Component):
        service_ns = 'myservices'


In both cases, the service instances will no longer be installed directly as
attributes of the holding instance, but inside an attribute ``self._s`` (the
first case above) or ``self.myservices`` (the 2nd case above)

Extending the examples above.

.. code-block:: python

    class MyComponent(Component):
        service_ns = True

        services = {'super_service': SuperService}

        def loading(self):
            self._s.super_service.load_super_items()

or with an explicit declaration

.. code-block:: python

    class MyComponent(Component):
        service_ns = 'myservices'

        services = {'super_service': SuperService}

        def loading(self):
            self.myservices.super_service.load_super_items()
