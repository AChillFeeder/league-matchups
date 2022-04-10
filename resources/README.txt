You'll have issues installing pycurl from pip
use the file here to install it directly
pip install pycurl-7.45.1-cp38-cp38-win32.whl


if you have a different architecture:
    >import platform
    >platform.architecture()

for more info, see answer here:
https://stackoverflow.com/questions/28568070/error-filename-whl-is-not-a-supported-wheel-on-this-platform
