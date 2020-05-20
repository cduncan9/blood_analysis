#blood_analysis.py

def HDL_interface():
    print("HDL")    
    pass

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