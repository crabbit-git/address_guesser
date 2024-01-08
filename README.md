# Address Guesser

Address Guesser is a Python script that uses random number generation to figure
out partially obfuscated URIs containing numbers in a known pattern. It does so
by sending HTTP requests to guessed URIs and recording any URIs that respond
with an acknowledgement that they are valid (200).

Each URI tested is recorded in the plain text file tested_urls.txt. This is
primarily so that the same randomly generated URIs are not tested repeatedly, as
there is probably little point in re-testing the same URI if you know it's not
valid (though of course it is possible that an invalid URI may later start
being used and thus become valid, but you can retest by removing URIs from the
file).

If a URI is valid, it should respond with a 200, in which case it is also
recorded in valid_urls.txt so that it can be accessed later.

## No licence? What are you, some kind of amateur?

This is provided with no licence intentionally because it is a blunt object that
could be used to hammer servers with an unreasonable number of HTTP requests and
I do not want anybody blaming me if they use it to do that and face negative
consequences as a result. So you can see what I did if you're curious, but all
rights are reserved and you may not consider yourself entitled to use this
script for abusive purposes.

## What's the point, then?

This was just a practice exercise for my own amusement, because I hadn't used
Python for a while and I wanted to refresh my memory a bit. (I've been a full
stack .NET engineer for the past year.)

The thing that inspired its creation was a much simpler, less adaptable, and
morally questionable script written by someone who posted theirs on Reddit (it
was quickly taken down, for good reason, but I won't go into details because it
isn't really relevant to what I did myself). I initially just wanted to see if I
could create something with roughly equivalent functionality, then decided to
flesh it out a bit so that it could hypothetically be a bit more useful (though
I haven't really found a worthwhile use case for it and I possibly never will).

## Requirements

A working Python installation, obviously. That's pretty much it.

## How do I use it?

Well... chances are, you don't, given the whole "no licence" thing. But this is
a README, so I should probably at least summarise how it works.

The URI pattern must be provided in a plain text file, with "{random}" marking
the spot at which the randomly generated numbers are to be inserted. The file
name is not fixed, as it is provided to the script when it is run.

If address_guesser.py is run from a terminal, it will ask the user to specify
the following:

1. How many valid URIs are to be generated
2. The range within which random numbers are to be generated
3. The path to the plain text file containing the URI pattern

The tested_urls.txt and valid_urls.txt files will be created on first run if
they do not exist already.

The script will run until it reaches the specified target number of valid URIs,
so if you want to stop it before that happens (which is important because it
might never happen at all), you can do so with the old faithful Control + C.
