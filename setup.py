from setuptools import setup

setup(
    name='News-Breaker',
    version='1.0',
    py_modules=['index'],
    install_requires=[
        'Click', 'requests'
    ],
    entry_points='''
        [console_scripts]
        news=index:cli
    '''
)
