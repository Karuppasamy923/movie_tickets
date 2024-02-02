from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in movie_tickets/__init__.py
from movie_tickets import __version__ as version

setup(
	name="movie_tickets",
	version=version,
	description="Movie ticket booking app with frappeUI",
	author="karuppasamy",
	author_email="karuppasamylivak@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
