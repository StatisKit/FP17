.. image:: https://img.shields.io/badge/License-Apache%202.0-yellow.svg
   :target: https://opensource.org/licenses/Apache-2.0
   
.. image:: https://travis-ci.org/StatisKit/FP17.svg?branch=master
   :target: https://travis-ci.org/StatisKit/FP17
  
.. image:: https://ci.appveyor.com/api/projects/status/bwc7elajp21arif0/branch/master
   :target: https://ci.appveyor.com/project/pfernique/fp17/branch/master

Material for the paper entitled "**AutoWIG**: automatic generation of *Python* bindings for *C++* libraries" and submitted to PeerJ Computer Science
====================================================================================================================================================

This repository contains supplementary material for the reproducibiliy of computational studies performed in the article "**AutoWIG**: automatic generation of *Python* bindings for *C++* libraries" written by:

* Pierre Fernique,
* Christophe Pradal.

This article has been submitted to the "PeerJ Computer Science" journal.
Here is the the citation formated as the bibtex standart.

.. code-block:: bibtex

  @article{FP17,
    author    = {Pierre Fernique and Christophe Pradal},
    title     = {{AutoWIG}: Automatic Generation of {Python} Bindings for {C++} Libraries},
    journal   = {CoRR},
    volume    = {abs/1705.11000},
    year      = {2017},
    url       = {http://arxiv.org/abs/1705.11000},
    timestamp = {Wed, 07 Jun 2017 14:40:24 +0200},
    biburl    = {http://dblp.uni-trier.de/rec/bib/journals/corr/FerniqueP17},
    bibsource = {dblp computer science bibliography, http://dblp.org}
  }

These studies are formatted as pre-executed **Jupyter** `notebooks <https://jupyter.readthedocs.io/en/latest/index.html>`_.
Refers to the `index.ipynb <share/jupyter/index.ipynb>`_ notebook which presents and references each study.

Test it !
=========

Using **Docker** `images <https://docs.docker.com/>`_  and **Binder**  `servers <http://docs.mybinder.org/>`_ , we are able to provide ways to reproduce the article studies without installing the **StatisKit** software suite.
    
Online with **Binder**
----------------------

.. warning::

   Currently, **Binder** does not work with this repository due to timeouts.
   
To reproduce the studies online, use this `server <https://beta.mybinder.org/v2/gh/statiskit/fp17/v1.0.0?filepath=share/jupyter/index.ipynb>`_.

.. note::

   This server corresponds to the one used for the article.
   Most recent server can be runned using this `link <https://beta.mybinder.org/v2/gh/statiskit/fp17/master?filepath=share/jupyter/index.ipynb>`_.

On your computer with **Docker**
--------------------------------

To reproduce the studies with **Docker** use these `images <https://hub.docker.com/r/statiskit/fp17/tags>`_.
After `installing <https://docs.docker.com/engine/installation/>`_ **Docker**, you can type the following commands in a shell:
  
* For the *Python 2* version 

  .. code-block:: console

    docker run -i -t -p 8888:8888 statiskit/fp17:v1.0.0-py2k
   
* For the *Python 3* version 

  .. code-block:: console

    docker run -i -t -p 8888:8888 statiskit/fp17:v1.0.0-py3k
  
Then, follow the given instructions.
  
.. note::

    These images correspond to the ones used for the article.
    Most recent images can be runned using these commands in a shell:

    * For the *Python 2* version 

      .. code-block:: console

        docker run -i -t -p 8888:8888 statiskit/fp17:latest-py2k
   
    * For the *Python 3* version 

      .. code-block:: console

        docker run -i -t -p 8888:8888 statiskit/fp17:latest-py3k
    
Install it !
============
  
You can also install required packages on your computer to reproduce these studies.

.. warning::

  To use the examples without **Docker** you must first follow instructions available on this `page <http://statiskit.readthedocs.io/en/latest/developer/configure.html>`_.
  
In order to ease the installation of these packages on multiple operating systems, the **Conda** `package and environment management system <https://conda.io/docs/>`_ is used.
For more information refers to the **StatisKit** software suite documentation concerning prerequisites to the `installation <http://statiskit.readthedocs.io/en/latest/user/install_it.html>`_ step.
Then, to install the required packages, proceed as as follows:

1. Clone this repository,

   .. code:: console
   
     git clone --recursive https://github.com/StatisKit/FP17
     
2. Enter the cloned repository,

   .. code:: console
   
     cd FP17
     
3. Install the given **Conda** environment,

   .. code:: console

     conda env create -f environment.yml
  
4. Activate the **Conda** environment as advised in your terminal.

5. Enter the :code:`share` repository,

   .. code:: console
   
     cd share
     
6. Enter the :code:`jupyter` repository,

   .. code:: console
   
     cd jupyter
     
7. Launch the **Jupyter** the `index.ipynb <jupyter/index.ipynb>`_ notebook,

   .. code:: console

     jupyter notebook index.ipynb
     
8. Execute the `index.ipynb <share/jupyter/index.ipynb>`_ notebook to execute all examples or navigate among referenced notebooks to execute them separatly.
