Part 6-Plus - REAL Networking
*****************************

Copy the ``top6`` folder to ``top6-plus`` and enter it. For example, with::

  cp -r top6 top6-plus

.. note:: Under *Windows* and unless you have a proper shell installed
          (*Cygwin*, *MSYS*, *GitBash*, ...) you are probably better off
          using the *Windows Explorer* to make a copy of the directory)


We have left our *Pyroes* hanging from a thread, because they are being fetched
from the network ... but still a virtual network. Being real *Pyroes* they
really want to go the distance.

Any avid reader has probably already wondered why not doing it altogether,
given that we have the tools at our disposal:

  - A set of services (``PyroService`` and ``PyroSearchService``) which use the
    generic ``Http`` interface available in *AnPyLar*

  - A single conditional definition in ``app_module.py`` to serve data locally

    .. code-block:: python

       if True:
           from .mock_pyroes import Pyroes
           Http.serve(Pyroes, index='pyd', url='api/pyroes/')

  - An ``anpylar-serve`` command which is offering a web server on port 2222

**And yes!** The simple server in ``anpylar-serve`` can also serve a simple
*CRUD* interface. An excerpt from the ``anpylar-serve --help`` command::

  $ anpylar-serve --help

  ...
  ...

  API options:
    --api-url API_URL     URL path when serving an API request (default: )
    --api-mod API_MOD     Which python source file contains the data (default: )
    --api-data API_DATA   Name of the variable holding teh data (default: )
    --api-index API_INDEX
                          Name of the field which will serve as an index
                          (default: )

The layout hasn't changed and the application is not going to change
either. Simply edit ``app_module.py`` to remove the inclusion of the local
data:

.. tabs::

   .. code-tab:: python app_module.py

       if False:  # <<-- SET THIS TO FALSE
           from .mock_pyroes import Pyroes
           Http.serve(Pyroes, index='pyd', url='api/pyroes/')

Set the condition to ``False``. If you are brave ... **delete the 3 lines**. It
doesn't make a difference.

And now serve the application ... this time with a longer command::

  anpylar-serve top6-plus \
    --api-url /api/pyroes/ \
    --api-mod tour-of-pyroes/top6/app/mock_pyroes.py \
    --api-data Pyroes \
    --api-index pyd

And go the browser

  http://127.0.0.1:2222

We have used backslashes to make the command line readable. We have opened the
developer console and highlighted the first network request from the browser to
fetch the list of *Pyroes*

.. thumbnail:: top6plus-dashboard-api-pyroes.png

You can do the and play with the application. Everything will be fetched from a
real server. Ok ... it's only the toy development server which can act as a
CRUD server, but proves the point: the ``Http`` code was generic enough to hit
the network with no changes to ``PyroService`` and ``PyroSearchService``

That means that our *Pyroes* are free to navigate the perils of the network or
who knows to save us from those perils without us noticing such a feat. All
hail the *Pyroes*!
