# Unit Test for blood_analysis.py


def test_HDL_analysis():
	from blood_analysis import HDL_analysis
	answer = HDL_analysis(70)
	expected = "Good"
	assert answer == expected  

    
def test_HDL_analysis_borderline():
    from blood_analysis import HDL_analysis
    answer = HDL_analysis(45)
    expected = "Borderline"
    assert answer == expected
    
    
def test_HDL_analysis_bad():
    from blood_analysis import HDL_analysis
    answer = HDL_analysis(20)
    expected = "Bad"
    assert answer == expected
    
    
def test_LDL_analysis_normal():
    from blood_analysis import LDL_analysis
    answer = LDL_analysis(120)
    expected = "Normal"
    assert answer == expected