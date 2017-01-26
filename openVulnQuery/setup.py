from setuptools import setup

setup(name='OpenVulnQuery',
      version='1.23',
      description='A python-based module(s) to query the Cisco PSIRT openVuln API.',
      url='https://github.com/CiscoPSIRT/openVulnAPI/tree/master/openVulnQuery',
      author='Bradley Korabik, Parash Ghimire',
      author_email='bkorabik@cisco.com, pghimire@cisco.com',
      license='The MIT License (MIT)',
      packages=['openVulnQuery'],
      entry_points={
          'console_scripts':
              ['openVulnQuery=openVulnQuery.main:main']
          },
      install_requires=[
          'argparse==1.4.0',
          'requests==2.10.0'
      ],
      zip_safe=False,)
