import Lab2.bmi as bmi

def test_bmi_normal_weight():
    result=[]
    input_weight=57
    input_height=1.73
    test_output=0
    result=bmi.calculate_bmi(input_height,input_weight)
    assert (result==test_output)