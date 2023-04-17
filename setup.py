from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='slurm_mongo',
    version='1.0.7',
    packages=['./'],
    install_requires=[
        'pymongo',
    ],
    entry_points={
        'console_scripts': [
            'slurm_mongo=slurm_usage_to_mongodb:main',
        ],
    },
    author='Ravindra Shinde',
    author_email='r.l.shinde@utwente.nl',
    description='A package to download slurm usage from a supercomputer and upload it to MongoDB',
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords='slurm usage uploader mongodb',
    url='https://github.com/neelravi/slurm-mongo',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Operating System :: OS Independent',
        'Topic :: Scientific/Engineering',
        'Topic :: System :: Distributed Computing',
        'Topic :: Database :: Database Engines/Servers',
    ],
)
