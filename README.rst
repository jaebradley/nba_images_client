NBA Images Client
=================

|Build Status|

Introduction
------------

A Python client to retrieve team logo and player head shot images from
NBA.com

Installation
------------

``pip install nba_images_client``

API
---

Get Team Logo
~~~~~~~~~~~~~

Returns a team's logo as bytes. Returns ``PNG`` (default) or ``JPG``.
Also, allows resizing, based on input dimensions. The default dimensions
are ``150x150``.

.. code:: python

    from nba_images_client import NbaImagesClient, Team, FileType, ImageDimensions

    # Get a 150x150 PNG of the Boston Celtics logo in bytes
    default_celtics_logo = NbaImagesClient.get_team_logo(team=Team.BOSTON_CELTICS)

    # Get a 400x400 JPG of the Boston Celtics logo in bytes
    celtics_logo_400_by_400_jpg = NbaImagesClient.get_team_logo(team=Team.BOSTON_CELTICS, file_type=FileType.JPG, image_dimensions=ImageDimensions(height=400, length=400))

Get A Player's Head Shot
~~~~~~~~~~~~~~~~~~~~~~~~

Returns a player's head shot as bytes. Returns ``PNG`` (default) or
``JPG``. Allows resizing, based on input dimensions. The default
dimensions are ``260x190``.

.. code:: python

    from nba_images_client import NbaImagesClient, Team, FileType, ImageDimensions

    # Get a PNG of Isaiah Thomas' head shot in bytes
    isaiah_thomas_head_shot = NbaImagesClient.get_player_head_shot(player_id=202738)

    # Get a 400x400 JPG of Isaiah Thomas' head shot in bytes
    isaiah_thomas_head_shot_400_by_400_jpg = NbaImagesClient.get_player_head_shot(player_id=202738, file_type=FileType.JPG, image_dimensions=ImageDimensions(height=400, length=400))

.. |Build Status| image:: https://travis-ci.org/jaebradley/nba_images_client.svg?branch=master
   :target: https://travis-ci.org/jaebradley/nba_images_client
