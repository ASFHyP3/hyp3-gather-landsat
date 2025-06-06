#!/bin/bash --login
set -e
conda activate hyp3-gather-landsat
exec python -um hyp3_gather_landsat "$@"
