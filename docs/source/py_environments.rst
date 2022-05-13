====================
Python Environments  
====================

Quick Guide  
-----------

    Q: Do I need a virtual environment?
    A: If you need to ask, chances are you don't.

On the other hand, you're going to need them at some point, so why not start now - especially if you're on a system (Linux) that has Python pre-installed and depends on a version older than the one you want to use for your projects.

With an environment for your projects you'll be able to use different Python version than the one on your system. Or have different versions of Python for your projects. Same goes for the modules. Different versions in different projects but also different modules in different projects. 

Chances are you're going to work on several different projects at the same time and while your flask or django backend may need WTForms, numpy and pandas may only be needed elsewhere.

    One thing to consider is whether you want your environments (each is actually a folder) inside your project folders (one per project) or under your user folder (several projects may use the same environment)

Most popular environment managers are:

1. venv_
    modern standard for Python 3
#. virtualenv
    still popular - works with Python 2 & 3
#. pipenv
    less popular - creates and manages your virtual environments (pipfile, pip and virtualenv in one)
#. conda 
    included in Anaconda and Miniconda - popular with the data science and machine learning crowd
#. poetry
    least popular - similar to pipenv but also handles packaging and publishing to PyPi

venv_
-----
(virtualenv works the same just use ``virtualenv`` instead of ``venv``
on Windows make sure you call your python interpreter correctly ``py`` or ``python``)

Installing::
    python3 -m pip install --user venv
Creating::
    python3 -m venv environment-name
Activating::
    source -m venv environment-name
Activating on Windows::
    \environment-name\Scripts\activate.bat
Deactivating::     
    deactivate
