Introduction
############

*AnPyLar* is the first **Python** front-end framework for building user
interfaces, which allows to manage and simplify web development.

It is modelled following the concepts developed by *Google* with *Angular* (v2
and later), but with a Pythonic approach in mind.

The goal is not only to allow easy development of small or large and complex
Single Page Application (*SPA*) but to allow all Python backend programmers to
make the jump to front-end development.

To open your appetite here is a simple fully embedded component:

.. code-block:: python

   class HelloWorld(Component):

       htmlsheet = '''<h1>Hello {name}</h1>'''
       stylesheet = '''
           h1 {
               color: red;
               margin-left: 20px;
           }
       '''

       def render(self, node):
           with node.select('h1') as h1:
              h1._fmt(name=self.params.get('name', 'John Doe'))


If the route taking the application to this component carries a ``name``
parameter, it will be displayed. If not, ``John Doe`` will be shown.
