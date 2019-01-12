from setuptools import setup

setup(
    name="savescum_helper",
    version="0.1.0",
    description="A tool to back up saves when they are modified",
    url="https://github.com/afk/savescum_helper",
    author="Efe Aydın",
    py_modules=["savescum_helper"],
    entry_points={"console_scripts": ["savescum_helper=savescum_helper:main"]},
)
