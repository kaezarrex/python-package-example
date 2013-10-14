from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='funniest',
      version='0.1',
      description='The funniest joke in the world',
      long_description=readme(),
      url='http://github.com/storborg/funniest',
      author='Flying Circus',
      author_email='flyingcircus@example.com',
      license='MIT',
      packages=['funniest', 'hello'],
      scripts=['bin/funniest-joke'],
      entry_points = {
          'console_scripts': ['funniest-joke2=funniest.command_line:main'],
      },
      install_requires=[
          'markdown',
      ],
      test_suite='nose.collector',
      test_requite=['nose'],
      include_package_data=True,
      zip_safe=False)
