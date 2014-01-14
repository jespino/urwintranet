urwintranet
===========

.. image:: http://kaleidos.net/static/img/badge.png

.. image:: https://api.travis-ci.org/kaleidos/greenmine-ncurses.png?branch=master
    :target: https://travis-ci.org/kaleidos/greenmine-ncurses
.. image:: https://coveralls.io/repos/jespino/urwintranet/badge.png?branch=master
    :target: https://coveralls.io/r/jespino/urwintranet?branch=master
.. image:: https://d2weczhvl823v0.cloudfront.net/jespino/urwintranet/trend.png
    :alt: Bitdeli badge
    :target: https://bitdeli.com/free

A NCurses client for the Kaleidos intranet.

Setup development environment
-----------------------------

Just execute these commands in your virtualenv(wrapper):

.. code-block::

    $ pip install -r dev-requirements.txt
    $ python setup.py develop
    $ py.test           # to run the tests
    $ urwintranet         # to run the app
    

Obviously you need the `intranet backend`_ and, if you consider yourself a loser,
you can use the `intranet web client`_, sometimes. ;-)

Note: urwintranet only runs with python 3.3+.

.. _intranet backend: https://github.com/kaleidos/intranet
.. _intranet web client: https://github.com/kaleidos/intranet/tree/master/clients/antranet
