# Travis Encrypt

This is a very simple Python 3.5 project to implement encrypting variables in Travis. Currently the Windows Travis gem doesn't work so I figured I'd implement my own script to do the encryption.

# Concept
The script takes a repository and user or organisation name and then uses that to fetch the public key from Travis associated with that repository. It then encrypts the string and spits it back out in a format you can copy into your `.travis.yml` file.  

# Usage
The script takes three arguments a `--org` or `--user`, `--repo`, and a string.

## Example

```
> C:\Users\Arran\Documents\GitHub\BricksandMortar\travis-encrypt>python main.py --org BricksandMortar --repo IdealPostcodes GH_TOKEN=8573974759387459374934875395dfw457
> - secure: f7o5a3UblI1/XzlF94r8ckE6knK27/j2LczEnjLYEwsaYXDgo1Xm99XdsVjaMJuythVHo7fp6q6b0QJg6TUulWPQbHSH7WB73BBon6qt3sXcQytiHnILfy2+nwSlGRp+baOGt3j3BcJhrN2/ujxG6py8mys1ldmgPu3FIJvGHpJ9WhXyIixy2pHOxt1Tnq8bNXvxgsr6RxY0lYGNKnK0ocJfspPBl8FUFMHDZ6+9fv8k28VsZZrFNghymib7BNWxj4e1mer745Kn5ZgiBsjpy96OlG4XGoMzBh+3CwVuN62h4O9qcsZz74sM0qzThwBn5O5YUNeBL2zAfUhAJcdFig2Q4w6GP3Al6rw+UDDxrkWj1WopN4fCaxIAxyizwF8mODKby6pJKbLcfeq/MslChW/I+qTF9EkZt2auUChVXExgCs6jz1ix6VIM6v31x8Zr/Y6TH3FpT/JQU4NkXATWv46Xdr6n76Tup8oEnm6U9+rEeD1B/TdSiDvTx33s4wUDWm840n+pzVhHmuVZyz4x6yiKDn4ESs0WoojIQr7/PYAioqr9zqOu8V6AOhu8MGqIOsq8dBTWIuqUvHgX4FFT2l8ha+nmg18YY6lxjrVmC03vKfKmKi7WaLeMnCXVuopgSnS5+jlFi7Fbk/iQcGjteeFTAMyfMQy/sqsrXJlx9go=
```
