from setuptools import setup, find_packages
 
setup(
  name='cal_fibonacci',
  version='0.0.1',
  description='A very basic fibonacci calculator',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='https://github.com/siddheshsagar/get_fibonacci.git',
  author='Siddhesh Sagar',
  author_email='siddheshsagar3182001@gmail.com',
  license='MIT', 
  packages=['get_fibonacci'],
 zip_safe = False
)
