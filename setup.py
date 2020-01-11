try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'Matthew Marie-Rhodes',
    'url': 'Url to get it at',
    'download_url': 'Where to download it.',
    'author_email': 'matthewmr@protonmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['Name'],
    'scripts': [],
    'name': 'projectname'
}

setup(**config, install_requires=['flask'])
