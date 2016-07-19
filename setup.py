from setuptools import setup

setup(
    name='cffi_glpk',
    version='0.1',
    url='https://github.com/cfblaeb/cffi_glpk',
    author='laeb',
    author_email='laeb@biosustain.dtu.dk',
    description='CFFI bindings for GLPK',

    setup_requires=["cffi>=1.0.0"],
    cffi_modules=["cffi_glpk/cffi_glpk_build.py:ffibuilder"],
    install_requires=["cffi>=1.0.0"],
)
