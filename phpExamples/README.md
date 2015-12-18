# PHP-based sample clients.
## vulnapicm.php
vulnapicm.php is a brief example about how to get an access token via Oauth2 and perform a request to one of the APIs from serverside PHP code. A couple of clientside Javascript lines are also used to beautify the json response, but those are not essential to the example.

vulnapicm.php relies on the thephpleague/[oauth2-client](https://github.com/thephpleague/oauth2-client) library for performing the OAuth2 operations.
In order to deploy thephpleague/oauth2-client in your repository you will have to satisfy all of its dependencies, eg: GuzzleHttp, random-lib, security-lib, etc.. the easiest way to achieve this is to use the [composer](https://getcomposer.org) dependency manager.

For composer installation instructions please see:
* [Introduction and installation](https://getcomposer.org/doc/00-intro.md)

and for operation:
* [Basic usage](https://getcomposer.org/doc/01-basic-usage.md)

in practice once you donwload this folder, thanks to the composer.json file, you will be able to invoke:
```
php composer.phar install
```
and that should download and install recursively all the dependencies.

After that please edit vulnapicm.php to setup your 
1. client ID
2. client secret 
3. your redirect URL
as displayed on the Cisco API Console, and you should be good to go.


