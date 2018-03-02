Http Client
###########

The ``Http`` client is a class which can be instantiated to access web services
via *Ajax*. It is implemented as an *Observable* which allows anyone to
subscribe to it and perform operations on the results.

It is located inside ``anpylar.http``. For example::

  my_http = anpylar.http.Http()

Class Constructor
*****************

```Http(url='', headers=None, fullresp=False)```

  - ``url`` is the base url, which can be later extended when calling a method

  - ``headers`` is a dict with the headers. It can later be extended by each
    method

  - ``fulresp`` if ``False``, the body of responses with status codes between
    ``200`` and ``299`` will be returned

    If ``True`` the complete response will be returned. It will only be a
    failure if there is actually a failure in the connection (the browser
    blocks it, the connection times out, ...)


Methods
*******

  - ``get(url='', headers=None, data=None)``

    Issue a ``GET`` method extending the ``url`` and ``headers`` and adding any
    ``data`` passed

    *Returns*: *Observable*

  - ``post(url='', headers=None, data=None)``

    Issue a ``POST`` method extending the ``url`` and ``headers`` and adding any
    ``data`` passed

    *Returns*: *Observable*

  - ``put(url='', headers=None, data=None)``

    Issue a ``PUT`` method extending the ``url`` and ``headers`` and adding any
    ``data`` passed

    *Returns*: *Observable*

  - ``delete(url='', headers=None, data=None)``

    Issue a ``DELETE`` method extending the ``url`` and ``headers`` and adding
    any ``data`` passed

    *Returns*: *Observable*
