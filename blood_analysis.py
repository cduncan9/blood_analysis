#blood_analysis.py

def LDL_analysis(LDL_res):
    if LDL_res < 130:
        return "Normal"
    elif 130<=LDL_res<160:
        return "Borderline High"
    elif 160<=LDL_res<190:
        return "High"
    else:
        return "Very High"


def HDL_analysis(HDL_result):
    if HDL_result >= 60:
        return "Good"
    elif 40 <= HDL_result < 60:
        return "Borderline"
    else:
        return "Bad"


def Test_interface():
    print("Analysis Interface")
    print("Please input the result in the following format:")
    print("  ***=## where *** is the test and ## is the numeric result")
    Test_input = input("Result: ")
    Test_list = Test_input.split("=")
    Test_type = Test_list[0]
    Test_val = Test_list[1]
    
    if Test_type == 'LDL':
        Test_status = LDL_analysis(int(Test_val))
    else:
        Test_status = HDL_analysis(int(Test_val))
    
    print("Your results for your {} test are {}".format(Test_type,Test_status))

def interface():
    print("My Blood Analysis Calculator")
    keep_running = True
    while keep_running:
        print("\nOptions:")
        print("1-Test analysis")
        print("9-Quit")
        choice = input("Choose an option: ")
        if choice == '9':
            keep_running = False
        elif choice == '1':
            Test_interface()
        
if __name__ == "__main__":
    interface()