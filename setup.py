import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='cffi_glpk',
    version='0.5',
    url='https://github.com/cfblaeb/cffi_glpk',
    author='laeb',
    author_email='laeb@dtu.dk',
    description='CFFI bindings for GLPK',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),

    setup_requires=["cffi>=1.0.0"],
    cffi_modules=["cffi_glpk/cffi_glpk_build.py:ffibuilder"],
    install_requires=["cffi>=1.0.0"],
)
