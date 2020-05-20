#blood_analysis.py

def HDL_analysis(HDL_result):
    if HDL_result >= 60:
        return "Good"
    elif 40 <= HDL_result < 60:
        return "Borderline"
    else:
        return "Bad"

def HDL_interface():
    print("HDL Interface")
    print("Please input the result in the following format:")
    print("  HDL=## where ## is the numeric result")
    HDL_input = input("Result: ")
    HDL_list = HDL_input.split("=")
    HDL_val = HDL_list[1]
    HDL_status = HDL_analysis(int(HDL_val))
    print(HDL_status)

def interface():
    print("My Blood Analysis Calculator")
    keep_running = True
    while keep_running:
        print("\nOptions:")
        print("1-HDL analysis")
        print("9-Quit")
        choice = input("Choose an option: ")
        if choice == '9':
            keep_running = False
        elif choice == '1':
            HDL_interface()
        
if __name__ == "__main__":
    interface()