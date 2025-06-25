from pathlib import Path


def test_data_directory():
    here = Path(Path(__file__).parent)
    return here / 'data'
