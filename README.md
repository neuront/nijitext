NijiPress
=========

* Have `python` (2.5+) installed (but not python 3.x);
* Get the source via git;
* Run `make doc`, then documentations like **gaeconf.html** will be generated;
* Please read **gaeconf.html** first.

Note: if your `python` is a symlink to python 3.x, `make doc` would fail. You could use

    $ make doc PYTHON=python-interpreter

to specify the interpreter.
