import price_info as pi

def test_total_cost_shopping():
    result=0
    test_dict = {'apple' : 12, 'orange':14, 'watermelon': 65, 'pineapple': 27, 'pear' : 9, 'papaya': 29, 'pomegranate': 49 }
    output=205
    result = pi.total_cost_shopping(test_dict)

    assert(result==output)

def test_cost_of_fruits():
    result=0
    test_dict = {'apple' : 12, 'orange':14, 'watermelon': 65, 'pineapple': 27, 'pear' : 9, 'papaya': 29, 'pomegranate': 49 }
    output=140
    result = pi.cost_of_fruits("orange", 10, test_dict)

    assert(result==output)