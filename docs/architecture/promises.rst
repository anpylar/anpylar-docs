Promises
########

For the reference see: :doc:`/reference/promise`

*AnPyLar* ships with its own version of *Promises*. The standard Python library
has *Futures* (the *asyncio* one) but *Promises* go simply a step
beyond. *Promises* are built on top a slighty (yet compatbible) modified
version of the *Futures* to allow setting anything as an error, rather than
just a *Exception*.

The implementation is made following the guidelines of *Promises/A+* (or
Promises-Aplus)

  - `Web Site <https://promisesaplus.com/>`_

  - `Specification Repo <https://github.com/promises-aplus/promises-spec>`_

You may also check the documentation from *MDN Web Docs*

  - `Promise@MD
    <https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise>`_

Quick introduction
******************

A *Promise* is an object that takes an *executor* (a *callable* in Python
slang) which will be executed by the promise during construction. The
*executor* will ideally start an asynchronous operation (like downloading a web
page in the background)

The *executor* is invoked with *callables*

  - The ``resolve`` function which the *executor* has to invoke if the
    operation succeeded.

  - The ``reject`` function which the *executor* has to invoke if the operation
    failed.

When the *Promise* has been created, one can aweit *resolution* or *rejection*
by:

  - Invoking ``then(callable)`` for resolution.

    The *callable* has to accept 1 parameter which will contain the *result*
    that led to the resolution of the promise.

  - Invoking ``catch(callable)`` for rejection.

    The *callable* has to accept 1 parameter which will contain the *error*
    that led to the rejection.

These can be chained and not once ... but actually as many times as wished.

Let's go for a practical example:

.. code-block:: python

    from anpylar import Promise, call_delayed

    def executor(resolve, reject):
        call_delayed(1000, lambda: resolve(1))

    mypromise = Promise(executor) \
                    .then(lambda x: x * 2) \
                    .then(lambda x: x * 3) \
                    .then(print)

As you may expect this will print the following (after 1000ms, i.e.: 1s) in the
developer console::

  6

.. note::

   You can test this simply script with ``anpylar-serve`` without creating a
   complicated structure by placing the contents in a file ``index.py`` and
   doing::

     anpylar-serve --auto-serve index.py

We have chained several operations and they have been executed. Let's see what
would happen if the promise ended up in rejection.

.. code-block:: python

    from anpylar import Promise, call_delayed

    def executor(resolve, reject):
        call_delayed(1000, lambda: reject('Blistering Barnacles!'))

    mypromise = Promise(executor) \
                    .then(lambda x: x * 2) \
                    .then(lambda x: x * 3) \
                    .then(print) \
                    .catch(lambda x: print('Error:', x))

Which prints::

  Error: Blistering Barnacles!

A more real example
*******************

So far we have only delayed the execution of call with ``call_delayed``, but we
can do some real world job, for example:

.. code-block:: python

    from anpylar import Promise, Http


    def executor(resolve, reject):
        def _resolver(resp):
            resolve(resp[0:min(50, len(resp))])  # 1st 50 chars of the answer

        def _rejecter(error):
            reject(error)

        Http().get('http://127.0.0.1:2222/index.html') \
            .catch_exception(lambda x: None if _rejecter(x) else None) \
            .filter(lambda x: x is not None) \
            .subscribe(_resolver)


    Promise(executor) \
        .then(lambda x: print('Promise.then:', x)) \
        .catch(lambda x: print('Promise.catch: Error happened', x))

If you run this, the console will show the following::

    Promise.then: <!DOCTYPE html>
    <html>
    <head>
      <title>The Title

Let's change a line to break our code by setting the port to ``2223``::

        Http().get('http://127.0.0.1:2223/index.html') \

And the console will now say::

    GET http://127.0.0.1:2223/index.html net::ERR_CONNECTION_REFUSED
    Promise.catch: Error happened

The ```GET ...`` error message is from the browser. Our ``catch`` method was
invoked and we know an error happened. Meanwhile, the ``then`` code was left
alone.

The real code now
*****************

*Observables* can be easily turned into *Promises* ... you don't have to do the
work yourself.

.. code-block:: python

    from anpylar import Http

    Http().get('http://127.0.0.1:2222/index.html') \
        .to_promise() \
        .then(lambda x: print('Promise.then:', x)) \
        .catch(lambda x: print('Promise.catch: Error happened', x))

The ``to_promise`` operator turns the *Observable* into a *Promise* and forces
an internal subscription to make sure things reach either ``then`` or
``catch``. Play with it ...
