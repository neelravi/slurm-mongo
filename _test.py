import unittest
from slurm_usage_to_mongodb import main


class TestSlurmMongo(unittest.TestCase):

    def test_main(self):
        start = "01-01-2022"
        end = "01-02-2022"
        host = "user@hostname"
        connection = "localhost"
        port = 27017
        database = "Slurm"
        collection = "Usage"
        args = [start, end, host, connection, port, database, collection]
        self.assertIsNone(main(args))


if __name__ == '__main__':
    unittest.main()
