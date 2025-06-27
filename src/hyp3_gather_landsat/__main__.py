"""gather-landsat processing for HyP3."""

import logging
from argparse import ArgumentParser

from hyp3_gather_landsat.process import process_gather_landsat


def main() -> None:
    """HyP3 entrypoint for hyp3_gather_landsat."""
    parser = ArgumentParser()
    parser.add_argument('--bucket', help='AWS S3 bucket HyP3 for upload the final product(s)')
    parser.add_argument('--bucket-prefix', default='', help='Add a bucket prefix to product(s)')
    parser.add_argument('--start-date', type=str, help='Start date of the images (YYYY-MM-DD)')
    parser.add_argument('--end-date', type=str, help='End date of the images (YYYY-MM-DD)')
    # TODO: Your arguments here
    parser.add_argument(
        '--location',
        type=str.split,
        nargs='+',
        help='LON LAT',
    )

    args = parser.parse_args()

    args.location = [item for sublist in args.location for item in sublist]

    logging.basicConfig(
        format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO
    )

    process_gather_landsat(
        location=args.location,
        start_date=args.start_date,
        end_date=args.end_date,
        bucket=args.bucket,
        bucket_prefix=args.bucket_prefix,
    )


if __name__ == '__main__':
    main()
