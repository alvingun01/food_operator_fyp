from setuptools import setup, find_packages

setup(
    name='food-pickup-operator',
    version='1.0.0',
    packages=['food_pickup_operator'],
    install_requires=[
        'async-generator==1.10',
        'attrs==22.1.0',
        'certifi==2022.12.7',
        'exceptiongroup==1.0.4',
        'h11==0.14.0',
        'idna==3.4',
        'outcome==1.2.0',
        'PySocks==1.7.1',
        'selenium==4.7.2',
        'sniffio==1.3.0',
        'sortedcontainers==2.4.0',
        'trio==0.22.0',
        'trio-websocket==0.9.2',
        'urllib3==1.26.13',
        'wsproto==1.2.0',
    ]
)