from distutils.core import setup as s, Extension as x

s(name='m',
  version='1.1',
  ext_modules=[x('m', ['m.c'])])
