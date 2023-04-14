import unittest
from slurm_usage_to_mongodb import main
import subprocess

class TestSlurmMongo(unittest.TestCase):

    def test_main(self):
        start = "01-01-2022"
        end = "01-02-2022"
        host = "user@hostname"
        connection = "localhost"
        port = 27017
        database = "Slurm"
        collection = "Usage"
        args = [start, end, host, "--connection", connection, "--port", str(port), "--database", database, "--collection", collection]

        # Construct the command as a list of strings
        command = ["python", "-m", "slurm_usage_to_mongodb", start, end, host, "--connection", connection, "--port", str(port), "--database", database, "--collection", collection]
        print("command: ", command)

        # Run the command as a subprocess and capture the output
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        print ("result: ", result)
        print ("result.stdout: ", result.stdout)
        print ("result.stderr: ", result.stderr)
        # Check that the subprocess ran successfully with no errors
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stderr, b"")  # Check that there were no errors

if __name__ == '__main__':
    unittest.main()
