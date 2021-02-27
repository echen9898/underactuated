import sys
from urllib.request import urlretrieve
import warnings

assert 'google.colab' in sys.modules, (
    "This script is intended for use on Google Colab only.")

urlretrieve(
    "http://underactuated.csail.mit.edu/scripts/setup/setup_underactuated_colab.py",  # noqa
    "setup_underactuated_colab.py")

import setup_underactuated_colab as new_setup  # noqa
warnings.warn("jupyter_setup.py is deprecated.  Please use"
              " setup_underactuated_colab.py instead.")


def setup_drake():
    new_setup.setup_drake(version='0.27.0', build='release')


def setup_underactuated():
    new_setup.setup_underactuated(
        underactuated_sha='1dca1b915977aeec9f327d61aaeac4cfb9c6b408',
        drake_version='0.27.0',
        drake_build='release')
