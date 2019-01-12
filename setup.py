from setuptools import setup

setup(
    name='savescum_helper',
    version='0.1.0',
    description='A simple tool to help people savescum',
    url='https://github.com/afk/savescum_helper',
    author='Efe Aydın',
    py_modules=['savescum_helper'],
    entry_points={
        'console_scripts': ['savescum_helper=savescum_helper:main']
    }
)