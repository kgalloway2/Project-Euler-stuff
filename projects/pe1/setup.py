try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'Keaton Galloway',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'keatongalloway@yahoo.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['pe1'],
    'scripts': [],
    'name': 'projectname'
}

setup(**config)