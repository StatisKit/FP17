.. image:: https://img.shields.io/badge/License-Apache%202.0-yellow.svg
   :target: https://opensource.org/licenses/Apache-2.0
   
.. image:: https://travis-ci.org/StatisKit/FP17.svg?branch=master
   :target: https://travis-ci.org/StatisKit/FP17
  
.. image:: https://ci.appveyor.com/api/projects/status/bwc7elajp21arif0/branch/master?svg=true
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

To reproduce the studies with **Docker** use these `images <https://hub.docker.com/r/statiskit/fp17/tags>`_.
After `installing <https://docs.docker.com/engine/installation/>`_ **Docker**, you can type the following commands in a shell:

  .. code-block:: console

    docker run -i -t -p 8888:8888 statiskit/fp17:v1.0.0
  
Then, follow the given instructions.
  
.. note::

    These images correspond to the ones used for the article.
    Most recent images can be runned using these commands in a shell: 

      .. code-block:: console

        docker run -i -t -p 8888:8888 statiskit/fp17:latest
    
Install it !
============
  
You can also install required packages on your computer to reproduce these studies.
In order to ease the installation of these packages on multiple operating systems, the **Conda** `package and environment management system <https://conda.io/docs/>`_ is used.
For more information refers to the **StatisKit** software suite documentation concerning prerequisites to the `installation <http://statiskit.readthedocs.io/en/latest/user/install_it.html>`_ step.
Then, to install the required packages, proceed as as follows:

1. Clone this repository,

   .. code:: console
   
     git clone --recursive https://github.com/StatisKit/FP17
     
2. Create a **Conda** environment containing the meta-package :code:`fp17`,
      
   .. code:: console

     conda create -n fp17py3k fp17=1.0.0 python=3 -c statiskit -c defaults --override-channels

   .. note::

     This meta-package corresponds to the one used for the article.
     Most recent meta-package can be installed by replacing :code:`fp17=1.0.0` by :code:`fp17` in previous command lines.
     Moreover, if you replace the :code:`statiskit` channel by the :code:`statiskit/label/unstable` channel, you will benefit from the latest meta-package available that has not yet been released.
     
3. Activate the **Conda** environment as advised in your terminal.

4. Enter the directory containing **Jupyter** notebooks,

   .. code:: console
   
     cd FP17
     cd share
     cd jupyter
     
5. Launch the **Jupyter** the `index.ipynb <jupyter/index.ipynb>`_ notebook,

   .. code:: console

     jupyter notebook index.ipynb
     
6. Execute the `index.ipynb <share/jupyter/index.ipynb>`_ notebook to execute all examples or navigate among referenced notebooks to execute them separatly.
