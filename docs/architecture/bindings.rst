Bindings
########

In the :doc:`module` and :doc:`component` sections, it has been explained that
both can host a ``bindings`` declaration. These ``bindings`` are a link
between:

  *Attributes* and *Observables* (see :doc:`/architecture/observables`)

The declaration looks like this.

.. code-block:: python

   from anpylar import Component, html

   ...

   class PyroesComponent(Component):

       bindinds = {
           'pyroes': [],
      }

      ...

This at first seems like a normal *dict* declaration containing a ``pyroes``
key and a matching value of ``[]`` (an empty *list*), but there is more.

Because the declaration happens inside a subclass of ``Component`` the
following holds true:

  - ``PyroesComponent`` will automatically have an attribute named ``pyroes``
    which will obviously have a default value of ``[]``

  - A 2nd attribute named ``pyroes_`` will be available and this is an
    **Observable**

.. note:: Yes, the observable attribute receives the suffix ``_`` (an
          underscore).

          In Python ``_`` is usually doubled before and after a name to
          indicate a Python reserved name, doubled before a name to indicate a
          name-mangled component and used as single character before a name to
          indicate a kind of **reserved** attribute.

          *AnPyLar* has chosen to mark the *bindings* (or *observable
          attributes*) by using a single ``_`` as a **suffix**


.. seealso::  If you are eager, you can also go straight to
              :doc:`/architecture/observables`

Both attributes are linked together so that:

  - Setting the value of ``pyroes`` triggers the *observable* ``pyroes_`` and
    therefore any operations subscriptions to it

  - Setting (or *calling*) the *observable* sets the value of the attribute::

      self.pyroes_([1, 2, 3])  # equivalent to self.pyroes = [1, 2, 3]

Let's see it in code terms

.. code-block:: python

   from anpylar import Component, html

   class Counter(Component):

       bindinds = {
           'count': 0,
      }

      def render(self, node):
          html.h1('{}')._fmt(self.count_)

          with html.button('Count up!') as b:
              b._bindx('click', self.do_count)

      def do_count(self):
          # Alternative -> self.count_(self.count + 1)
          # Alternative -> self.count_ = self.count + 1
          self.count += 1

.. note::

   You can test this simply script with ``anpylar-serve`` without creating a
   complicated structure by placing the contents in a file ``index.py`` and
   doing::

     anpylar-serve --auto-serve index.py

With this basic example the powers of the binding (*attribute* <->
*observable*) could be explained:

.. code-block:: python

          html.h1('{}')._fmt(self.count_)

We are creating an ``<h1>`` with the formatting template ``{}`` as text. This
will be formatted to contain the value delivered by ``_fmt(self.count_)``

Because ``self.count_`` is an *Observable*, there will be a background
subscription to it. Whenever the value of ``self.count`` changes, this will be
reflected as a event through the observable and the value of our ``<h1>`` tag
will change.

.. code-block:: python

          with html.button('Count up!') as b:
              b._bindx('click', self.do_count)

We are now adding a ``<button>`` for which we add an event binding. When
clicked, it will call our ``do_count`` method.

.. note:: Notice the name ``_bindx`` with the trailing ``x``. This is to
          separate it from the ``_bind`` method. With the ``x`` method the
          generated *click* event is not delivered with the callback.

And finally

.. code-block:: python

      def do_count(self):
          # Alternative -> self.count_(self.count + 1)
          # Alternative -> self.count_ = self.count + 1
          self.count += 1

In our ``do_count``, we simply increase the value of ``self.count``. This will
(as explained above) trigger the *observable* ``self.pyroes_`` and update the
value of our ``<h1>`` tag.

Experienced Python programmers will have by now for sure noticed that during
the ``bindx`` operation no ``lambda`` was used and this because ``self.count +=
1`` wouldn't be valid.

.. code-block:: python

          with html.button('Count up!') as b:
              b._bindx('click', lambda: self.count += 1)  # <- NOT VALID

One has to use an expression inside the ``lambda`` and the auto-increment
operation doesn't count as one.

But looking at the alternatives of how to set the value of ``self.count`` using
the *observable* we could have actually used a ``lambda``. For example:

.. code-block:: python

          with html.button('Count up!') as b:
              b._bindx('click', lambda: self.count_(self.count + 1))  # <- VALID

Removing with it the need to have a dedicated ``do_count`` method.

For the sake of it, let's show a final possibility, which is related as how one
declares the event to bind to.

.. code-block:: python

          with html.button('Count up!') as b:
              b._bindx.click(lambda: self.count_(self.count + 1))  # <- VALID

Rather than specifying ``click`` as the first argument of ``_bindx`` it can be
chained in standard dot notation, leaving the ``lambda`` as the only argument
inside the call.

We believe this is actually a lot more readable, but the programmer is king.
