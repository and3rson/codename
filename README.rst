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

    # Capitalize
    $ codename -c
    Unexpected Dragon

    # Uppercase
    $ codename -u
    STALKING BATTERY

    # Custom separator
    $ codename -s _
    exploding_crab

    # Deterministic codenames
    $ codename -i 1.2.3+foo
    diamond guitar
    $ codename -i 1.2.3+foo
    diamond guitar

    $ codename -h
    usage: codename.py [-h] [-c] [-u] [-s SEPARATOR]

    optional arguments:
      -h, --help            show this help message and exit
      -c, --capitalize      Capitalize words.
      -u, --uppercase       Upper-case each word.
      -s SEPARATOR, --separator SEPARATOR
                            String to use to join words. Defaults to whitespace.
      -i ID, --id ID        String to use as random seed for deterministic
                            codenames.
