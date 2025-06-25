# HyP3 gather-landsat

Plugin to get landsat scenes from an input location

## Usage
The `hyp3_gather_landsat` command line tool can be run using the following structure:
```bash
python -m hyp3_gather_landsat --start-date 2025-05-01 --end-date 2025-05-07 --location -163.97 54.756
```
Where:

* `--start-date` is the start date of the images in the format (YYYY-MM-DD)
* `--end-date` is the end date of the images in the format (YYYY-MM-DD)
* `--location` is the longitude and latitude coordinates for the location point in the format `lon lat`

## Developer Setup
1. Ensure that conda is installed on your system (we recommend using [mambaforge](https://github.com/conda-forge/miniforge#mambaforge) to reduce setup times).
2. Download a local version of the `hyp3-gather-landsat` repository (`git clone https://github.com/ASFHyP3/hyp3-gather-landsat.git`)
3. In the base directory for this project call `mamba env create -f environment.yml` to create your Python environment, then activate it (`mamba activate hyp3-gather-landsat`)
4. Finally, install a development version of the package (`python -m pip install -e .`)

To run all commands in sequence use:
```bash
git clone https://github.com/ASFHyP3/hyp3-gather-landsat.git
cd hyp3-gather-landsat
mamba env create -f environment.yml
mamba activate hyp3-gather-landsat
python -m pip install -e .
```

## Contributing
Contributions to the HyP3 gather-landsat plugin are welcome! If you would like to contribute, please submit a pull request on the GitHub repository.

## Contact Us
Want to talk about HyP3 gather-landsat? We would love to hear from you!

Found a bug? Want to request a feature?
[open an issue](https://github.com/ASFHyP3/hyp3-gather-landsat/issues/new)
