from setuptools import setup, find_packages

setup(
    name="tdbinlog_reader",
    version="0.1.0",
    # Automatically finds packages in your directory structure
    packages=find_packages(include=["tdbinlog_reader", "tdbinlog_reader.*"]),
)
