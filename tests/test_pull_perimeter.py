from hyp3_gather_landsat import pull_perimeter


def test_get_product_name():
    extent = [-1.2, -0.1, 4.7, 5.8]
    start = '0000-00-00'
    end = '1111-11-11'
    assert pull_perimeter.get_name(extent, start, end) == 'FIRE_PERIMETER_W1_E5_S0_N6_00000000_11111111.json'
