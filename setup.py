import os

from setuptools import setup, find_packages


def _packages():
    pkg_name = 'conduit'
    packages = [f'{pkg_name}.{sub_pkg_name}' for sub_pkg_name in
                find_packages(os.path.join(os.path.dirname(__file__), pkg_name))
                ]
    packages.append(pkg_name)
    return packages


setup(name='tw2019-ui-tests',
      version='0.1',
      description='realworld sample app ui tests',
      url='https://github.com/dduleba/tw2019-ui-tests',
      author='Dariusz Duleba',
      author_email='ddarus@gmail.com',
      packages=_packages(),
      package_data={},
      include_package_data=True,
      install_requires=['Faker'],
      zip_safe=False,
      license='MIT'
      )
