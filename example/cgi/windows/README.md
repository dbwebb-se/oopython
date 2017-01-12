How to run Python as CGI on XAMPP
==========

Install XAMPP
--------------

You have XAMPP installed, it is preconfigured to allow CGI-scripts which ends in `.cgi`.


Install Python in Windows
--------------

1. Install Python as part of windows.

1. Add the path to the python installation directory, and `python.exe`, to your `PATH` variable.

Verify by executing `python` in your terminal.


Run Python as CGI
---------------

1. Edit `hello.cgi` and change the shebang to the path to your installation of `python.exe`.

Open up the `hello.cgi` in your webbrowser, through Apache/XAMPP.
