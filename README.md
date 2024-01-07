Helps 
- https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment
- https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#install-a-specific-package-version
- https://gabrieldemarmiesse.github.io/python-on-whales/

install (windows)
- py -m venv .venv

prepare pip
- py -m pip install --upgrade pip
- py -m pip --version

(Linux Bash)
- source .venv/Scripts/activate
- which python

(Windows)
- .venv\Scripts\activate
- where python

(DEACTIVE)
- deactivate

Add Deps
- py -m pip install

Requirements
- py -m pip install -r requirements.txt

Export
- py -m pip freeze
