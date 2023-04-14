# Slurm-mongo
[![Python Package](https://github.com/neelravi/slurm-mongo/actions/workflows/python-publish.yml/badge.svg?branch=main)](https://github.com/neelravi/slurm-mongo/actions/workflows/python-publish.yml)

[![PyPI version](https://badge.fury.io/py/slurm-mongo.svg)](https://badge.fury.io/py/slurm-mongo)


Slurm-Mongo is a Python package that downloads SLURM usage data from a supercomputer and uploads it to MongoDB.

## Installation

You can install Slurm-Mongo using pip:

```bash
pip install slurm-mongo
```

## Usage

You can use Slurm-Mongo by running the `slurm_mongo` command followed by the start date, end date, and supercomputer host name in user@hostname format:

```bash
slurm_mongo start_date end_date supercomputer_host_name
```

## Example

```bash
slurm_mongo '2017-01-01' '2017-01-02' 'shinde@snellius.surf.nl'
```

By default, Slurm-Mongo will connect to a MongoDB instance running on `localhost:27017` and will store the data in a database called "Snellius" and a collection called "Usage". You can customize the MongoDB connection and database/collection names by using the optional `--connection`, `--port`, `--database`, and `--collection` flags:

```bash
slurm_mongo start_date end_date supercomputer_host_name --connection mongo.example.com --port 12345 --database MySlurm --collection MyUsage
```

## License

Slurm-Mongo is released under the MIT License. See LICENSE for more information.

## Issues

If you encounter any issues with Slurm-Mongo, please report them on the GitHub issue tracker.

## Contact

Contact the author Dr. Ravindra Shinde at r.l.shinde@utwente.nl