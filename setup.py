from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))
with codecs.open(os.path.join(here, 'README.md'), encoding='utf-8') as fh:
  long_description = f'\n{fh.read()}'

setup(
  name='webfleet_connect',
  version='0.1.28',
  description='The WEBFLEET.connect API connects software applications with the Webfleet fleet management solution. Via WEBFLEET.connect you can enhance the value of all types of business solutions, including routing and scheduling optimization, ERP, Transport Management System (TMS), supply chain planning, asset management, and much more.',
  long_description=long_description,
  long_description_content_type='text/markdown',
  url='https://github.com/movomx/webfleet_connect_python',
  author='movomx',
  author_email='alex.guajardo@movomx.com',
  license='MIT License',
  packages=find_packages(),
  install_requires=['requests'],
  keywords=['python', 'webfleet', 'webfleet.connect', 'movomx', 'telemetry', 'gps'],
  classifiers=[
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Topic :: Software Development :: Libraries'
  ]
)
