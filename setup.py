from distutils.core import setup
from Cython.Build import cythonize

setup(
  name = 'Chatcity app',
  ext_modules = cythonize("client.pyx"),
)