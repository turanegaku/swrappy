from setuptools import setup, find_packages
from timeline import __author__, __version__, __licence__

setup(
        name                = 'timeline',
        version             = __version__,
        description         = 'slack wrapper get and post timeline',
        licence             = __licence__,
        author              = __author__,
        author_email        = 'turanegaku@gmail.com',
        url                 = 'https:github.com/turanegaku/timeline.git',
        keywords            = 'slack github pip python',
        packages            = find_packages(),
        install_requires    = ['requests'],
        )
