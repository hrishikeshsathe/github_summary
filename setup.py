try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Github Summary',
    'author': 'Hrishikesh Sathe',
    'url': 'https://github.com/hrishikeshsathe/github_summary',
    'download_url': 'https://github.com/hrishikeshsathe/github_summary',
    'author_email': 'hrishikesh.sathe90@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['github_summary'],
    'scripts': [],
    'name': 'Github Summary'
}

setup(**config)