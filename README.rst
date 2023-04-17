What is runish?
===============

A Unicode name finder and characters explainer.

Simple to use::

    $ runish umbrella
    ☂  UMBRELLA
    ☔ UMBRELLA WITH RAIN DROPS
    ⛱  UMBRELLA ON GROUND
    🌂 CLOSED UMBRELLA
    🏖 BEACH WITH UMBRELLA

    $ runish ☂
    UMBRELLA

In that simple use case it tries to guess what are you asking for (one letter -> explain; more -> find). 

You can also be explicit passing ``-e/--explain`` or ``-f/--find`` to select the behaviour mode::

    $ runish -e bœuf
    b  LATIN SMALL LETTER B
    œ  LATIN SMALL LIGATURE OE
    u  LATIN SMALL LETTER U
    f  LATIN SMALL LETTER F
