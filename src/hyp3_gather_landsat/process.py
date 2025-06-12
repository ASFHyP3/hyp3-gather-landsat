"""gather-landsat processing."""

import logging
import os
from pathlib import Path

import pystac_client
from osgeo import gdal


gdal.UseExceptions()

LANDSAT_CATALOG_API = 'https://landsatlook.usgs.gov/stac-server'
LANDSAT_CATALOG = pystac_client.Client.open(LANDSAT_CATALOG_API)
LANDSAT_BUCKET = 'usgs-landsat'


log = logging.getLogger(__name__)

def get_lc2_path(metadata: dict) -> str:
    """Get Landsat link.

    Args:
        metadata: Dictionary from json file associated with the Landsat image.

    Returns:
        Bucket link for Landsat image.
    """
    if metadata['id'][3] in ('4', '5'):
        band = metadata['assets'].get('B2.TIF')
        if band is None:
            band = metadata['assets']['green']
    elif metadata['id'][3] in ('7', '8', '9'):
        band = metadata['assets'].get('B8.TIF')
        if band is None:
            band = metadata['assets']['pan']
    else:
        raise NotImplementedError(f'autoRIFT processing not available for this platform. {metadata["id"][:3]}')

    return band['href'].replace('https://landsatlook.usgs.gov/data/', f'/vsis3/{LANDSAT_BUCKET}/')

def process_gather_landsat(location: list, start_date: str, end_date: str) -> Path:
    """Download a Landsat image.

    Args:
        location: List with lon/lat coordinates.
        start_date:  The start date of the images
        end_date:  The end date of the images

    Returns:
        Filename of the downloaded image
    """
    os.environ['AWS_REGION'] = 'us-west-2'
    os.environ['AWS_REQUEST_PAYER'] = 'requester'
    gdal.SetConfigOption('AWS_REGION', 'us-west-2')
    gdal.SetConfigOption('AWS_REQUEST_PAYER', 'requester')
    
    lon=location[0]
    lat=location[1]
    search = LANDSAT_CATALOG.search(
             collections=['landsat-c2l1'], # Landsat 8 collection
             datetime=f'{start_date}/{end_date}',
             intersects={"type": "Point", "coordinates": [float(lon), float(lat)]}, # Coordinates
         )
    for item in list(search.items()):
        url=get_lc2_path(item.to_dict())
        gdal.Translate(url.split('/')[-1],url)
    
    return Path(f'./{url.split('/')[-1]}')
