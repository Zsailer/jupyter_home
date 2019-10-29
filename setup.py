
import os
import sys
from shutil import rmtree

from setuptools import find_packages, setup, Command
import setuptools

NAME = 'jupyter_home'
VERSION = '0.0.1'

with open("README.md", "r") as fh:
    long_description = fh.read()

here = os.path.abspath(os.path.dirname(__file__))


class UploadCommand(Command):
    """Support setup.py upload."""

    description = 'Build and publish the package.'
    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print('\033[1m{0}\033[0m'.format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status('Removing previous builds…')
            rmtree(os.path.join(here, 'dist'))
        except OSError:
            pass

        self.status('Building Source and Wheel (universal) distribution…')
        os.system('{0} setup.py sdist bdist_wheel --universal'.format(sys.executable))

        self.status('Uploading the package to PyPI via Twine…')
        os.system('twine upload dist/*')

        sys.exit()


setup(
    name=NAME,
    version=VERSION,
    author="Jupyter Development Team",
    author_email="jupyter@googlegroups.com",
    description="A package that provides a simple transition away from Jupyter Notebook to Jupyter Server",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Zsailer/nbclassic",
    license='BSD',
    platforms="Linux, Mac OS X, Windows",
    packages=setuptools.find_packages(),
    install_requires=[
        'jupyter_server',
        'notebook<7',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    include_package_data=True,
    data_files=[
        # like `jupyter serverextension enable --sys-prefix`
        ("etc/jupyter/jupyter_server_config.d", [
            "jupyter-config/jupyter_server_config.d/jupyter_home.json"
        ])
    ],
    zip_safe=False,
    # $ setup.py publish support.
    cmdclass={
        'upload': UploadCommand,
    },
    entry_points = {
        'console_scripts': [
            'jupyter-home = jupyter_home.app:main'
        ]
    },
)