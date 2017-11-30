Try out plain CGI-scripts
===================================

Lets see if CGI works on your webserver.

Open the scripts and they should state a message saying (in HTML):

```html
<h1>Hello The World of Web</h1>
<p>Ohhh! CGI works!
```



Enable CGI in Apache
----------------------------------

Enable the CGI mod, if not already enabled.

```
sudo a2enmod cgi
```

Enable CGI in the Apache config file, within a `<directory>` directive.

```
Options +ExecCGI
AddHandler cgi-script .cgi
```
