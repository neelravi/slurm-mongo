import json
from pymongo import MongoClient
from datetime import datetime
import subprocess
import sys
import argparse


#add a main function that takes start_date and end_date as arguments, and move the code that downloads and uploads data to this function.

def main():
    # Define the remote host and command to execute

    # read the start and end dates from the command line using argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("start", help="start date in DD-MM-YYYY format")
    parser.add_argument("end", help="end date in DD-MM-YYYY format")
    parser.add_argument("host", help="host name in user@hostname format")

    parser.add_argument("--connection", help="MongoDB connection (default=localhost)", default="localhost")
    parser.add_argument("--port", help="port number", type=int, default=27017)

    parser.add_argument("--database", help="database name", default="Snellius")
    parser.add_argument("--collection", help="collection name", default="usage")


    args = parser.parse_args()

    start = args.start
    end = args.end
    host = args.host

    connection = args.connection
    port = args.port

    database = args.database
    collection = args.collection

    print ("Start date:                 ", start)
    print ("End date:                   ", end)
    print ("Supercomputer host:         ", host)
    print ("Database connection:        ", connection)
    print ("Database port:              ", port)
    print ("Database name:              ", database)
    print ("Database Collection name:   ", collection)


    # Define the remote host and command to execute

    command = 'accuse -d --raw --start ' + start + ' --end ' + end

    # Use subprocess to run the command on the remote host and fetch the output
    ssh = subprocess.Popen(['ssh', host, command],
                        shell=False,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE)
    output, error = ssh.communicate()

    # Convert the output to a list object
    output_list = output.decode('utf-8')

    # Print the output list
    # print(output_list)

    if output_list is None:
        print("No data found for the given dates")
        sys.exit(1)

    # write this to a file
    with open( start + '-to-' + end + '.json', 'w') as f:
        f.write(output_list)

    #Read the temp.json file. It contains a list of dictionaries
    with open(start + '-to-' + end + '.json') as json_file:
        list = json.load(json_file)

        print ("Number of records to be put in the database : ", len(list))
    # Iterate over the list of dictionaries
        for data in list:
            # print(data)

            # split facility_usage_description by pipe character and create a new dictionary
            usage_dict = {}
            if 'facility_usage_description' in data:
                usage_str = data['facility_usage_description']
                if usage_str.startswith('{') and usage_str.endswith('}'):
                    usage_str = usage_str[1:-1]
                for item in usage_str.split('|'):
                    key, value = item.split('=')
                    usage_dict[key.strip()] = value.strip()

            # merge the new dictionary with the original one
            data.update(usage_dict)

            # Drop the facility_usage_description field
            data.pop('facility_usage_description', None)

            # Convert the transaction_date field to a datetime object that mongodb can use
            date_obj = datetime.strptime(data['transaction_date'], '%Y-%m-%d')

            # update the data dictionary with the BSON date object
            data["transaction_date"] = date_obj
            data["date"] = date_obj

            print ("Trasanction date: ", date_obj, "::   SBUs charged: ", data["service_amount"])

            # Convert the 'end' field to a datetime object that mongodb can use
            end_obj = datetime.fromtimestamp(int(data['end']))

            # update the data dictionary with the BSON date object
            data["end"] = end_obj

            client = MongoClient( connection, port)
            db = client[database]
            Collection = db[collection]

            # Insert the data into the database.
            # Insert the fields that are changed to datetime objects
            # Insert to the collection named 'usage' only if the record does not exist

            Collection.update_one(data, {"$set": data}, upsert=True)








