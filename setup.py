from setuptools import setup, find_packages

setup(name='boo',
      version='0.1',
      description='Russian corporate reports 2012-2017',
      url='http://github.com/ru-corporate/sandbox',
      author='Evgeniy Pogrebnyak',
      author_email='e.pogrebnyak@gmail.com',
      license='MIT',
      packages=find_packages(),
      zip_safe=False, 
      install_requires=[
        "requests",
        "pandas",
        "tqdm"
        ]
      )
