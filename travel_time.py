import googlemaps
import argparse, pprint, traceback
from datetime import datetime
from termcolor import colored
from typing import Dict

parser = argparse.ArgumentParser()
parser.add_argument("-k", "--key", help="Google API key", required=True)
parser.add_argument("-s", "--sources_filepath", help="Filepath of source locations", required=True)
parser.add_argument("-d", "--destinations_filepath", help="Filepath of destination locations", required=True)
parser.add_argument("-sbt", "--sort_by_time", help="Sort by travel time", action='store_true')
parser.add_argument("-m", "--mode", help="mode", required=False)
parser.add_argument("-l", "--language", help="language", required=False)
parser.add_argument("-a", "--avoid", help="avoid", required=False)
parser.add_argument("-u", "--units", help="units", required=False)
parser.add_argument("-dt", "--departure_time", help="departure time", required=False)
parser.add_argument("-at", "--arrival_time", help="arrival time", required=False)
parser.add_argument("-tm", "--transit_mode", help="transit mode", required=False)
parser.add_argument("-pr", "--transit_routing_preference", help="transit routing preference", required=False)
parser.add_argument("-mo", "--traffic_model", help="traffic model", required=False)
parser.add_argument("-r", "--region", help="region", required=False)
args = parser.parse_args()


# read a file and return each line in array
def read_file(filepath) -> [str]:
    all_lines = open(filepath, "r").read().splitlines()
    non_empty_lines = [line for line in all_lines if line]
    return non_empty_lines


# make client call and return distance matrix
def call_distance_matrix(client, sources, dests, **kwargs) -> Dict:
    # make call, get response matrix
    matrix = client.distance_matrix(origins=sources, destinations=dests, **kwargs)
    return matrix

# print data in desired format
# rows = list of elements for an origin, elements are a list of duration/distances from given origin to each dest
# matrix format: rows by origin, and columns
def handle_data(matrix, options, sort_by_time) -> None:
    print(colored("Configurations", attrs=['bold']))
    pprint.pprint(options)

    # for each source
    for s_index in range(0, len(matrix['origin_addresses'])):
        source_name = matrix['origin_addresses'][s_index]
        print("\n" + colored("From: " + source_name, 'green', attrs=['bold']))

        # list of elements for each destination for a given source
        elements_for_source = matrix['rows'][s_index]['elements']

        # sort original indices by duration (have to do this as destination_addresses not paired with data elements)
        if sort_by_time:
            indices = [i[0] for i in sorted(enumerate(elements_for_source), key=lambda k:k[1]['duration']['value'])]
        # use order from response (currently matches order of input)
        else:
            indices = range(0, len(matrix['destination_addresses']))

        # ensure that index of destination_addresses matches order of destination elements
        for d_index in indices:
            dest_name = matrix['destination_addresses'][d_index]
            duration = elements_for_source[d_index]['duration']['text']
            print(dest_name + " - " + colored(duration, 'red'))

    return


if __name__ == "__main__":
    # initialize client
    client = googlemaps.Client(key=args.key)

    # read sources and destinations from input files
    sources = read_file(args.sources_filepath)
    dests = read_file(args.destinations_filepath)

    # sort bool
    sort_by_time = args.sort_by_time

    # Set script args as dict, and delete custom arguments from argparse
    optional_params = vars(args)
    del optional_params["key"]
    del optional_params["sources_filepath"]
    del optional_params["destinations_filepath"]
    del optional_params["sort_by_time"]

    try:
        # get matrix
        matrix = call_distance_matrix(client, sources, dests, **optional_params)

        # print formatted data
        handle_data(matrix, optional_params, sort_by_time)

    except Exception as e:
        traceback.print_exc()

