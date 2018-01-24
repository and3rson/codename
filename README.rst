.. content-start

Codename
========

A codename generator inspired by `projectcodename.com <http://projectcodename.com>`_

Installation
============

.. code:: bash

    $ pip install codename

Usage
=====

Command-line usage:

.. code:: bash

    $ codename
    killer unicorn

    $ codename -c
    Unexpected Dragon

    $ codename -u
    STALKING BATTERY

    $ codename -s _
    exploding_crab

    $ codename -h
    usage: codename.py [-h] [-c] [-u] [-s SEPARATOR]

    optional arguments:
      -h, --help            show this help message and exit
      -c, --capitalize      Capitalize words.
      -u, --uppercase       Upper-case each word.
      -s SEPARATOR, --separator SEPARATOR
                            String to use to join words. Defaults to whitespace.
