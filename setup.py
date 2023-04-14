from setuptools import setup, find_packages

setup(
    name='slurm_mongo',
    version='0.1',
    packages=find_packages(),
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
    keywords='slurm usage uploader mongodb',
    url='https://github.com/neelravi/slurm-mongo',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
)
