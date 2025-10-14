import datetime as dt
import geopandas as gpd
import requests
from argparse import ArgumentParser
from owslib.ogcapi.features import Features


def pull_perimeter():
    print('HERE WE WILL PULL THE PERIMETER')


def main() -> None:
    parser = ArgumentParser()
    parser.add_argument('--bucket', help='AWS S3 bucket HyP3 for upload the final product(s)')
    parser.add_argument('--bucket-prefix', default='', help='Add a bucket prefix to product(s)')
    parser.add_argument('--start-date', type=str, help='Start date of the images (YYYY-MM-DD)')
    parser.add_argument('--end-date', type=str, help='End date of the images (YYYY-MM-DD)')
    # TODO: Your arguments here
    parser.add_argument(
        '--extent',
        type=str.split,
        nargs='+',
        help='min_lon min_lat max_lon max_lat',
    )

    args = parser.parse_args()

    args.extent = [item for sublist in args.extent for item in sublist]

    pull_perimeter()
