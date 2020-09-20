
This site uses several models.  Here they are explained.

Generic
=======

Almost all models contain a creation date, a publication date and an archive date.

When the archive date is passed, the model instance will be archived.

News
====

Holds news items with a location, a header, and Dutch and English text.
And active and archive boolean fields.  This is ordered by publication date.

Manifest
========

Holds maniafests with a header, and Dutch and English text.
And active and archive boolean fields.  This is ordered by publication date.

Landprice
=========

Contains the types of the art objects:

 - Painting
 - Drawing
 - Photo
 - Statue
 - Media

Beside the type it also contains a header, a Dutch and English text, an active
boolean field, and an order of the model by type.

There will be a static method to get the price of a piece of art.

Content
=======

Each content model instance needs to contain these five unique fields: section, key, language and order:

 - section is one of
   - home,
   - news,
   - archive,
   - news archive,
   - manifest archive,
   - manifest
   - land price,
   - about my art,
   - art,
   - contact

 - key: any string (must be one word)

 - language: None, en (English) or nl (Dutch)

 - order: an small positive integer

Beside these fields, there is the rich text value field and an identifier object.

Tag
=====

Tags can be added to works of art.

Artist
======

An artist has a name, a link, an image and an activity field.

Art
=====

Art is the most important model.

 - name: The name of the work of art.
 - tags: The tags related to this work of art. [The Tag model]
 - artist: The artist. [The Artist model]
 - image: The image of the work of art.
 - land_price: The landprice related with this work of art.  TODO: should come from the Landprice model
 - x: The number of centimeters on the x-axis.
 - y: The number of centimeters on the y-axis.
 - z: Depth of the piece.
 - materials: The used materials.
 - active: If set the work of art will be shown, otherwise it will not.
 - in_private_collection: When set this work is sold, or unavailable.
 - archived: If set the art will be part of the archive section.

Contact
=======

Contains contact information of an Artist.
