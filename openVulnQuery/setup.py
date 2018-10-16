from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='OpenVulnQuery',
      version='1.29',
      description='A python-based module(s) to query the Cisco PSIRT openVuln API.',
      url='https://github.com/CiscoPSIRT/openVulnAPI/tree/master/openVulnQuery',
      author=' Omar Santos',
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
