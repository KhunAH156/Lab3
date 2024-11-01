import employee_info as em

def test_get_employees_by_age_range():
    result=[]
    test_list=[
        {"name": "John", "age": 30},
        {"name": "Khun", "age": 19},
        {"name": "Baw", "age": 24},
        {"name": "Jason", "age": 35}
    ]
    lower_limit = 10
    upper_limit = 31

    output=[{"name": "John", "age": 30},
            {"name": "Khun", "age": 19},
            {"name": "Baw", "age": 24}
            ]

    result=em.get_employees_by_age_range(lower_limit,upper_limit, test_list)

    assert(result==output)

def test_calculate_average_salary():
    result=[]
    test_list=[
        {"name": "John", "age": 30, "salary":50000},
        {"name": "Khun", "age": 19, "salary":90000},
        {"name": "Baw", "age": 24, "salary":40000},
        {"name": "Jason", "age": 35, "salary":60000}
    ]
    output=60000

    result=em.calculate_average_salary(test_list)

    assert(result==output)

def test_get_employee_department():
    result=[]
    test_list = [
    {"name": "Baw", "age": 30, "department": "Sales", "salary": 50000},
    {"name": "Linn", "age": 25, "department": "Marketing", "salary": 60000},
    {"name": "Min", "age": 23, "department": "Marketing", "salary": 56000},
    {"name": "Waiyan", "age": 35, "department": "Engineering", "salary": 70000},
    {"name": "Khun", "age": 32, "department": "Engineering", "salary": 65000},
    {"name": "Lee", "age": 40, "department": "Sales", "salary": 60000}
    ]
    output=[
        {"name": "Baw", "age": 30, "department": "Sales", "salary": 50000},
        {"name": "Lee", "age": 40, "department": "Sales", "salary": 60000}
    ]
    department="Sales"
    result=em.get_employees_by_dept(department, test_list)

    assert(result==output)