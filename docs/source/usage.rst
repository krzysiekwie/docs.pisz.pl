Usage
=====

.. _installation:

Installation
------------

To use docs.pisz.pl read it, think and get in touch; if you want to install it try pip:

.. code-block:: console

   (.venv) $ pip install piszpl

Writing docs
----------------

To retrieve a list of random topics,
you can use the ``piszpl.get_random_docs()`` function:

.. autofunction:: piszpl.get_random_docs

The ``kind`` parameter should be either ``"ux"``, ``"translation"``,
or ``"localisation"``. Otherwise, :py:func:`piszpl.get_random_docs`
will raise an exception.

.. autoexception:: piszpl.InvalidKindError

For example:

>>> import lumache
>>> piszpl.get_random_docs()
['api', 'microcopy', 'tutorial']

