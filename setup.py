from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in libms/__init__.py
from libms import __version__ as version

setup(
	name="libms",
	version=version,
	description="This is a Library Management System",
	author="Diya",
	author_email="libms@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
