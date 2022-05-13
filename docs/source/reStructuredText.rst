=========================
What is reStructuredText?
=========================

It's primarily a format of choice for `docutils <https://docutils.sourceforge.io/rst.html>`_
an open-source system for processing plain-text into a number of documentation-specific and other formats. It's popular in the Python community.

EN docs for reST are great and comprehensive, so let's have this bit in PL instead without any official localization. 

===========================
Czym jest reStructuredText?
===========================

To główny format wykorzystywany przez `docutils <https://docutils.sourceforge.io/rst.html>`_: otwartoźródłowy system wykorzystywany w społeczności Pythona do tworzenia dokumentacji (i innych formatów) z plików tekstowych.

Ściągawka:
----------
oparta na 
https://docutils.sourceforge.io/docs/user/rst/cheatsheet.txt

Tabele
-------


+--------------------------------+-----------------------------------+
| Akapity do lewego marginesu    | blok poprzedzony           "::":: |
| rozdzielone pustymi liniami.   |                                   |
|                                |     Z wcięciem                    |
|     Blok cytatu z wcięciem.    |                                   |
+--------------------------------+ lub::                             |
| >>> print 'blok Doctest'       |                                   |
| blok Doctest                   | > Cytat                           |
+--------------------------------+-----------------------------------+
| | bloki z zachowaniem łamania linii i wcięć. [nowe w 0.3.6]        |
| |     Przydatne przy adresach, poezji, list bez ozdobników; długie |
|       linie można zawijać.                                         |
+--------------------------------------------------------------------+

Proste tabele:
--------------

================  ============================================================
Typ Listy         Przykłady (składania w `tekście <cheatsheet.txt>`_)
================  ============================================================
punkty            * items begin with "-", "+", or "*"
numery            1. dowolny typ notacji "1.", "A)", oraz "(i)"
                  #. automatyczna numeracja
definicje         Termin do lewej : opcjonalna klasyfikacja
                      Definicja z wcięciem w kolejnej linii (bez odstępu)
pola              :nazwa pola: treść pola
Opcje             -o  co najmniej 2 spacje między opcją a opisem
================  ============================================================

