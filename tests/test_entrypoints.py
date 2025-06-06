def test_hyp3_gather_landsat(script_runner):
    ret = script_runner.run(['python', '-m', 'hyp3_gather_landsat', '-h'])
    assert ret.success
