from setuptools import setup, find_packages


setup(
    name="my_plugin",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Django'
    ],
    entry_points={
        'console_scripts': [
            'my_plugin_install=my_plugin.install:install',  
        ],
    },
    setup_requires=['wheel'],
    scripts=['enable_plugin.py'],
)