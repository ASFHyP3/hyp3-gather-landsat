"""gather-landsat processing for HyP3."""

import logging
from argparse import ArgumentParser

from hyp3lib.aws import upload_file_to_s3

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
        type=str,
        nargs='+',
        help='LON LAT',
    )

    args = parser.parse_args()

    logging.basicConfig(
        format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO
    )

    product_file = process_gather_landsat(location=args.location, start_date=args.start_date, end_date=args.end_date)

    if args.bucket:
        upload_file_to_s3(product_file, args.bucket, args.bucket_prefix)


if __name__ == '__main__':
    main()
