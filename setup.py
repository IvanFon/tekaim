from distutils.core import setup

setup(
    name='tekaim',
    version='1.4.0',
    description='A simple tool to take and upload screenshots to teknik.io',
    author='Ivan Fonseca',
    author_email='ivanfon@riseup.net',
    url='https://github.com/IvanFon/tekaim',
    license='GPL3',
    scripts=['tekaim'],
    data_files=[('', ['config.json'])]
)

