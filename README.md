# Shamir's Secret Sharing
[![Generic badge](https://img.shields.io/badge/version-3.1.26-<COLOR>.svg)](https://shields.io/)
[![Open Source Love png1](https://badges.frapsoft.com/os/v1/open-source.png?v=103)](https://github.com/ellerbrock/open-source-badges/)
[![Generic badge](https://img.shields.io/badge/contributors-1-blue)](https://shields.io/)  
[![forthebadge made-with-python](https://forthebadge.com/images/badges/made-with-python.svg)](https://www.python.org/)  


## Table of contents
* [About the Project](#about-the-project)
* [Getting Started](#getting-started)
    * [Prerequisites](#prerequisites)
    * [Installation](#installation)
* [Usage](#usage)  
    * [Shares File](#shares-file)
    * [Tests](#tests)
* [Documentation](#documentation)
* [Contact](#contact)
* [Acknowledgements](#Acknowledgements)


# About the Project
A basic cli app to encrypt and decrypt files using *Shamir's Secret Sharing Scheme* and *AES*.  
Already been tested with the following file type:  
 * `.pdf`
 * `.tex`
 * `.txt`
 * `.py`
 * `.jpg`
 > But it should work with any type of file

# Getting Started
Since this app is all made with `Python` you're going to need some python-libraries and utilities listed below.

## Prerequisites
* First check that your current `Python` version is `Python 3.6` or above, by running the following command on your terminal:

    ```shell
    $ python --version
    ```
    > `Python 3.8+` is recommended 

    Note that in some linux distros you'll need to run it as: 
    ```shell
    $ python3 --version
    ```


* You migth as well check if you have PyPI as your Python package installer:  
  Since this process vary for every Linux distro, I'll link you to an article explanning how to set
  [PyPI](https://www.tecmint.com/install-pip-in-linux/) up.  

## Instalation
1. Clone the repo  
    ```shell
    $ git clone https://github.com/DiXap/ShamirsSecretSharing.git
    ```

2. Move to project's `dir` and run the following
    ```shell
    $ pip install -r requirements.txt
    ```

3. The step above is going to automatically install packages needed for this project.  
If you want to install them manually, here's a list with the packages:
    * `pycryptodome`
    * `pytest`
    * `numpy`

You should have the following modules already in your python library, but here's a list of them if you want to check them:  
		* `sys`
		* `getpass`
		* `pathlib`
		* `functools`
		* `random`
		* `time`
		* `sys`
		* `os`
		* `platform`
		* `unittest`

# Usage
Since this is a `cli` app, you're need to know the syntaxis:
```shell
$ python main.py <COMMAND> [COMMANDS ARGS]
```
where:  
* `<COMMAND>`, could be one of the following:
    | Command      | Description                           |
    | -----------  | :------------------------------------:|
    | `-c`         | Enable *encryption* mode              |
    | `-d`         | Enable *decryption* mode              |


* `[COMMANDS ARGS]`, once a mode is enabled, proced with the corresponding arguments:   

    | Encrypt                       | Description                                                      |
    | ----------------------------  | :---------------------------------------------------------------:|
    | `<share's destinaton file>`   | File where the `n` evaluations of the polynomial will be stored  |
    | `<n>`                         | Total number of evaluations such as `n>2`                        |
    | `<k>`                         | Minimun required evaluations to decrypt such as `1<k<=n`         |
    | `<file to encrypt>`           | File to encrypt                                                  |

    *Encryption* example:  

	```shell
	$ python main.py -c /PATH/TO/shares.frg 13 7 /PATH/TO/very-secret-doc.pdf
	```
  Note that you can grab the to-encrypt file from wherever place you have it stored, same goes for the shares' file, as they'll be dropped inside this project directory
.
  > You can use relative paths only if the file is inside project's `dir`

  You can specify the extension for the shares' file, altough if you leave it without one, it won't affect further decryption. <sup>[**1**](#shares-file)</sup>  
		

   | Decrypt                | Description                                                         |
   | ---------------------  | :------------------------------------------------------------------:|
   | `<file to decrypt>`    | File to decrypt                                                     |
   | `<file with shares>`   | File containing all or at least the minimum evaluations to decrypt  |

 	 *Decryption* example:

	 ```shell
	 $ python main.py -d /PATH/TO/very-secret-doc.pdf.aes /PATH/TO/shares.frg
	 ```
   Note that you can grab the encrypted file from wherever place you have it stored, same goes for the shares' file.

  > You can use relative paths only if the file is inside project's `dir`

  No need to have your shares stored in a file with a specific extension. <sup>[**1**](#shares-file)</sup>  


   At any given time you can pass `--help` or `-h` to show help:
   ```shell
   $ python main.py --help
   ```
<!--
For example, you can pass the following command:
```shell
$ python main.py /PATH/TO/IMAGE -s --w
```
and the program will show and write the image  
-->

<!--img src="./dump/11773-seg.jpg" alt="drawing" width="500"/-->  


<!--Regardless of your flag choices, the app will always display the CCI in your terrminal:
```script
$ python main.py /PATH/TO/IMAGE -s --d --w
    CCI for image exmaple.jpg is X.XX%
```

Images will always be dumped inside `./dump` folder, so please, don't delete it.  
You can modify this setting in `IPP.py`:
```python
def write(self, name: str, image='b&w', path='dump/'): # change path='' value
    ...
```
-->

### Shares File
Shares will be written as it follows:  
```shell
XXXXXXXXXXXXXXXXXXXX,YYYYYYYYYYYYYYYYYYYYYY
XXXXXXXXXXXXXXXXXXXX,YYYYYYYYYYYYYYYYYYYYYY
```
As long as they're formatted as the above, shares' file extension shouldn't be a problem.  
Already tested with the following extensions:
 * `.txt`
 * `.frg`
 * `plain text` (without extension)
> You can even write your own file with the shares throwed by the encryption process

## Tests

These test cases were coded to demostrate functions' error handling.  
Feel free to play around with them at `tests/`.
To run them you'll need to excecute the following from project's directory:  
```shell
$ python -m pytest -v
```

# Documentation

All documentation was generated using `pydoc`. You'll find it inside `docs`.  
I personaly recommend switching to `docs/` and then starting a local server to visualize them:
```shell
$ python -m http.server
```

# Contact
Diego J. Padilla  
[<img src="https://img.shields.io/badge/gmail-D14836?&style=for-the-badge&logo=gmail&logoColor=white"/>](https://mail.google.com/mail/?view=cm&source=mailto&to=dpadlara@gmail.com) <img src="https://img.shields.io/badge/discord-Dixap@5792-181717?style=for-the-badge&logo=discord" />


# Acknowledgements
* [ForTheBadge](http://ForTheBadge.com) 
* [Badges 4 README.md Profile](https://github.com/alexandresanlim/Badges4-README.md-Profile)


---
![forthebadge biult-with-love](https://forthebadge.com/images/badges/built-with-love.svg) 
[![forthebadge powered-by-electricity](https://forthebadge.com/images/badges/powered-by-electricity.svg)](http://ForTheBadge.com)  

---
[Go up](#cloud-coverage-index-calculator)
