from setuptools import setup, find_packages

setup(
    name="tdbinlog_reader",
    version="0.1.0",
    packages=['tdbinlog_reader'],
    install_requires=['tgcrypto'],
    #entry_points={
    #    'console_scripts': ['tdbinlog_reader=main']
    #}    
    # Automatically finds packages in your directory structure
    #packages=find_packages(include=["tdbinlog_reader", "tdbinlog_reader.*"]),
)
