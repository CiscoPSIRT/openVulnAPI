from setuptools import setup, find_packages

setup(name='OpenVulnQuery',
      version='1.27',
      description='A python-based module(s) to query the Cisco PSIRT openVuln API.',
      url='https://github.com/CiscoPSIRT/openVulnAPI/tree/master/openVulnQuery',
      author='Omar Santos',
      author_email='os@cisco.com',
      license='The MIT License (MIT)',
      packages=find_packages(exclude=["tests"]),
      entry_points={
          'console_scripts':
              ['openVulnQuery=openVulnQuery.main:main']
          },
      install_requires=[
          'argparse>=1.4.0',
          'requests>=2.10.0'
      ],
      zip_safe=False,)
