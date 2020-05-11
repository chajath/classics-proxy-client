# coding: utf-8

"""
    Classics Proxy API

    Proxy API for fetching Classic Sino-Korean Literature from various corpora  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "classics-proxy-client"
VERSION = "0.0.1"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="Classics Proxy API",
    author="OpenAPI Generator community",
    author_email="team@openapitools.org",
    url="https://github.com/chajath/classics-proxy-client",
    keywords=["OpenAPI", "OpenAPI-Generator", "Classics Proxy API"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description="""\
    Proxy API for fetching Classic Sino-Korean Literature from various corpora  # noqa: E501
    """
)
